import { createRouter, createWebHistory } from 'vue-router'

// import CoachesList from '../pages/coaches/CoachesList.vue'
const CoachesList = () => import('../pages/coaches/CoachesList.vue')
// import CoachDetail from '../pages/coaches/CoachDetail.vue'
const CoachDetail = () => import('../pages/coaches/CoachDetail.vue')
// import CoachContact from '../pages/coaches/CoachContact.vue'
const CoachContact = () => import('../pages/coaches/CoachContact.vue')
// import CoachRegist from '../pages/coaches/CoachRegist.vue'
const CoachRegist = () => import('../pages/coaches/CoachRegist.vue')
// import Requests from '../pages/reques/RequestsList.vue'
const Requests = () => import('../pages/reques/RequestsList.vue')
// import UserAuth from '../pages/auth/UserAuth.vue'
const UserAuth = () => import('../pages/auth/UserAuth.vue')
// import NotFound from '../pages/NotFound.vue'
const NotFound = () => import('../pages/NotFound.vue')
import store from '../store/index'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: HomeView
    // },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // },
    {
      path: '/',
      redirect: '/coaches'
    },
    {
      path: '/coaches',
      component: CoachesList,
      children: []
    },
    {
      path: '/coaches/:id',
      component: CoachDetail,
      props: true,
      children: [
        {
          path: 'contact',
          component: CoachContact,
          children: []
        }
      ]
    },
    {
      path: '/register',
      component: CoachRegist,
      children: [],
      meta: { requiresAuth: true }
    },
    {
      path: '/requests',
      component: Requests,
      children: [],
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      component: UserAuth,
      children: [],
      meta: {requiresUnauth: true}
    },
    {
      path: '/:notFound(.*)',
      component: NotFound,
      children: []
    }
  ]
})

router.beforeEach( (to, from, next) => {
  if (to.meta.requiresAuth && !store.getters.isAuthenticated) {
    next('/login')
  } else if (to.meta.requiresUnauth && store.getters.isAuthenticated) {
    next('/coaches')
  } else {
    next()
  }
})

export default router
