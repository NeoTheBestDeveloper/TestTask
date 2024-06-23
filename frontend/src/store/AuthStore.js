import { checkMeAuthAPI } from '@/api/Auth'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        isAuthChecked: false,
        isAuthenticated: false,
    }),
    actions: {
        async checkAuth() {
            if (!this.isAuthChecked) {
                this.isAuthenticated = await checkMeAuthAPI();
            }
            this.isAuthChecked = true;
        }
    }
})