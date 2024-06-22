import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useEditEquipmentStore = defineStore('edit-equipment', () => {
    const id = ref(0);
    const serialNumber = ref("");
    const typeName = ref("");
    const description = ref("");

    return { id, serialNumber, typeName, description };
})