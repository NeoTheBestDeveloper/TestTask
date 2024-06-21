import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
    const isAuthenticated = ref(false);
    const isAuthChecked = ref(false);

    return { isAuthenticated, isAuthChecked };
})