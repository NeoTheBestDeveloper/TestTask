<script setup>

import { ref } from 'vue';

import { useMainPageStore } from '@/store/MaingPageStore';

const store = useMainPageStore();

const searchByKeys = { "Серийный номер": "serial_number", 'Описание': "description" };
const selectedSearchByKey = ref(Object.keys(searchByKeys)[0]);
store.searchByKey = searchByKeys[selectedSearchByKey.value];


</script>

<template>
    <v-form v-on:submit.prevent="store.fetchEquipments">
      <v-row>
        <v-text-field width="60%" label="Поиск" class="mr-3" v-model="store.searchByValue"></v-text-field>
        <v-select width="20%" :items="Object.keys(searchByKeys)" :value="selectedSearchByKey" @update:modelValue="value => store.searchByKey = searchByKeys[value]">
        </v-select>
        <v-btn type="submit" size="55px" class="d-print-block ml-2">
          <v-icon>mdi-account-search</v-icon>
        </v-btn>
      </v-row>
    </v-form>
</template>