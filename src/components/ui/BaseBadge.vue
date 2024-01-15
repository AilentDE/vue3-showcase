<template>
    <span :class="typeClass">{{ titleUpper }}</span>
</template>

<script lang="ts">
export default {
    props: {
        type: {
            type: String,
            required: false,
            default: null
        },
        title: {
            type: String,
            required: false,
            default: null
        }
    },
    computed: {
        typeClass() {
            return {
                'inline-block px-10 py-2 mr-2 mb-4 bg-[#ccc] text-[#252525] rounded-[30px]': true,
                'bg-indigo-800 text-white': 'frontend' == this.type,
                'bg-purple-800 text-white': 'backend' == this.type,
                'bg-pink-800 text-white': 'career' == this.type
            }
        },
        titleUpper() {
            return this.title.toUpperCase()
        }
    }
}
</script>