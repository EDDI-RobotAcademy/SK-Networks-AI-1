<template lang="">
  <v-container>
      <h2>Product 과제</h2>
      <div style="text-align: left; margin: 15px;">
          <router-link :to="{ name: 'ProductRegisterPage' }">
              상품 등록
          </router-link>
      </div>
    <v-row v-if="productList.length > 0">
        <v-col v-for="(product, index) in productList" :key=index sm="6">
            <v-card @click="goToProductReadPage(product.productId)">
                <!-- productimageName에서 productImage라는 field로 바꿔야함 -->
                <v-img :src="getImageUrl(product.productImage)" aspect-ratio="1" class="grey lighten-2">
                        <template v-slot:placeholder>
                            <v-row class="fill-height ma-0" align="center" justify="center">
                                <!-- 이미지 처리에 걸리는 시간 고려  -->
                                <v-progress-circular indeterminate color="grey lighten-5"/> 
                            </v-row>
                        </template>
                </v-img>
                <v-card-title>{{product.productName}}</v-card-title>
                <v-card-subtitle>{{product.productPrice}}</v-card-subtitle>
            </v-card>
        </v-col>
    </v-row>
    <v-row v-else>
        <v-col cols="12" class="text-center">
            <v-alert type="info">등록된 상품이 없습니다!</v-alert>
        </v-col>
    </v-row>
    <v-row>
        <v-col cols="12" class="text-center">
            <v-img src="@/assets/images/fixed/mario.png" aspect-ratio="1" class="grey lighten-2">
                <template v-slot:placeholder>
                    <v-row class="fill-height ma-0" align="center" justify="center">
                        <!-- 이미지 처리에 걸리는 시간 고려  -->
                        <v-progress-circular indeterminate color="grey lighten-5"/> 
                    </v-row>
                </template>
            </v-img>
        </v-col>
    </v-row>
  </v-container>
</template>

// npm install axios --legacy-peer-deps

<script>
// 이것은 vuex 때문에 사용 가능
import { mapActions, mapState } from 'vuex'

const productModule = 'productModule'

export default {
  components: {
      // RouterLink
  },
  computed: {
      ...mapState(productModule, ['boards']),
      pagedItems () {
          const startIdx = (this.pagination.page - 1) * this.perPage
          const endIdx = startIdx + this.perPage
          return this.boards.slice(startIdx, endIdx)
      }
  },
  mounted () {
      this.requestBoardListToDjango()
  },
  methods: {
      ...mapActions(boardModule, ['requestProductListToDjango']),
      getImageUrl(imageName) {
        return require('@/assets/images/uploadImages' + imageName)
      },
      goToProductReadPage (event, {item}){
        console.log('읽기 구현 할 때 사용')
      },
      readRow (event, { item }) { // 행단위로 읽기
          this.$router.push({ // list에 있는 행 누르면
              name: 'ProductReadPage', // 해당 게시물로 이동 (readpage)
              params: { productId: item['productId'].toString() } // route에서 props 설정을 햇기 때문에 params 설정이 가능한 것!
          })
      }
  },
  data () {
      return {
          headerTitle: [
              {
                  title: 'No',
                  align: 'start',
                  sortable: true,
                  key: 'boardId',
              },
              { title: '상품명', align: 'end', key: 'productName' },
              { title: '등록자', align: 'end', key: 'writer' },
              { title: '상품정보', align: 'end', key: 'productDescription' },
              { title: '상품가격', align: 'end', key: 'productPrice' },
          ],
          perPage: 5,
          pagination: {
              page: 1,
          }
      }
  }
}
</script>