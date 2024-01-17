<template>
    <form @submit.prevent="submitForm" class=" p-4 m-4 border border-solid border-[#ccc] rounded-[12px]">
        <div class="mx-0 my-2">
            <label for="email" class=" block font-bold mb-2">Your Email</label>
            <input type="email" id="email" class=" p-[0.15rem] block w-full border border-solid border-[#ccc] focus:border-[#3d008d] focus:bg-[#faf6ff] focus:outline-none" v-model.trim="email">
        </div>
        <div class="mx-0 my-2">
            <label for="message" class=" block font-bold mb-2">Message</label>
            <textarea id="message" cols="30" rows="5" class=" p-[0.15rem] block w-full border border-solid border-[#ccc] focus:border-[#3d008d] focus:bg-[#faf6ff] focus:outline-none" v-model.trim="message"></textarea>
        </div>
        <p class=" font-bold text-red-600" v-if="!formIsValid">Please enter a valid email and non-empty message.</p>
        <div class=" text-center">
            <base-button>Send Message</base-button>
        </div>
    </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
const route = useRoute();
const router = useRouter();
import { useStore } from 'vuex';
const store = useStore();

const email = ref('');
const message = ref('');
const formIsValid = ref(true);

const submitForm = () => {
    formIsValid.value = true;
    if (!email.value.includes('@') || email.value == '' || message.value == '') {
        formIsValid.value = false;
        return
    };
    const data = {
        coachId: route.params.id,
        email: email.value,
        message: message.value
    };
    store.dispatch('requests/addRequestToCoach', data);
    router.replace('/coaches');
};
</script>
<!-- <script lang="ts">
export default {
    data() {
        return {
            email: '',
            message: '',
            formIsValid: true
        }
    },
    methods: {
        submitForm() {
            this.formIsValid = true;
            if (!this.email.includes('@') || this.email == '' || this.message == '') {
                this.formIsValid = false;
                return
            };
            const data = {
                coachId: this.$route.params.id,
                email: this.email,
                message: this.message
            };
            this.$store.dispatch('requests/addRequestToCoach', data);
            this.$router.replace('/coaches')
        }
    }
}
</script> -->