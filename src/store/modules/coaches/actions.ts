import axios from 'axios'

export default {
    async addCoach(context:any, data:Object) {
        const coachData = {
            // id: new Date().toISOString(),
            // id: context.rootGetters.userId,
            // id would given by
            firstName: data.first,
            lastName: data.last,
            description: data.desc,
            hourlyRate: data.rate,
            areas: data.areas
        };

        const token = context.rootGetters.token;
        const config = {
            headers: { Authorization: `Bearer ${token}` }
        };
        await axios.post('http://localhost:8000/coach', coachData, config)
        .then(response => console.log(response.data))
        .catch(error => console.log(error))
    },
    async loadCoaches(context:any, payload:Object[]) {
        if (!payload.forceRefresh && !context.getters.shouldUpdate) {
            return
        };

        await axios.get('http://localhost:8000/coaches')
        .then(response => {
            context.commit('setCoaches', response.data);
            context.commit('setTimestamp');
        })
        .catch(error => {
            throw new Error(error.response.data.detail || 'Failed to fetch!')
        })
    }
}