<template>
    <v-container>
        <h2>상품 정보 상세 페이지</h2>
        <v-card v-if="product">
            <v-card-title>상품 정보</v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.productName" readonly label="상품명"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.productPrice" readonly label="가격"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-textarea v-model="product.productDescription" readonly label="상세내용" auto-grow/>
                        </v-col>
                    </v-row>
                    <v-row justify="end">
                        <v-col cols="auto">
                            <router-link :to="{ name: 'ProductModifyPage', params: { productId } }">
                                <v-btn color="primary">수정</v-btn>
                            </router-link>
                        </v-col>
                        <v-col cols="auto">
                            <v-btn color="error" @click="onDelete">삭제</v-btn>
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
        ...mapActions(boardModule, ['requestProductToDjango']),
    },
    created () {
        this.requestProductToDjango(this.boardId)
    },
}
</script>