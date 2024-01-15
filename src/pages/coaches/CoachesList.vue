<template>
  <div class="base">
    <base-dialog :show="!!error" title="An error occurred!" @close="handleError">
      <p>{{ error }}</p>
    </base-dialog>
    <base-card>
      <section>
        <coach-filter @change-filter="setFilters"></coach-filter>
      </section>
    </base-card>
    <base-card>
      <section>
        <div class="flex justify-between">
          <base-button mode="outline" @click="loadCoaches(true)">Refresh</base-button>
          <div class="asCoach">
            <base-button link to="/login" v-if="!isLoggedIn && !isLoading">Login</base-button>
            <base-button link to="/register" v-if="isLoggedIn && !isCoach && !isLoading">Register as Coach</base-button>
            <base-button link to="/login?redirect=register" v-else-if="!isLoggedIn && !isCoach && !isLoading">Login and Register as Coach</base-button>
          </div>
        </div>
        <div v-if="isLoading">
          <base-spinner></base-spinner>
        </div>
        <ul v-else-if="hasCoaches" class="marker:text-sky-400 list-none m-0 p-0 space-y-3 text-slate-400">
          <coach-iteam
            v-for="coach in filteredCoaches"
            :key="coach.id"
            :id="coach.id"
            :firstName="coach.firstName"
            :lastName="coach.lastName"
            :rate="coach.hourlyRate"
            :areas="coach.areas"
          ></coach-iteam>
        </ul>
        <h3 v-else>No coaches found.</h3>
      </section>
    </base-card>
  </div>
</template>

<script lang="ts">
import CoachIteam from '../../components/coaches/CoachItem.vue'
import CoachFilter from '../../components/coaches/CoachFilter.vue'
import type Coach from '../../types/coach'
export default {
  components: {
    CoachIteam,
    CoachFilter
  },
  data() {
    return {
      isLoading: false,
      error: null,
      activeFilters: {
        frontend: true,
        backend: true,
        career: true
      }
    }
  },
  computed: {
    isLoggedIn(): Boolean {
      return this.$store.getters.isAuthenticated
    },
    filteredCoaches(): Coach[] {
      const coaches =  this.$store.getters['coaches/listCoaches'];
      return coaches.filter(coach => {
        if (this.activeFilters.frontend && coach.areas.includes('frontend')) {
          return true
        };
        if (this.activeFilters.backend && coach.areas.includes('backend')) {
          return true
        };
        if (this.activeFilters.career && coach.areas.includes('career')) {
          return true
        };
        return false
      })
    },
    hasCoaches(): Boolean {
      return !this.isLoading && this.$store.getters['coaches/hasCoaches']
    },
    isCoach() : Boolean {
      return this.$store.getters['coaches/isCoach']
    }
  },
  created() {
    this.loadCoaches()
  },
  methods: {
    setFilters(updatedFilters:Object) {
      this.activeFilters = updatedFilters
    },
    async loadCoaches(refresh:Boolean = false) {
      this.isLoading = true;
      try {
        await this.$store.dispatch('coaches/loadCoaches', {forceRefresh: refresh});
      } catch (error) {
        this.error = error.message || 'Something went wrong!';
      }
        this.isLoading = false;
    },
    handleError() {
      this.error = null
    }
  }
}
</script>