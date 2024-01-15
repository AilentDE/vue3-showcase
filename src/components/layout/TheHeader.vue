<template>
    <header class="flex w-full h-20 items-center justify-center bg-indigo-900">
        <nav class="w-11/12 m-auto flex justify-between items-center">
            <h1 class="m-0">
                <router-link to="/" class="inline-block px-6 py-3 m-0 text-white no-underline font-black">Find a Coach</router-link>
            </h1>
            <ul class="list-none m-0 p-0 flex justify-center items-center">
                <li class="mx-2 my-0">
                    <router-link to="/coaches" class="inline-block px-6 py-3 no-underline text-fuchsia-400">All Coaches</router-link>
                </li>
                <li class="mx-2 my-0">
                    <router-link to="/requests" v-if="isLoggedIn" class="inline-block px-6 py-3 no-underline text-fuchsia-400">Requests</router-link>
                    <router-link to="/login" v-else class="inline-block px-6 py-3 no-underline text-fuchsia-400">Login</router-link>
                </li>
                <li class="mx-2 my-0" v-if="isLoggedIn">
                    <base-button @click="logout">Logout</base-button>
                </li>
            </ul>
        </nav>
    </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    computed: {
        isLoggedIn():Boolean {
            return this.$store.getters.isAuthenticated
        }
    },
    methods: {
        logout() {
            this.$store.dispatch('logout');
            this.$router.replace('/coaches')
        }
    }
})
</script>

<style scoped>
a:active,
a:hover,
a.router-link-active {
  border: 1px solid #f391e3;
}

h1 a:hover,
h1 a:active,
h1 a.router-link-active {
  border-color: transparent;
}
</style>