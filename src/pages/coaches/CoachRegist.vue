<template>
    <section>
        <base-card>
            <h2>Register as a coach now!</h2>
            <coach-form @save-data="saveData"></coach-form>
        </base-card>
    </section>
</template>

<script lang="ts">
import CoachForm from '../../components/coaches/CoachForm.vue'
export default {
    components: {
        CoachForm
    },
    methods: {
        saveData(data:Object) {
            this.$store.dispatch('coaches/addCoach', data);
            this.$router.replace('/coaches');
        }
    }
}
</script>