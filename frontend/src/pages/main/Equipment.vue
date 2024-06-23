<script setup>
import { routerPush } from '@/router';
import { useEditEquipmentStore } from '@/store/EditEquipmentStore';
import { useMainPageStore } from '@/store/MaingPageStore';

defineProps({
  equipment: Object,
});

const store = useMainPageStore();

const goEditEquipment = (equipment) => {
  const editPageStore = useEditEquipmentStore()
  editPageStore.setEquipment(equipment);
  routerPush('edit-equipment');
};

</script>

<template> 
    <v-card class="mb-5" :title="equipment.type_name" :subtitle="equipment.serial_number" :text="equipment.description">
      <v-card-actions>
        <v-btn @click="goEditEquipment(equipment)">Редактировать</v-btn>
        <v-btn color="red" @click="store.deleteEquipment(equipment.id)">Удалить</v-btn>
      </v-card-actions>
    </v-card>
</template>