import axios from 'axios'

export default {
    async login(context:any, payload:Object) {
        return context.dispatch('auth', {
            ...payload,
            mode: 'login'
        })
    },
    async signup(context:any, payload:Object) {
        return context.dispatch('auth', {
            ...payload,
            mode: 'signup'
        })
    },
    async auth(context:any, payload:Object) {
        let url = 'http://localhost:8000/register'
        if (payload.mode == 'login') {
            url = 'http://localhost:8000/login'
        }

        const formData = new FormData();
        formData.append('username', payload.email);
        formData.append('password', payload.password);
        await axios.post(url, formData)
        .then(response => {
            const UserInfo = {
                token: response.data.accessToken,
                userId: response.data.user.userId,
                tokenExpiration: response.data.tokenExpiration
            };

            // localStorage
            localStorage.setItem('token', response.data.accessToken);
            localStorage.setItem('userId', response.data.user.userId);
            localStorage.setItem('tokenExpiration', response.data.tokenExpiration);
            // store
            context.commit('setUser', UserInfo);
        })
        .catch(error => {
            throw new Error(error.response.data.detail || 'Failed to authenticate.')
        })
    },
    tryLogin(context:any) {

        const token = localStorage.getItem('token');
        const userId = localStorage.getItem('userId');
        const tokenExpiration = localStorage.getItem('tokenExpiration');
        // token expired check and login
        if (token && userId &&tokenExpiration) {
            const tokenExpirationDate = new Date(tokenExpiration);
            const currentDate = new Date();
            if (tokenExpirationDate < currentDate) {
                // here only check token expired when loading page
                // should checking when sending request too
                context.dispatch('logout');
            } else {
                context.commit('setUser', {
                    token: token,
                    userId: userId,
                    tokenExpiration: null
                })
            }
        };
    },
    logout(context:any) {
        // localStorage
        localStorage.removeItem('token');
        localStorage.removeItem('userId');
        localStorage.removeItem('tokenExpiration');
        // store
        context.commit('setUser', {
            userId: null,
            token: null,
            tokenExpiration: null
        })
    }
}