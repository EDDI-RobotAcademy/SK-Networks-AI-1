<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title>전체 주문 리스트</v-card-title>
                    <v-card-text>
                        <v-table v-if="orderList && orderList.length">
                            <thead>
                                <tr>
                                    <th>주문 번호</th>
                                    <th>주문 일자</th>
                                    <th>주문 항목</th>
                                    <th>전체 주문 가격</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="order in orderList" :key="order.orderId">
                                    <td>{{ order.orderId }}</td>
                                    <td>{{ order.orderDate }}</td>
                                    <td>{{ truncateOrderName(order.orderName) }}</td>
                                    <td>{{ order.orderItemTotalPrice }}</td>
                                </tr>
                            </tbody>
                        </v-table>

                        <v-divider></v-divider>

                        <v-row justify="end">
                            <v-btn color="green" @click="goToHome">홈으로 돌아가기</v-btn>
                        </v-row>

                        <v-pagination
                            v-if="totalPageNumber > 1"
                            v-model:page="currentPageNumber"
                            :length="totalPageNumber"
                            @input="fetchOrderList"/>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

const orderModule = 'orderModule'

export default {
    data () {
        return {
            currentPageNumber: 1,
        }
    },
    computed: {
        ...mapGetters(orderModule, ['orderList', 'currentPageNumber', 'totalPageNumber']),
    },
    methods: {
        ...mapActions(orderModule, ['requestOrderListToDjango']),
        async fetchOrderList () {
            await this.requestOrderListToDjango({ page: this.currentPageNumber })
        },
        goToHome () {
            this.$router.push({ name: 'HomeView' })
        },
        truncateOrderName (orderName) {
            const maxLength = 50
            return orderName.length > maxLength ? 
                    orderName.substring(0, maxLength) + '...' : orderName
        }
    },
    watch: {
        currentPageNumber: 'fetchOrderList',
    },
    created () {
        this.fetchOrderList()
    }
}
</script>