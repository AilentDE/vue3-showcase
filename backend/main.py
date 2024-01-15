from fastapi import FastAPI, Depends, Body, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from config.database_sqlite import get_db, engine
from models.model import Base, Coaches, CoachAreas, Requests, Users
from schemas.schema import CoachBase, RequestBase
import uuid
from datetime import datetime, timedelta, timezone

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# pip install python-jose[cryptography]
from jose import JWTError, jwt
# pip install passlib[bcrypt]
## bcrypt==4.0.1
# pip install python-multipart
from passlib.context import CryptContext
## 創建 CryptContext 實例
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = 'the_secret_key'
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

Base.metadata.create_all(bind=engine)
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, delete
db_dependency = Annotated[Session, Depends(get_db)]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=["*"],
)

# base
@app.get('/')
def home():
    return {'success': True}

# coach
@app.get('/coaches')
def coaches_list(db:db_dependency):
    stmt = select(Coaches)
    coaches = db.execute(stmt).scalars().all()

    result = []
    for coach in coaches:
        coach_data = {
            "id": str(coach.userId),
            "firstName": coach.firstName,
            "lastName": coach.lastName,
            "areas": [area.areaName for area in coach.areas],
            "description": coach.description,
            "hourlyRate": coach.hourlyRate,
        }
        result.append(coach_data)
    return JSONResponse(result)

@app.post('/coach')
def add_coach(db:db_dependency, coach_data: Annotated[CoachBase, Body()], token: Annotated[str, Depends(oauth2_scheme)]):

    # get user_id from token
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"verify_exp": True, "leeway": 10}
        )
        user_id = uuid.UUID(payload.get('userId'))
        if user_id is None:
            raise credentials_exception
    except JWTError as e:
        print(f"JWT Error: {e}")
        raise credentials_exception

    # insert coachData
    stmt = insert(Coaches).values(
        userId = user_id,
        firstName=coach_data.firstName,
        lastName=coach_data.lastName,
        description=coach_data.description,
        hourlyRate=coach_data.hourlyRate
    )
    result = db.execute(stmt)
    # insert coachAreas
    coach_id = result.inserted_primary_key[0]
    for i, area in enumerate(coach_data.areas):
        db.execute(insert(CoachAreas).values(coachId=coach_id, areaName=area, sort=i))
    # commit
    db.commit()
    return JSONResponse({**coach_data.model_dump(), 'id': str(user_id)})

# request
@app.get('/requests')
def requests_list(db:db_dependency, token: Annotated[str, Depends(oauth2_scheme)]):
    
    # get user_id from token
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"verify_exp": True, "leeway": 10}
        )
        user_id = uuid.UUID(payload.get('userId'))
        if user_id is None:
            raise credentials_exception
    except JWTError as e:
        print(f"JWT Error: {e}")
        raise credentials_exception
    
    # select requests
    stmt = select(Requests).where(Requests.coachId == user_id)
    requests = db.execute(stmt).scalars().all()

    result = []
    for req in requests:
        req_data = {
           "id": str(req.id),
           "coachId": str(req.coachId),
           "userEmail": req.userEmail,
           "message": req.message
        }
        result.append(req_data)
    return JSONResponse(result)

@app.post('/request')
def add_request(db:db_dependency, request_data: Annotated[RequestBase, Body()]):
    # insert request
    stmt = insert(Requests).values(**request_data.model_dump())
    result = db.execute(stmt)
    request_id = result.inserted_primary_key[0]
    #commit
    db.commit()
    request_data.coachId = str(request_data.coachId)
    return JSONResponse({**request_data.model_dump(), 'id': str(request_id)})

def create_jws(data:dict, expire_delta_hours:int=1):
    # token expire time
    expire = datetime.now(tz=timezone.utc) + timedelta(hours=expire_delta_hours)
    exp = int(expire.timestamp())
    expISO = expire.isoformat().replace('+00:00', 'Z')

    data.update({
        'exp': exp,
        'expISO': expISO
    })
    encoded_jws = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM,
        headers={"alg": "HS256"}
    )
    return encoded_jws, expISO

# auth
@app.post('/register')
def register_user(db:db_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # check email used
    stmt = select(Users).where(Users.email == form_data.username)
    result = db.execute(stmt).scalar_one_or_none()
    if result:
        raise HTTPException(
            status_code=400,
            detail='Exited user.'
        )
    else:
        # create user
        stmt = insert(Users).values(
            email = form_data.username,
            password = pwd_context.hash(form_data.password)
        )
        result = db.execute(stmt)
        user_id = result.inserted_primary_key[0]
        #commit
        db.commit()
    
    # return user JWS
    encoded_jws, expISO = create_jws({'userId': str(user_id)})
    return {
        "accessToken": encoded_jws,
        "tokenType": "bearer",
        "tokenExpiration": expISO,
        "user": {
            "userId": str(user_id),
            "email": form_data.username
        }
    }

@app.post('/login')
def login_user(db:db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    # check email used
    stmt = select(Users).where(Users.email == form_data.username)
    result = db.execute(stmt).scalar_one_or_none()
    if not result:
        raise HTTPException(
            status_code=400,
            detail='Can not find this user.'
        )
    elif not pwd_context.verify(form_data.password, result.password):
        raise HTTPException(
            status_code=400,
            detail='Wrong password.'
        )
    else:
        user_id = result.id
    
    # return user JWS
    encoded_jws, expISO = create_jws({'userId': str(user_id)})
    return {
        "accessToken": encoded_jws,
        "tokenType": "bearer",
        "tokenExpiration": expISO,
        "user": {
            "userId": str(user_id),
            "email": form_data.username
        }
    }

@app.post('/clearUsers')
def clear_user(db:db_dependency):
    stmt = delete(Users)
    result = db.execute(stmt)
    print(result.__dict__)
    db.commit()
    return {'success': True}

# uvicorn main:app --reload