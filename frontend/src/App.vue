<script setup>

import {RouterView} from 'vue-router'
import Navigation from '@/components/Navigation.vue'
import { useAuthStore } from './store/AuthStore';
import { storeToRefs } from 'pinia';

const store = useAuthStore();
const { isAuthenticated } = storeToRefs(store);

</script>

<template>
  <v-app>
    <Navigation v-if="isAuthenticated"/>
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>