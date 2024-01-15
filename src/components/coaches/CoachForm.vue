<template>
    <form @submit.prevent="submitForm">
        <div class="mx-0 my-2">
            <label class="after:content-['*'] after:ml-0.5 after:text-red-500 block font-bold mb-2" for="firstname">Firstname</label>
            <input ref="firstNameInput" class="peer block w-full border border-solid border-[#ccc] focus:bg-[#f0e6fd] focus:outline-none focus:border-[#3d008d]" :class="{' border border-solid border-red-600': !firstName.isValid}" type="text" id="firstname" v-model.trim="firstName.val" @blur="clearValidity('firstName')">
            <p v-if="!firstName.isValid" class="mt-1 text-red-600 text-sm">Content must not be empty.</p>
        </div>
        <div class="mx-0 my-2">
            <label class="after:content-['*'] after:ml-0.5 after:text-red-500 block font-bold mb-2" for="lastname">Lastname</label>
            <input ref="lastNameInput" class="peer block w-full border border-solid border-[#ccc] focus:bg-[#f0e6fd] focus:outline-none focus:border-[#3d008d]" :class="{' border border-solid border-red-600': !lastName.isValid}" type="text" id="lastname" v-model.trim="lastName.val" @blur="clearValidity('lastName')">
            <p v-if="!lastName.isValid" class="mt-1 text-red-600 text-sm">Content must not be empty.</p>
        </div>
        <div class="mx-0 my-2">
            <label class="after:content-['*'] after:ml-0.5 after:text-red-500 block font-bold mb-2" for="description">Description</label>
            <textarea ref="descriptionInput" class="peer block w-full border border-solid border-[#ccc] focus:bg-[#f0e6fd] focus:outline-none focus:border-[#3d008d]" :class="{' border border-solid border-red-600': !description.isValid}" id="description" cols="30" rows="5" v-model.trim="description.val" @blur="clearValidity('description')"></textarea>
            <p v-if="!description.isValid" class="mt-1 text-red-600 text-sm">Content must not be empty.</p>
        </div>
        <div class="mx-0 my-2">
            <label class="after:content-['*'] after:ml-0.5 after:text-red-500 block font-bold mb-2" for="rate">Hourly Rate</label>
            <input ref="rateInput" class="peer block w-full border border-solid border-[#ccc] focus:bg-[#f0e6fd] focus:outline-none focus:border-[#3d008d]" :class="{' border border-solid border-red-600': !rate.isValid}" type="number" id="rate" min="0" v-model.number="rate.val" @blur="clearValidity('rate')">
            <p v-if="!rate.isValid" class="mt-1 text-red-600 text-sm">Rate must be greater than 0.</p>
        </div>
        <div class="mx-0 my-2">
            <h3 class="after:content-['*'] after:ml-0.5 after:text-red-500 font-bold text-base mx-0 my-2">Areas of Expertise</h3>
            <div>
                <input ref="areasInput" class="peer inline font-normal my-0 ml-0 mr-2 w-auto border-none focus:outline-[#3d008d] focus:outline focus:outline-1" type="checkbox" id="frontend" value="frontend" v-model="areas.val" @blur="clearValidity('areas')">
                <label class=" inline font-normal my-0 ml-0 mr-2" :class="{'text-red-600': !areas.isValid}" for="frontend">Frontend Development</label>
            </div>
            <div>
                <input class="  inline font-normal my-0 ml-0 mr-2 w-auto border-none focus:outline-[#3d008d] focus:outline focus:outline-1 invalid:outline invalid:outline-2 invalid:outline-red-600" type="checkbox" id="backend" value="backend" v-model="areas.val" @blur="clearValidity('areas')">
                <label class=" inline font-normal my-0 ml-0 mr-2" :class="{'text-red-600': !areas.isValid}" for="backend">Backend Development</label>
            </div>
            <div>
                <input class=" inline font-normal my-0 ml-0 mr-2 w-auto border-none focus:outline-[#3d008d] focus:outline focus:outline-1 invalid:outline invalid:outline-2 invalid:outline-red-600" type="checkbox" id="career" value="career" v-model="areas.val" @blur="clearValidity('areas')">
                <label class=" inline font-normal my-0 ml-0 mr-2" :class="{'text-red-600': !areas.isValid}" for="career">Career Advisory</label>
            </div>
            <p v-if="!areas.isValid" class="mt-1 text-red-600 text-sm">Must choose at least one area.</p>
        </div>
        <base-button>Register</base-button>
    </form>
</template>

<script lang="ts">
export default {
    emits: ['save-data'],
    data() {
        return {
            firstName: {
                val: "",
                isValid: true
            },
            lastName: {
                val: "",
                isValid: true
            },
            description: {
                val: "",
                isValid: true
            },
            rate: {
                val: null,
                isValid: true
            },
            areas: {
                val: [],
                isValid: true
            },
            formIsValid: true
        }
    },
    methods: {
        submitForm() {
            this.validateInput();
            if (!this.formIsValid) {
                return
            }

            const formData = {
                first: this.firstName.val,
                last: this.lastName.val,
                desc: this.description.val,
                rate: this.rate.val,
                areas: this.areas.val
            };
            this.$emit('save-data', formData);
        },
        validateInput() {
            this.formIsValid = true;
            // firstName
            if (this.firstName.val =='') {
                this.firstName.isValid = false;
                this.formIsValid = false;
            }
            // lastName
            if (this.lastName.val =='') {
                this.lastName.isValid = false;
                this.formIsValid = false;
            }
            // description
            if (this.description.val =='') {
                this.description.isValid = false;
                this.formIsValid = false;
            }
            // rate
            if (!this.rate.val && this.rate.val <0) {
                this.rate.isValid = false;
                this.formIsValid = false;
            }
            // areas
            if (this.areas.val.length ===0) {
                this.areas.isValid = false;
                this.formIsValid = false;
            }
        },
        clearValidity(input) {
            this[input].isValid = true
        }
    }
}
</script>