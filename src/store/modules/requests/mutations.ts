export default {
    // addRequest(state:any, payload:Object) {
    //     state.requests.push(payload)
    // },
    setRequests(state:any, payload:Object[]) {
        state.requests = payload
    }
}