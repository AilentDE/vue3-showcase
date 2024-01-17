<template>
    <div class="base">
        <section>
            <base-card>
                <h2>{{ fullName }}</h2>
                <h3>${{ rate }}/hour</h3>
            </base-card>
        </section>
        <section>
            <base-card>
                <header>
                    <h2>Interested? Reach out now!</h2>
                    <base-button v-show="showContactButton" link :to="contactLink">Contact</base-button>
                </header>
                <router-view></router-view>
            </base-card>
        </section>
        <section>
            <base-card>
                <base-badge v-for="area in areas" :key="area" :type="area" :title="area"></base-badge>
                <p>{{ description }}</p>
            </base-card>
        </section>
    </div>
</template>

<script setup lang="ts">
import { reactive, computed, defineProps } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute();
import { useStore } from 'vuex';
const store = useStore();

const props = defineProps(['id']);

let selectedCoach = reactive({
    firstName: '',
    lastName: '',
    hourlyRate: null,
    areas: [],
    description: ''
});
const selectedCoachFunc = () => {
    selectedCoach = reactive(store.getters['coaches/listCoaches'].find(coach => coach.id === props.id))
};
selectedCoachFunc()
const fullName = computed(() =>
    selectedCoach.firstName + ' ' + selectedCoach.lastName
);
const rate = computed(() => 
    selectedCoach.hourlyRate
);
const contactLink = computed(() => 
    route.path + '/contact'
);
const showContactButton = computed(() =>
    !route.path.includes('/contact')
);
const areas = computed(() => 
    selectedCoach.areas
);
const description = computed(() =>
    selectedCoach.description
);
</script>
<!-- <script lang="ts">

export default {
    props: ['id'],
    data() {
        return {
            selectedCoach: null
        }
    },
    computed: {
        fullName() {
            return this.selectedCoach.firstName + ' ' + this.selectedCoach.lastName
        },
        rate() {
            return this.selectedCoach.hourlyRate
        },
        contactLink() {
            return this.$route.path + '/contact'
        },
        areas() {
            return this.selectedCoach.areas
        },
        description() {
            return this.selectedCoach.description
        }
    },
    created() {
        this.selectedCoach = this.$store.getters['coaches/listCoaches'].find(
            (coach) => coach.id === this.id    
        )
    }
}
</script> -->