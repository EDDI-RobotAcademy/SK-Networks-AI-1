<template>
    <v-container>
        <h2>상품 정보 수정</h2>
        <v-card v-if="product">
            <v-card-title>상품 상세 정보</v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="productName" label="상품명"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="productPrice" label="상품가격"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.writer" readonly label="상품등록자"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                                <v-select
                                v-model="productCategory"
                                :items="categories"
                                label="상품 카테고리"
                                clearable
                                solo/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-textarea v-model="content" label="상품상세설명" auto-grow/>
                        </v-col>
                    </v-row>
                    <v-row justify="end">
                        <v-col cols="auto">
                            <v-btn color="primary" @click="onModify">수정 완료</v-btn>
                        </v-col>
                        <v-col cols="auto">
                            <router-link :to="{ name: 'ProductReadPage' }"> <!-- 수정상태에서 다시 돌아가는 것 "Read" 페이지로 -->
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
    data () {
        return {
            productName: '',
            productPrice: '',
            writer: '',
            productCategory: '',
            content: '',
        }
    },
    computed: {
        ...mapState(productModule, ['product'])
    },
    methods: {
        ...mapActions(productModule, ['requestProductToDjango', 'requestModifyProductToDjango', 'requestDeleteProductToDjango']),
        async onModify () {
            console.log('수정 완료 누름')
            const payload = {
                productName: this.productName, // 해당 title을 써야 수정된 title. writer는 수정 없으므로 생략
                productPrice: this.productPrice,
                productCategory: this.productCategory,
                content : this.content,
                productId : this.productId,
            }
            await this.requestModifyProductToDjango(payload)
            alert('수정이 완료되었습니다.');
            await this.$router.push({ name : 'ProductReadPage', params: { productId: this.productId} })
        },
        async onDelete () {
            console.log('삭제를 누르셨습니다!')
            alert('상품이 삭제되었습니다.');
            await this.requestDeleteProductToDjango(this.productId)
            await this.$router.push({ name : 'ProductListPage' })
        },
    },
    created () {
        this.requestProductToDjango(this.productId).then(() => {
            this.productName = this.product.productName
            this.productPrice = this.product.productPrice
            this.productCategory = this.product.productCategory
            this.writer = this.product.writer
            this.content = this.product.content
        })
    },
}
</script>