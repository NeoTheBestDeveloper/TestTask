<script setup>

import { createEquipmentsAPI } from '@/api/Equipment';
import { fetchTypesAPI } from '@/api/EquipmentType';
import { ref } from 'vue'

const isLoading = ref(true);
const valid = ref(false);
const selectedType = ref("");
const serialNumbers = ref([ref("")]);
const serialNumbersErrors = ref([ref("")]);

const description = ref("");

let types = [];

const createEquipment = async () => {
  const selectedTypeIdx = types.findIndex(i => i.title == selectedType.value);
  const typeId = types[selectedTypeIdx].id;
  const sendData = [];

  serialNumbers.value.forEach((number) => {
    sendData.push(
      {
        type_id: typeId,
        description: description.value,
        serial_number: number.value,
      }
    );
  });

  try {
    await createEquipmentsAPI(sendData);
    description.value = "";
    serialNumbers.value = [ref("")];
    serialNumbersErrors.value = [ref("")];
    selectedType.value = "";
  } catch (error) {
    serialNumbers.value = [];
    serialNumbersErrors.value = [];
    for (const item of error.response.data.detail) {
      serialNumbers.value.push(ref(item.data.serial_number));
      serialNumbersErrors.value.push(ref(item.detail.non_field_errors[0]));
    }
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
  <v-form v-model="valid" v-on:submit.prevent="createEquipment" fluid class="fill-height d-flex" v-if="!isLoading">
    <v-row align="center" justify="center">
      <v-sheet  ms="auto" width="20%">
        <v-select v-model="selectedType" label="Тип оборудования" :items="types"></v-select>
        <v-list lines="one">
          <v-text-field label="Серийный номер" :key="i" v-for="(_, i) in serialNumbers" v-model="serialNumbers[i].value" :error-messages="serialNumbersErrors[i].value">
            <template v-slot:append>
              <v-icon color="red" @click="() => serialNumbers.splice(i, 1)">
                mdi-delete
              </v-icon>
            </template>
             </v-text-field>
        </v-list>
        <v-btn class="mb-4" @click="() => {
          serialNumbers.push(ref(''));
           serialNumbersErrors.push(ref(''));
           }">Добавить серийный номер</v-btn>
        <v-textarea v-model="description" label="Описание" hide-details required></v-textarea>
        <v-btn class="mt-2" type="submit" block>Добавить оборудование</v-btn>
      </v-sheet>
    </v-row>
  </v-form>
</template>