<script setup>

import EquipmentsList from './EquipmentsList.vue';
import SearchEquipmentsForm from './SearchEquipmentsForm.vue';

</script>

<template>
  <v-sheet class="mt-5 ma-auto" width="80%">
    <SearchEquipmentsForm />
    <EquipmentsList/>
  </v-sheet>
</template>