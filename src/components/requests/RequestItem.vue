<template>
    <li class="mx-0 my-4 p-4 border border-solid border-[#ccc]">
        <div>
            <a :href="emailToUser" class="text-[#3d008d] font-bold hover:text-[#8d007a] active:text-[#8d007a]">{{ email }}</a>
        </div>
        <p class="mt-2 mb-0 mx-0">{{ message }}</p>
    </li>
</template>

<script lang="ts">
export default {
    props: ['email', 'message'],
    computed: {
        emailToUser(): String {
            return 'mailto:' + this.email
        }
    }
}
</script>