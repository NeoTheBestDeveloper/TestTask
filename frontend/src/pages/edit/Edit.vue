<script setup>
import { editEquipmentAPI } from '@/api/Equipment';
import { fetchTypesAPI } from '@/api/EquipmentType';
import { useEditEquipmentStore } from '@/store/EditEquipmentStore';
import { storeToRefs } from 'pinia';
import { ref } from 'vue';

const store = useEditEquipmentStore();
const {id, serialNumber, typeName, description} = storeToRefs(store);
const valid = ref(false);

const isLoading = ref(true);
let types = [];

const editEquipment = async () => {
    console.log(types, typeName.value, types.findIndex((i) => i.title == typeName.value));
    const type = types[types.findIndex((i) => i.title == typeName.value)];
    await editEquipmentAPI(id.value, serialNumber.value, type.id, description.value)
}

const fetchTypes = () => {
  let fetchedData = [];

  fetchTypesAPI().then((data) => {
    fetchedData = data.data;

    fetchedData = fetchedData.flatMap((item) => {
      return {
        id: item.id,
        title: item.name,
        serial_number_mask: item.serial_number_mask,
      }
    })

    isLoading.value = false;
    types = fetchedData;
  });  
}

fetchTypes();
</script>

<template>
  <v-form v-model="valid" v-on:submit.prevent="editEquipment" fluid class="fill-height d-flex" v-if="!isLoading">
    <v-row align="center" justify="center">
      <v-sheet  ms="auto" width="20%">
        <v-select v-model="typeName" label="Тип оборудования" :items="types"></v-select>
        <v-text-field v-model="serialNumber" label="Серийный номер"></v-text-field>
        <v-textarea v-model="description" label="Описание" hide-details required></v-textarea>
        <v-btn class="mt-2" type="submit" block>Сохранить</v-btn>
      </v-sheet>
    </v-row>
  </v-form>
</template>