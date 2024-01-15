export default {
    setUser(state:any, payload:Object) {
        state.token = payload.token;
        state.userId = payload.userId;
        state.tokenExpiration = payload.tokenExpiration;
    }
}