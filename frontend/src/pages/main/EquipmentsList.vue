<script setup>

import { useMainPageStore } from '@/store/MaingPageStore';
import Equipment from './Equipment.vue';

const store = useMainPageStore();

</script>


<template>
    <div>
        <Equipment :equipment="equipment" :key="equipment.id" v-for="equipment in store.equipments"/>
        <v-pagination @click="store.fetchEquipments" v-model="store.pageNumber" :length="store.pagesCount" v-if="store.pagesCount"></v-pagination>
    </div>
</template>