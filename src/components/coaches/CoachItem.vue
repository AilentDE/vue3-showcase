<template>
    <li class="mx-0 my-4 border border-solid border-[#424242] rounded-xl p-4">
        <h3 class=" text-2xl">{{ fullName }}</h3>
        <h4 class=" mx-0 my-2">$ {{ rate }}/hour</h4>
        <div class=" mx-0 my-2">
            <base-badge v-for="area in areas" :key="area" :type="area" :title="area"></base-badge>
        </div>
        <div class=" mx-0 my-2 flex justify-end">
            <base-button mode="outline" link :to="coachContantLink">Contant</base-button>
            <base-button link :to="coachDetailLink">View Details</base-button>
        </div>
    </li>
</template>

<script lang="ts">
import BaseBadge from '../ui/BaseBadge.vue'
export default {
  components: { BaseBadge },
    props: ['id', 'firstName', 'lastName', 'rate', 'areas'],
    computed: {
        fullName() {
            return this.firstName + this.lastName
        },
        coachContantLink() {
            return this.$route.path + '/' + this.id + '/contact'
        },
        coachDetailLink() {
            return this.$route.path + '/' + this.id
        }
    }
}
</script>

<style scoped>

</style>