import { createRouter, createWebHistory } from 'vue-router'

import Main from '@/pages/main/Main.vue';
import Login from '@/pages/auth/Login.vue';
import Registration from '@/pages/auth/Registration.vue';
import Create from '@/pages/create/Create.vue';
import Edit from '@/pages/edit/Edit.vue';
import { useAuthStore } from '@/store/AuthStore';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main,
      meta: { requiresAuth: true },
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: { requiresAuth: false },
    },
    {
      path: '/register',
      name: 'register',
      component: Registration,
      meta: { requiresAuth: false },
    },
    {
      path: '/create',
      name: 'create-equipment',
      component: Create,
      meta: { requiresAuth: true },
    },
    {
      path: '/edit',
      name: 'edit-equipment',
      component: Edit,
      meta: { requiresAuth: true },
    }

  ]
})

router.beforeEach(async (to, _from) => {
  const store = useAuthStore();
  await store.checkAuth();

  if (!store.isAuthenticated && to.meta.requiresAuth) {
    return { name: 'login' };
  }
})

export const routerPush = (name) => {
  return router.push({ name });
}

export default router
