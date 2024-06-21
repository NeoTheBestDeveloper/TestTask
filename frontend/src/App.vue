<script setup>

import {RouterView} from 'vue-router'
import Navigation from '@/components/Navigation.vue'

</script>

<template>
  <v-app>
    <Navigation/>
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>