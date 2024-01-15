export default {
    listRequests(state:any, getters:any, rootState:any, rootGetters:any): Object[] {
        const coachId:String = rootGetters.userId;
        return state.requests.filter(req => req.coachId === coachId)
    },
    hasRequests(state:any, getters:any): Boolean {
        return getters.listRequests && getters.listRequests.length >0
    }
}