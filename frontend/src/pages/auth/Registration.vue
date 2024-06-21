<script setup>
import { ref } from 'vue';

import { registerAPI } from '@/api/Auth';
import { routerPush } from '@/router';

const login = ref("");
const email = ref("");
const password = ref("");
const valid = ref(false);

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
<v-form v-model="valid" v-on:submit.prevent="registerUser" fluid class="fill-height d-flex" >
    <v-row align="center" justify="center">
      <v-sheet  ms="auto" width="20%">
        <v-text-field v-model="login" label="Логин" hide-details required></v-text-field>
        <v-text-field v-model="email" label="Почта" hide-details required type="email"></v-text-field>
        <v-text-field v-model="password" label="Пароль" type="password" hide-details required></v-text-field>
        <v-btn class="mt-2" type="submit" block>Зарегистрироваться</v-btn>
        <RouterLink class="blue-link" to="/login">Уже есть аккаунт? Войти</RouterLink>
      </v-sheet>
    </v-row>
</v-form>
</template>

<style>
.blue-link {
  color: blue;
}
</style>