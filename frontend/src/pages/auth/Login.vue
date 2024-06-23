<script setup>
import { ref } from 'vue';

import { loginAPI } from '@/api/Auth';
import { routerPush } from '@/router';
import { useAuthStore } from '@/store/AuthStore';

const login = ref("");
const password = ref("");
const errorMsg = ref("");
const valid = ref(false);

const store = useAuthStore();

const loginUser = async () => {
  if (!valid.value) {
    return;
  }
  try {
      await loginAPI(login.value, password.value);
      login.value = "";
      password.value = "";

      store.isAuthenticated = true;
      routerPush("main");
  } catch (error) {
    errorMsg.value = error.response.data.detail;
  }
}

const loginRules = [
  v => !!v || 'Логин обязателен',
  v => (v && v.length <= 150) || 'Логин должен быть короче 150 символов',
  v => (v && v.length >= 3) || 'Логин должен быть длиной хотя бы 3 символа',
];

const passwordRules = [
  v => !!v || 'Пароль обязателен',
  v => (v && v.length <= 255) || 'Пароль должен быть короче 256 символов',
  v => (v && v.length >= 8) || 'Пароль должен быть длиной хотя бы 8 символов',
];
</script>

<template>
  <v-form v-model="valid" v-on:submit.prevent="loginUser" fluid class="fill-height d-flex" >
    <v-row align="center" justify="center">
      <v-sheet  ms="auto" width="20%">
        <v-text-field v-model="login" label="Логин" :rules="loginRules" :error-messages="errorMsg"></v-text-field>
        <v-text-field v-model="password" label="Пароль" type="password" :rules="passwordRules" :error-messages="errorMsg"></v-text-field>
        <v-btn class="mt-2" type="submit" block>Войти</v-btn>
        <RouterLink class="blue-link" to="/register">Нет аккаунта? Зарегистрироваться</RouterLink>
      </v-sheet>
    </v-row>
  </v-form>
</template>