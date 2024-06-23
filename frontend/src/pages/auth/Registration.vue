<script setup>
import { ref } from 'vue';

import { registerAPI } from '@/api/Auth';
import { routerPush } from '@/router';

const login = ref("");
const email = ref("");
const password = ref("");
const valid = ref(false);
const errorMsg = ref("");


const registerUser = async () =>  {
    try {
      await registerAPI(login.value, email.value, password.value);

      login.value = "";
      email.value = "";
      password.value = "";

      routerPush("login");
    } catch (error) {
      errorMsg.value = error.response.data.data.username;
    }
}

const loginRules = [
  v => !!v || 'Логин обязателен',
  v => (v && v.length <= 140) || 'Логин должен быть короче 140 символов',
  v => (v && v.length >= 3) || 'Логин должен быть длиной хотя бы 3 символа',
];

const emailRules = [
  v => !!v || 'Почта обязательна',
  v => /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()\\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(v) || "Невалидная почта",
];

const passwordRules = [
  v => !!v || 'Пароль обязателен',
  v => (v && v.length <= 255) || 'Пароль должен быть короче 256 символов',
  v => (v && v.length >= 8) || 'Пароль должен быть длиной хотя бы 8 символов',
];

</script>

<template>
<v-form v-model="valid" v-on:submit.prevent="registerUser" fluid class="fill-height d-flex" >
    <v-row align="center" justify="center">
      <v-sheet  ms="auto" width="20%">
        <v-text-field v-model="login" label="Логин" :rules="loginRules" :error-messages="errorMsg"></v-text-field>
        <v-text-field v-model="email" label="Почта" type="email" :rules="emailRules"></v-text-field>
        <v-text-field v-model="password" label="Пароль" type="password" :rules="passwordRules"></v-text-field>
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