import type Coach from '../../../types/coach'

export default {
    listCoaches(state:any): Coach[] {
        return state.coaches
    },
    hasCoaches(state:any): Boolean {
        return state.coaches && state.coaches.length > 0
    },
    isCoach(_:any, getters:any, _2:any, rootGetters:any) {
        const coaches:Coach[] = getters.listCoaches;
        const userId:string = rootGetters.userId;
        return coaches.some(coach => coach.id === userId)
    },
    shouldUpdate(state:any) {
        if (!state.lastFetch) {
            return true
        };
        const currentTimestamp = new Date().getTime();
        return (currentTimestamp - state.lastFetch)/1000 > 60;
    }
}