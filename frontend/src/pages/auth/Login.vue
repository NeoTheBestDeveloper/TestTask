<script setup>
import { loginAPI } from '@/api/Auth';
import { routerPush } from '@/router';
import { useAuthStore } from '@/store/AuthStore';
import { storeToRefs } from 'pinia';
import { ref } from 'vue';

const login = ref("");
const password = ref("");
const valid = ref(false);

const store = useAuthStore();
const { isAuthenticated } = storeToRefs(store);

const loginUser = async () => {
    try {
        await loginAPI(login.value, password.value);

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
  <v-form v-model="valid" v-on:submit.prevent="loginUser" fluid class="fill-height d-flex" >
    <v-row align="center" justify="center">
      <v-sheet  ms="auto" width="20%">
        <v-text-field v-model="login" label="Логин" hide-details required ></v-text-field>
        <v-text-field v-model="password" label="Пароль" type="password" hide-details required></v-text-field>
        <v-btn class="mt-2" type="submit" block>Войти</v-btn>
        <RouterLink class="blue-link" to="/register">Нет аккаунта? Зарегистрироваться</RouterLink>
      </v-sheet>
    </v-row>
  </v-form>
</template>