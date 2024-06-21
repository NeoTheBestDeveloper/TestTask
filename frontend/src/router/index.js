import { createRouter, createWebHistory } from 'vue-router'

import Main from '@/pages/main/Main.vue';
import Login from '@/pages/auth/Login.vue';
import Registration from '@/pages/auth/Registration.vue';
import Create from '@/pages/create/Create.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/register',
      name: 'register',
      component: Registration,
    },
    {
      path: '/create',
      name: 'create-equipment',
      component: Create,
    }

  ]
})

export const routerPush = (name) => {
  return router.push({ name });
}

export default router
