from sqlalchemy import Uuid, Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid

from config.database_sqlite import Base

class Coaches(Base):
    __tablename__ = 'coachData'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    userId = Column(Uuid, ForeignKey('users.id'), nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    areas = relationship('CoachAreas', back_populates='coach', order_by='CoachAreas.sort.asc()')
    description = Column(String, default='No content')
    hourlyRate = Column(Integer, default=1)

class CoachAreas(Base):
    __tablename__ = 'coachAreas'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    coachId = Column(Uuid, ForeignKey('coachData.id'), nullable=False)
    areaName = Column(String, nullable=False)
    sort = Column(Integer)

    coach = relationship('Coaches', back_populates='areas')

class Requests(Base):
    __tablename__ = 'requests'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    coachId = Column(Uuid, ForeignKey('coachData.id'), nullable=False)
    userEmail = Column(String, nullable=False)
    message = Column(String, default='No content')

class Users(Base):
    __tablename__ = 'users'

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)