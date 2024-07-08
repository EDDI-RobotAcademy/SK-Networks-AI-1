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
                                <th>Product Name</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Total</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="item in order.order_items" :key="item.productId">
                                <td>{{ item.product_name }}</td>
                                <td>{{ item.price }}</td>
                                <td>{{ item.quantity }}</td>
                                <td>{{ item.price * item.quantity }}</td>
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
                                <v-btn color="green" @click="goToBack">돌아가기</v-btn>
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
const orderModule = 'orderModule';

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
            if (!this.order || !Array.isArray(this.order.order_items) || this.order.order_items.length === 0) {
                return 0;
            }
            return this.order.order_items.reduce((total, item) => total + item.price * item.quantity, 0);
        }
    },
    methods: {
        ...mapActions("orderModule", ["requestReadOrderToDjango"]),
        async fetchOrderData() {
            const orderId = this.orderId
            console.log('OrderReadPage orderId:', orderId)

            try {
                const response = await this.requestReadOrderToDjango({ orderId })
                this.order = response
                console.log('ordersItemInfo:', this.order)
            } catch (error) {
                console.error('주문 내역 확인 중 에러:', error)
            }
        },
        goToBack() {
            const page = this.$route.query.page || 1;
            this.$router.push({ name: 'OrderListPage', query: { page } });
        }
    },
    created() {
        this.fetchOrderData();
    },
};
</script>

<style scoped>
/* 필요한 스타일을 여기에 추가합니다. */
</style>
