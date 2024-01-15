import axios from 'axios'

export default {
    async addRequestToCoach(context:any, payload:Object) {
        const newRequest = {
            // id: new Date().toISOString(),
            coachId: payload.coachId,
            userEmail: payload.email,
            message: payload.message
        };
        
        await axios.post('http://localhost:8000/request', newRequest)
        .then(response => console.log(response.data))
        .catch(error => console.log(error))
    },
    async loadRequests(context:any, payload:any) {
        const token = context.rootGetters.token;
        const config = {
            headers: { Authorization: `Bearer ${token}` }
        }
        await axios.get('http://localhost:8000/requests', config)
        .then(response => {
            context.commit('setRequests', response.data);
        })
        .catch(error => {
            throw new Error(error.response.data.detail || 'Failed to fetch requests.')
        })
    }
}