<script setup>
import { fetchEquipmentsAPI } from '@/api/Equipment';
import { ref } from 'vue'

const equipments = ref([]);
const isLoading = ref(true);

const searchByCriteria = { "Серийный номер": "serial_number", 'Описание': "description", 'Тип оборудования': "type_id" };
const searchBy = ref("");
const selectedSearchByCriteria = ref(Object.keys(searchByCriteria)[0]);

const fetchEquipments = async () => {
  const response = await fetchEquipmentsAPI(1, searchByCriteria[selectedSearchByCriteria.value], searchBy.value);
  equipments.value = response.data.data;
}

</script>

<template>
  <v-sheet class="mt-5 ma-auto" width="80%">
    <v-form v-on:submit.prevent="fetchEquipments">
      <v-row>
        <v-text-field width="60%" label="Поиск" class="mr-3" v-model="searchBy"></v-text-field>
        <v-select width="20%" :items="Object.keys(searchByCriteria)" v-model="selectedSearchByCriteria"></v-select>
        <v-btn type="submit" size="55px" class="d-print-block ml-2">
          <v-icon>mdi-account-search</v-icon>
        </v-btn>
      </v-row>
    </v-form>
    <v-card class="mb-5" :title="" :subtitle="item.serial_number" :text="item.description" v-for="item in equipments"
      :key="item.id">
      <v-card-actions>
        <v-btn>Отредактировать</v-btn>
      </v-card-actions>
    </v-card>
  </v-sheet>
</template>