<template>
    <div class="base">
        <base-dialog :show="!!error" title="An error occurred!" @close="handleError">
            <p>{{ error }}</p>
        </base-dialog>
        <section>
            <base-card>
                <header class=" text-center">
                    <h2>Requests Received</h2>
                </header>
                <div v-if="isLoading">
                    <base-spinner></base-spinner>
                </div>
                <ul v-else-if="hasRequests" class=" list-none mx-auto my-8 p-0 max-w-[30rem]">
                    <request-item v-for="res in receivedRequests" :key="res.id" :email="res.userEmail" :message="res.message"></request-item>
                </ul>
                <h3 v-else class=" text-center">You haven't received any request yet!</h3>
            </base-card>
        </section>
    </div>
</template>

<script lang="ts">
import requestItem from '../../components/requests/requestItem.vue'

export default {
    components: { requestItem },
    data() {
        return {
            isLoading: false,
            error: null
        }
    },
    computed: {
        receivedRequests(): Object[] {
            return this.$store.getters['requests/listRequests']
        },
        hasRequests(): Boolean {
            return this.$store.getters['requests/hasRequests']
        }
    },
    created() {
        this.loadRequests()
    },
    methods: {
        async loadRequests() {
            this.isLoading = true;
            try {
                await this.$store.dispatch('requests/loadRequests');
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