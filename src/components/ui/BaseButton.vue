<template>
    <button v-if="!link" :class="buttonClass">
        <slot></slot>
    </button>
    <router-link v-else :to="to" :class="buttonClass">
        <slot></slot>
    </router-link>
</template>

<script lang="ts">
export default {
    props: {
        mode: {
            type: String,
            required: false,
            default: null
        },
        link: {
            type: Boolean,
            required: false,
            default: false
        },
        to: {
            type: String,
            required: false,
            default: '/'
        }
    },
    computed: {
        buttonClass() {
            return {
                'inline-block no-underline px-6 py-3 mr-2 border border-solid cursor-pointer rounded-[30px] hover:border-[#270041]': true,
                'bg-[#3a0061] text-white border-[#3a0061] hover:bg-[#270041]': null == this.mode, //css覆蓋有時候會壞掉，把default獨立出來
                'bg-transparent text-[#3a0061] border-none hover:bg-[#edd2ff] active:bg-[#edd2ff]': 'flat' == this.mode,
                'bg-transparent text-[#270041] border-[#270041] hover:bg-[#edd2ff] active:bg-[#edd2ff]': 'outline' == this.mode
            }
        }
    }
}
</script>