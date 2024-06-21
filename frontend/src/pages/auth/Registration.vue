<script setup>
import { ref } from 'vue';

import { registerAPI } from '@/api/Auth';
import { routerPush } from '@/router';

const login = ref("");
const email = ref("");
const password = ref("");

const registerUser = async () =>  {
    try {
        const response = await registerAPI(login.value, email.value, password.value);

        login.value = "";
        email.value = "";
        password.value = "";

        routerPush("login");
    } catch (error) {
        console.log(error);
    }
}
</script>

<template>
<div class="register">
    <form v-on:submit.prevent="registerUser" class="register-form">
        <div>
            <label for="login">Логин</label>
            <input type="text" id="login" v-model="login">
        </div>
        <div>
            <label for="email">Почта</label>
            <input type="email" id="email" v-model="email">
        </div>
        <div>
            <label for="password">Пароль</label>
            <input type="password" id="password" v-model="password">
        </div>
        <div>
            <button type="submit">Зарегистрироваться</button>
        </div>
    </form>
</div>
</template>