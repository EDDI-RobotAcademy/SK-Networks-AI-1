<template>
    <v-container>
        <h2>상품 상세 정보 조회</h2>
        <v-card v-if="product">
            <v-card-title>상품 상세 정보</v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.prodname" readonly label="상품명"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.price" readonly label="상품가격"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.writer" readonly label="상품등록자"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.content" readonly label="상품 상세 설명"/>
                        </v-col>
                    </v-row>
    
                    <v-row>
                        <v-col cols="12">
                            <v-img :src="getProductImageUrl(product.productImage)" aspect-ratio="1" color="grey lighten-2">
                                <template v-slot:placeholder>
                                    <v-row class="fill-height ma-0" align="center" justify="center">
                                        <v-progress-circular indeterminate color="grey lighten-5"/>
                                    </v-row>
                                </template> 
                            </v-img>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card-text>
        </v-card> 
        
        <v-alert v-else type="info">현재 등록된 상품이 없습니다!</v-alert>
        <div class="button-container">
            <v-btn color="primary" @click="onPurchase" class="action-button">
                <v-icon>mdi-cart</v-icon>
                <span class="button-text">구매하기</span>
            </v-btn>
            <router-link :to="{ name: 'ProductListPage' }" 
                            class="router-link no-underline">
                <v-btn color="secondary" class="action-button">
                    <v-icon>mdi-arrow-left</v-icon>
                    <span class="button-text">목록</span>
                </v-btn>
            </router-link>
        </div>
    </v-container>
</template>


<script>
import { mapActions, mapState } from 'vuex'

const productModule = 'productModule'

export default {
    props: {
        productId: {
            type: String,
            required: true,
        }
    },
    computed: {
        ...mapState(productModule, ['product'])
    },
    methods: {
        ...mapActions(productModule, ['requestProductToDjango']),
        getProductImageUrl (imageName) {
            return require(`@/assets/images/uploadimages/${imageName}`)
        },
        async onPurchase () {
            console.log('구매하기 버튼 눌렀음')
        },

    },
    created () {
            this.requestProductToDjango(this.productId)
        },
}
</script>