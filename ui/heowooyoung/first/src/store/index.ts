import { createStore } from 'vuex'

import boardModule from "@/board/store/boardModule"
import productModule from "@/product/store/productModule"
import authenticationModule from "@/authentication/store/authenticationModule"
import accountModule from '@/account/store/accountModule'
import cartModule from "@/cart/store/cartModule";

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    boardModule,
    productModule,
    authenticationModule,
    accountModule,
    cartModule,
  }
})