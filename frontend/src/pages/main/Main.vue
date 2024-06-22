<script setup>
import { deleteEquipmentAPI, fetchEquipmentsAPI } from '@/api/Equipment';
import { routerPush } from '@/router';
import { useEditEquipmentStore } from '@/store/EditEquipmentStore';
import { ref } from 'vue'

const equipments = ref([]);
const isLoading = ref(true);

const searchByKeys = { "Серийный номер": "serial_number", 'Описание': "description" };
const searchByValue = ref("");
const selectedSearchByKey = ref(Object.keys(searchByKeys)[0]);
const pagesCount = ref(0);
const pageNum = ref(1);

const fetchEquipments = async () => {
  const response = await fetchEquipmentsAPI(pageNum.value, searchByKeys[selectedSearchByKey.value], searchByValue.value);
  equipments.value = response.data.data.equipments;
  pagesCount.value = response.data.data.pages_count;
}

const deleteEquipment = async (id) => {
  await deleteEquipmentAPI(id);

  for (let i = 0;  i < equipments.value.length; ++i) {
    if (equipments.value[i].id == id) {
      equipments.value.splice(i, 1);
    }
  }
}

const goEditEquipment = (id, typeName, serialNumber, description) => {
  const store = useEditEquipmentStore()

  store.id = id;
  store.typeName = typeName;
  store.serialNumber = serialNumber;
  store.description = description;

  routerPush('edit-equipment');
}

</script>

<template>
  <v-sheet class="mt-5 ma-auto" width="80%">
    <v-form v-on:submit.prevent="fetchEquipments">
      <v-row>
        <v-text-field width="60%" label="Поиск" class="mr-3" v-model="searchByValue"></v-text-field>
        <v-select width="20%" :items="Object.keys(searchByKeys)" v-model="selectedSearchByKey"></v-select>
        <v-btn type="submit" size="55px" class="d-print-block ml-2">
          <v-icon>mdi-account-search</v-icon>
        </v-btn>
      </v-row>
    </v-form>
    <v-card class="mb-5" :title="item.type_name" :subtitle="item.serial_number" :text="item.description" v-for="item in equipments"
      :key="item.id">
      <v-card-actions>
        <v-btn @click="goEditEquipment(item.id, item.type_name, item.serial_number, item.description)">Отредактировать</v-btn>
        <v-btn color="red" @click="deleteEquipment(item.id)">Удалить</v-btn>
      </v-card-actions>
    </v-card>
    <v-pagination @click="fetchEquipments" v-model="pageNum" :length="pagesCount" v-if="pagesCount"></v-pagination>
  </v-sheet>
</template>