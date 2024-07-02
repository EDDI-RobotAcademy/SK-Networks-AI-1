<template lang="">
    <v-container>
        <h2>판매 상품 리스트</h2>
        <div style="text-align: left; margin: 15px;">
            <router-link :to="{ name: 'ProductRegisterPage' }">
                상품등록
            </router-link>
        </div>
            <v-row v-if="products.length > 0">
                <v-col v-for="(product, index) in products" :key=index cols="12" sm="6" md="4" lg="3">
                <v-card @click="goToProductReadPage(product.productId)">
                    <v-img :src="getImageUrl(product.productImage)" aspect-ratio="1" class="grey lighten-2">
                        <template v-slot:placeholder>
                            <v-row class="fill-height ma-0" align="center" justify="center">
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
                <!-- Bootstrap 등에서 기본적으로 화면을 12개의 열로 구성함(전체 쓰겠단 소리) -->
                <v-col cols="12" class="text-center">
                    <v-alert type="info">등록된 상품이 없습니다!</v-alert>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" class="text-center">
                    <v-img src='@/assets/images/fixed/fiximg.jpg' aspect-ratio="1" color="grey lighten-2">
                    <template v-slot:placeholder>
                            <v-row class="fill-height ma-0" align="center" justify="center">
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
        ...mapState(productModule, ['products']),
        pagedItems () {
            const startIdx = (this.pagination.page - 1) * this.perPage
            const endIdx = startIdx + this.perPage
            return this.products.slice(startIdx, endIdx)
        }
    },
    mounted () {
        this.requestProductListToDjango()
    },
    methods: {
        ...mapActions(productModule, ['requestProductListToDjango']),

        getImageUrl (imageName) {
            return require(`@/assets/images/uploadimages/${imageName}`)
        },
         goToProductReadPage (productId) {
            this.$router.push({
                name: 'ProductReadPage',
                params: { productId: productId }
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
                    key: 'productId',
                },
                { title: '상품명', align: 'end', key: 'productName' },
                { title: '상품가격(원)', align: 'end', key: 'productPrice' },
                { title: '판매자', align: 'end', key: 'writer' },
            ],
            perPage: 5,
            pagination: {
                page: 1,
            }
        }
    }
}
</script>