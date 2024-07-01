<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title>주문 상세 내역 보기</v-card-title>
                    <v-card-text>
                        <v-table v-if="order">
                            <thead>
                            <tr>
                                <th>Product</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Total</th>
                            </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in order.items" :key="item.productId">
                                    <td>{{ item.productName }}</td>
                                    <td>{{ item.productPrice }}</td>
                                    <td>{{ item.quantity }}</td>
                                    <td>{{ item.productPrice * item.quantity }}</td>
                                </tr>
                            </tbody>
                        </v-table>
                        <v-divider></v-divider>
                        <v-row>
                            <v-col class="text-right">
                                <strong>Total: {{ orderTotal }}</strong>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col class="text-right">
                                <v-btn color="green" @click="placeOrder">Place Order</v-btn>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapActions } from 'vuex';
const orderModule = 'orderModule'

export default {
    props: {
        orderId: {
            type: String,
            required: true,
        }
    },
    data() {
        return {
            order: null,
        };
    },
    computed: {
        orderTotal() {
            if (!this.order || 
                    !Array.isArray(this.order.items) || 
                    this.order.items.length === 0) {
                return 0;
            }
            return this.order.items.reduce(
                (total, item) => total + item.productPrice * item.quantity,
                0
            );
        }
    },
    methods: {
        ...mapActions("orderModule", ["requestReadOrderToDjango"]),
        async fetchOrderData() {
            const orderId = this.orderId
            console.log('OrderReadPage orderId:', orderId)

            try {
                const response = await this.requestReadOrderToDjango({ orderId })
            } catch (error) {
                console.error('주문 내역 확인 중 에러:', error)
            }

            // const orderId = this.$route.params.orderId;
            // 여기에서 API 호출 또는 Vuex 액션을 통해 주문 데이터를 가져옵니다.
            // 예시: const response = await this.$store.dispatch('fetchOrder', orderId);
            // this.order = response;
            // 여기서는 더미 데이터를 사용합니다.
            // this.order = {
            //     orderId: orderId,
            //     items: [
            //         { productId: 1, productName: "Product 1", productPrice: 100, quantity: 2 },
            //         { productId: 2, productName: "Product 2", productPrice: 200, quantity: 1 },
            //     ]
            // };
        },
        placeOrder() {
            // 최종 주문 처리 로직
            alert("Order has been placed successfully!");
            // 주문 후 장바구니 초기화 또는 다른 로직 추가
            this.$router.push({ name: 'HomePage' }); // Assuming you want to redirect to HomePage after order
        }
    },
    created() {
        this.fetchOrderData();
    }
};
</script>

<style>
/* 필요한 스타일을 여기에 추가합니다. */
</style>
