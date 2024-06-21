<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <h1>Добавить запись</h1>
  <button @click="count++">You clicked me {{ count }} times.</button>
</template>