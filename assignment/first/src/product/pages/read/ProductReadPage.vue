<template>
    <v-container>
        <h2>상품 리스트</h2>
        <v-card v-if="product">
            <v-card-title>상품 정보</v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.product_name" readonly label="상품명"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.price" readonly label="가격"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-textarea v-model="product.product_description" readonly label="상세 정보" auto-grow/>
                        </v-col>
                    </v-row>
                    <v-row justify="end">
                        <v-col cols="auto">
                            <v-btn color="primary">수정</v-btn>
                        </v-col>
                        <v-col cols="auto">
                            <v-btn color="error">삭제</v-btn>
                        </v-col>
                        <v-col cols="auto">
                            <router-link :to="{ name: 'ProductListPage' }">
                                <v-btn color="secondary">돌아가기</v-btn>
                            </router-link>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex'

const productModule = 'productModule'

export default {
    // props : 다른 vue랑 데이터를 주고 받기 위해 사용함 
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
        // 'requestDeleteProductToDjango' 추후 처리 필요
        ...mapActions(productModule, ['requestProductToDjango']),
        async onDelete () {
            console.log('삭제를 누르셨습니다!')
        },
    },

    created () {
        this.requestProductToDjango(this.productId)
    },   
}
</script>