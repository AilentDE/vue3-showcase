import mutations from './mutations'
import actions from './actions'
import getters from './getters'

export default {
    state() {
        return {
            myCoachId: "960b233b-a3b0-42fb-a55b-54a262fd890c",
            userId: null,
            token: null,
            tokenExpiration: null
        }
    },
    mutations,
    actions,
    getters
}