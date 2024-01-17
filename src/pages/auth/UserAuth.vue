<template>
  <div class="base">
    <base-dialog :show="!!error" title="An error occurred" @close="handleError">
      <p>{{ error }}</p>
    </base-dialog>
    <base-dialog :show="isLoading" fixed title="Authenticating...">
      <base-spinner></base-spinner>
    </base-dialog>
    <base-card>
      <form @submit.prevent="submitForm">
        <div class="mx-0 my-2">
          <label for="email" class="block font-bold mb-2">E-Mail</label>
          <input type="email" id="email" class="block w-full border border-solid border-[#ccc] focus:bg-[#f0e6fd] focus:outline-none focus:border-[#3d008d]" v-model.trim="email" @blur="clearValidity">
        </div>
        <div class="mx-0 my-2">
          <label for="password" class="block font-bold mb-2">Password</label>
          <input type="password" id="password" class="block w-full border border-solid border-[#ccc] focus:bg-[#f0e6fd] focus:outline-none focus:border-[#3d008d]" v-model.trim="password" @blur="clearValidity">
        </div>
        <p v-if="!formIsValid" class="mt-1 text-red-600 text-sm">{{ errorMessage }}</p>
        <base-button>{{ loginButton }}</base-button>
        <base-button type="button" mode="flat" @click="switchAuthMode">{{ switchAuthButton }}</base-button>
      </form>
    </base-card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
const route = useRoute();
const router = useRouter();
import { useStore } from 'vuex';
const store = useStore();

const isLoading = ref(false);
const errorMessage = ref('');
const error = ref(null);
const handleError = () => {
  error.value = null
};

const email = ref('');
const password = ref('');
const formIsValid = ref(true);
const submitForm = async () => {
  formIsValid.value = true;
  if (email.value === '' || !email.value.includes('@')) {
    formIsValid.value = false;
    errorMessage.value = 'wrong email address.';
    return
  } else if (password.value.length <6) {
    formIsValid.value = false;
    errorMessage.value = 'password must longer than 6 characters.';
    return
  };

  isLoading.value = true;
  try {
    if (loginMode.value) {
      await store.dispatch('login', {
        email: email.value,
        password: password.value
      })
    } else {
      await store.dispatch('signup', {
        email: email.value,
        password: password.value
      })
    };
    const redirectUrl = '/' + (route.query.redirect || 'coaches')
    router.replace(redirectUrl);
  } catch (getError:Error) {
    error.value = getError.message || 'Failed to authenticate, try later.'
  };

  isLoading.value = false;
};
const clearValidity = () => {
  formIsValid.value = true
};
const switchAuthMode = () => {
  loginMode.value = !loginMode.value
};

const loginMode = ref(true);
const loginButton = computed(() => {
  if (loginMode.value) {
    return 'Login'
  } else {
    return 'Signup'
  }
});
const switchAuthButton = computed(() => {
  if (!loginMode.value) {
    return 'Login instead'
  } else {
    return 'Signup instead'
  }
});
</script>
<!-- <script lang="ts">
export default {
  data() {
    return {
      email: '',
      password: '',
      formIsValid: true,
      loginMode: true,
      errorMessage: null,
      isLoading: false,
      error: null
    }
  },
  computed: {
    loginButton() {
      if (this.loginMode) {
        return 'Login'
      } else {
        return 'Signup'
      }
    },
    switchAuthButton() {
      if (!this.loginMode) {
        return 'Login instrad'
      } else {
        return 'Signup instead'
      }
    }
  },
  methods: {
    async submitForm() {
      this.formIsValid = true;
      if (this.email === '' || !this.email.includes('@')) {
        this.formIsValid = false;
        this.errorMessage = 'wrong email address.';
        return
      } else if (this.password.length <6) {
        this.formIsValid = false;
        this.errorMessage = 'password must longer than 6 characters.';
        return
      };
      
      this.isLoading = true;
      try {
        if (this.loginMode) {
          await this.$store.dispatch('login', {
            email: this.email,
            password: this.password
          })
        } else {
          await this.$store.dispatch('signup', {
            email: this.email,
            password: this.password
          })
        };
        const redirectUrl = '/' + (this.$route.query.redirect || 'coaches')
        this.$router.replace(redirectUrl);
      } catch (error: Error) {
        this.error = error.message || 'Failed to authenticate, try later.'
      }
      
      this.isLoading = false;
    },
    clearValidity() {
      this.formIsValid = true
    },
    switchAuthMode() {
      this.loginMode = !this.loginMode
    },
    handleError() {
      this.error = null
    }
  }
}
</script> -->