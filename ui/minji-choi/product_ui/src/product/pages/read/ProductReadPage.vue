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
                            <v-textarea v-model="product.content" readonly label="상품상세설명" auto-grow/>
                        </v-col>
                    </v-row>
                    <v-row justify="end">
                        <v-col cols="auto">
                            <router-link :to="{ name: 'ProductModifyPage', params: {productId} }">
                                <v-btn color="primary">수정</v-btn>
                            </router-link>
                        </v-col>
                        <v-col cols="auto">
                            <v-btn color="error" @click="onDelete">삭제</v-btn>
                        </v-col>
                        <v-col cols="auto">
                            <router-link :to="{ name: 'ProductListPage' }">
                                <v-btn color="secondary">목록</v-btn>
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
        ...mapActions(productModule, ['requestProductToDjango', 'requestDeleteProductToDjango']),
        async onDelete () {
            console.log('삭제를 누르셨습니다!')
            alert('상품이 삭제되었습니다.');
            await this.requestDeleteProductToDjango(this.productId)
            await this.$router.push({ name : 'ProductListPage' })
        },
    },
    created () {
            this.requestProductToDjango(this.productId)
        },
}
</script>