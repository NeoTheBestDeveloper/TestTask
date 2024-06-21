<script setup>
import { loginAPI } from '@/api/Auth';
import { routerPush } from '@/router';
import { useAuthStore } from '@/store/AuthStore';
import { storeToRefs } from 'pinia';
import { ref } from 'vue';

const login = ref("");
const password = ref("");
const store = useAuthStore();
const { isAuthenticated } = storeToRefs(store);

const loginUser = async () => {
    try {
        const response = await loginAPI(login.value, password.value);

        login.value = "";
        password.value = "";

        isAuthenticated.value = true;
        routerPush("main");
    } catch (error) {
        console.log(error);
    }
}
</script>

<template>
<div class="register">
    <form v-on:submit.prevent="loginUser" class="register-form">
        <div>
            <label for="login">Логин</label>
            <input type="text" id="login" v-model="login">
        </div>
        <div>
            <label for="password">Пароль</label>
            <input type="password" id="password" v-model="password">
        </div>
        <div>
            <button type="submit">Войти</button>
        </div>
    </form>
</div>
</template>