export default {
    // addCoach(state:any, payload:Object) {
    //     state.coaches.push(payload)
    // },
    setCoaches(state:any, payload:Object[]) {
        state.coaches = payload
    },
    setTimestamp(state:any) {
        state.lastFetch = new Date().getTime()
    }
}