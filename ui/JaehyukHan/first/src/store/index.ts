import { createStore } from 'vuex'
import boardModule from "@/board/store/boardModule"
import productModule from '@/product/store/productModule'


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
    productModule
  }
})
