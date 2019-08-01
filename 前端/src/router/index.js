import Vue from 'vue'
import Router from 'vue-router'
import index from '@/pages/index'
import content from '@/pages/content'
import contentList from '@/pages/contentList'
import order from '@/pages/order'
import personal from '@/pages/personal'
import shopping from '@/pages/shopping'
import Super from '@/pages/super'
import SuperOrder from '@/pages/SuperOrder'
import address from '@/pages/address'
import like from '@/pages/like'
import addorder from '@/pages/addorder'
import ordersuccess from '@/pages/ordersuccess'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: index
    },
    {
      path: '/content',
      component: content
    },
    {
      path: '/contentList',
      component: contentList
    },
    {
      path: '/order',
      component: order
    },
    {
      path: '/personal',
      component: personal
    },
    {
      path: '/shopping',
      component: shopping
    },
    {
      path: '/super',
      component: Super
    },
    {
      path:'/superOrder',
      component:SuperOrder
    },
    {
      path:'/address',
      component:address
    },
    {
      path:'/like',
      component:like
    },
    {
      path:'/addorder',
      component:addorder
    },
    {
      path:'/ordersuccess',
      component:ordersuccess

    },
  ]
})
