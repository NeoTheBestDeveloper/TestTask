import { defineStore } from 'pinia';

export const useEditEquipmentStore = defineStore('edit-equipment', {
    state: () => ({
        // Свойства редактируемого оборудования
        id: 0,
        serialNumber: "",
        typeName: "",
        description: "",

        // Флаг, показывающий есть ли сейчас оборудование, которое нужно отредактировать. 
        hasEquipment: false,
    }),
    actions: {
        setEquipment(equipment) {
            this.id = equipment.id;
            this.serialNumber = equipment.serial_number;
            this.typeName = equipment.type_name;
            this.description = equipment.description;

            this.hasEquipment = true;
        },
    }
})