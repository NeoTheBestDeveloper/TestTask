<script setup>
import { editEquipmentAPI } from '@/api/Equipment';
import { fetchTypesAPI } from '@/api/EquipmentType';
import { routerPush } from '@/router';
import { useEditEquipmentStore } from '@/store/EditEquipmentStore';
import { storeToRefs } from 'pinia';
import { ref } from 'vue';

const store = useEditEquipmentStore();
const {id, serialNumber, typeName, description, hasEquipment} = storeToRefs(store);
const valid = ref(false);

const isLoading = ref(true);
const errMsg = ref("");
let types = [];

const editEquipment = async () => {
    const type = types[types.findIndex((i) => i.title == typeName.value)];
    try {
      await editEquipmentAPI(id.value, serialNumber.value, type.id, description.value)
      store.$reset();
      routerPush('main');
    } catch (error) {
      errMsg.value = error.response.data.data.non_field_errors[0];
    }

}

const fetchTypes = () => {
    fetchTypesAPI().then((data) => {
        types = data;
        isLoading.value = false;
    });
}

fetchTypes();
</script>

<template>
  <v-form v-model="valid" v-on:submit.prevent="editEquipment" fluid class="fill-height d-flex" v-if="!isLoading && hasEquipment">
    <v-row align="center" justify="center">
      <v-sheet  ms="auto" width="20%">
        <v-select v-model="typeName" label="Тип оборудования" :items="types"></v-select>
        <v-text-field v-model="serialNumber" label="Серийный номер" :error-messages="errMsg"></v-text-field>
        <v-textarea v-model="description" label="Описание" hide-details required></v-textarea>
        <v-btn class="mt-2" type="submit" block>Сохранить</v-btn>
      </v-sheet>
    </v-row>
  </v-form>
  <div v-else-if="!hasEquipment">Выберите оборудование для редактирования на главной старнице</div>
</template>