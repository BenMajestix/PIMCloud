import { createRouter, createWebHistory } from 'vue-router'
import MailView from '../views/MailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/mail',
      name: 'mail',
      component: MailView,
    },
  ],
})

export default router
