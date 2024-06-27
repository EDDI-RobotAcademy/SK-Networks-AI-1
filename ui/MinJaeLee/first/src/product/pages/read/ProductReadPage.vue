<template>
    <v-container>
        <h2>Vue3 + Vuetify3 + TypeScript 상품 세부 사항 보기</h2>
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
                            <v-text-field v-model="product.productDescription" readonly label="상품 설명"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="product.productPrice" readonly label="가격" type="number"/>
                        </v-col>
                    </v-row>
                    
                    <v-row>
                        <v-col cols="12">
                            <v-img :src="getProductImageUrl(product.productImage)" aspect-ratio="1" class="grey lighten-2">
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
            <v-btn color="success" @click="onAddToCart" class="action-button">
                <v-icon>mdi-cart-plus</v-icon>
                <span class="button-text">장바구니에 추가</span>
            </v-btn>
            <router-link :to="{ name: 'ProductListPage' }" 
                            class="router-link no-underline">
                <v-btn color="secondary" class="action-button">
                    <v-icon>mdi-arrow-left</v-icon>
                    <span class="button-text">목록으로 돌아가기</span>
                </v-btn>
            </router-link>
        </div>
    </v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex'

const productModule = 'productModule'
const cartModule = 'cartModule'

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
        ...mapActions(cartModule, ['requestAddCartToDjango']),
        async onPurchase () {
            console.log('구매하기 버튼 눌렀음')
        },
        async onAddToCart () {
            console.log('장바구니에 추가 버튼 눌렀음')
            try {
                const cartData = {
                    productId: this.product.productId,
                    productName: this.product.productName,
                    productPrice: this.product.productPrice,
                    quantity: 1, // 임시로 기본 수량 1로 설정
                };
                await this.requestAddCartToDjango(cartData);
                this.$router.push({ name: 'CartListPage' });
            } catch (error) {
                console.log('장바구니 추가 과정에서 에러 발생:', error);
            }
        },
        getProductImageUrl (imageName) {
            console.log('imageName:', imageName)
            return require('@/assets/images/uploadImages/' + imageName)
        },
    },
    created () {
        this.requestProductToDjango(this.productId)
    },
}
</script>

<style scoped>
.action-button {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    font-weight: bold;
    padding: 0.75rem 1rem;
    margin: 0.5rem;
    border-radius: 8px;
}

.button-text {
    margin-left: 0.5rem;
}

.button-container {
    display: flex;
    justify-content: center;
    margin-top: 1rem;
}

/* 하이퍼링크 스타일 제거 */
.no-underline {
    text-decoration: none;
}

/* router-link 스타일 재정의 */
.router-link {
    text-decoration: none;
    color: inherit;
}
</style>