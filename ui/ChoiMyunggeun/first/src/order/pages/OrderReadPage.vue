<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title>주문정보 상세보기</v-card-title>
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
            if (!this.order || !Array.isArray(this.order.items) || 
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
                console.log('OrderReadPage orderId :', orderId)
                
                try {
                    const response = await this.this.requestReadOrderToDjango({ orderId })
                    this.order = response
                    console.log('ordersItemInfo:', this.order)
                } catch (error) {
                    console.error('주문 내역 확인 중 에러:',error)
                }
        },
        goToBack () {
            this.$router.push({ name: 'HomeView' })
        }
    },
    created() {
        this.fetchOrder();
    }
};
</script>

<style>
/* 필요한 스타일을 여기에 추가합니다. */
</style>