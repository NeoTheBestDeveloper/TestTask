import { defineStore } from 'pinia';

import { deleteEquipmentAPI, fetchEquipmentsAPI } from '@/api/Equipment';


export const useMainPageStore = defineStore('main-page', {
    state: () => ({
        // Хранит отображаемое оборудование
        equipments: [],

        // Настройки для пагинации оборудования
        pagesCount: 0,
        pageNumber: 1,

        // Состояние формы для поиска оборудования        
        searchByKey: "",
        searchByValue: "",
    }),

    actions: {
        async deleteEquipment(id) {
            await deleteEquipmentAPI(id);

            for (let i = 0; i < this.equipments.length; ++i) {
                if (this.equipments[i].id == id) {
                    this.equipments.splice(i, 1);
                }
            }
        },

        async fetchEquipments() {
            const response = await fetchEquipmentsAPI(this.pageNumber, this.searchByKey, this.searchByValue);
            this.equipments = response.data.equipments;
            this.pagesCount = response.data.pages_count;
        }

    },
})