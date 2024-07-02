<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title>Shopping Cart</v-card-title>
                    <v-card-text>
                        <v-table>
                            <thead>
                            <tr>
                                <th>Select</th>
                                <th>Product</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Total</th>
                                <th>Actions</th>
                            </tr>
                            </thead>
                            <tbody>
                                <!-- cart item 목록 전체를 가져와서 name, price 뿌리는 중 -->
                                <!-- order는 이렇게 productprice가 이렇게 고정값 반영되면 되고, cart는 시세 반영해야하므로 x -->
                            <tr v-for="item in cartItems" :key="item.cartItemId">
                                <td>
                                    <v-checkbox v-model="selectedItems" :value="item"></v-checkbox>
                                </td>
                                <td>{{ item.productName }}</td>
                                <td>{{ item.productPrice }}</td>
                                <td>
                                    <!-- type number로 주었기 때문에 수량 변경 가능 -->
                                    <!-- 여기서 updateQuantity를 통해 django로 요청을 보냄 -->
                                    <v-text-field
                                        v-model="item.quantity"
                                        type="number"
                                        min="1"
                                        @change="updateQuantity(item)"
                                    ></v-text-field>
                                </td>
                                <td>{{ item.productPrice * item.quantity }}</td>
                                <td>
                                    <!-- 카트에서 제거하는 부분 Django와 엮어주기 -->
                                    <v-btn color="red" @click="removeItem(item)">Remove</v-btn>
                                </td>
                            </tr>
                            </tbody>
                        </v-table>
                        <v-divider></v-divider>
                        <v-row>
                            <v-col>
                                <!-- 구매 확정 버튼 -->
                                <v-btn color="blue" @click="confirmCheckout">Checkout</v-btn>
                            </v-col>
                            <v-col class="text-right">
                                <strong>Total: {{ selectedItemsTotal }}</strong>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <!-- 구매 확인 누를 때 confirmaion dialog 띄우기 -->
        <v-dialog v-model="isCheckoutDialogVissible" max-width="500">
            <v-card>
                <v-card-title>Confirm Checkout</v-card-title>
                <v-card-text>Are you sure you want to order the selected items?</v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="isCheckoutDialogVissible = false">Cancel</v-btn>
                    <v-btn color="blue darkne-1" text @click="proceedToOrder">Confirm</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script>
import { mapActions } from "vuex";

const cartModule = 'cartModule'
const orderModule = 'orderModule'

export default {
    data() {
        return {
            // django에서 cartItem list가 와야 vue에 뿌려준다. , selectedItems도 마찬가지
            // 체크 표시가 다 안되어 있다면 confirm 버튼 못 누르도록 설정하기
            cartItems: [],
            selectedItems: [],
            isCheckoutDialogVissible: false,
        };
    },
    computed: {
        // 장바구니에 있는 모든 애들 통합
        cartTotal() {
            if (!Array.isArray(this.cartItems) || this.cartItems.length === 0) {
                return 0;
            }
            return this.cartItems.reduce(
                (total, item) => total + item.productPrice * item.quantity,
                0
            );
        },
        // 장바구니 중 최종적으로 산 것들만 통합
        selectedItemsTotal() {
            if (!Array.isArray(this.selectedItems) || this.selectedItems.length === 0){
                return 0;
            }
            // reduce 연산 : cart에 있는 item들을 다 뽑아서 그 중 total과 item값들만 뽑는다.
            // 각 항목의 총 수량 * 가격 연산 (=시그마)를 위해서 reduce를 사용 (자체 함수를 만드는 lambda의 기능과 비슷)
            return this.selectedItems.reduce(
                (total, item) => total + item.productPrice * item.quantity, 0
            )
        }
    },
    methods: {
        ...mapActions("cartModule", ["requestCartListToDjango"]),
        ...mapActions("orderModule", ["requestCreateOrderToDjango"]),
        updateQuantity(item) {
            // 수량 업데이트 로직
        },
        removeItem(item) {
            // 상품 제거 로직 >> 사실 그냥 해당 cart id 삭제할게가 빠름
            // filter 조건에 부합하는 애들은 삭제하겠다는 의미임
            this.cartItems =
                // 이 조건에 맞는 애들만 뽑아내겠다. (filter)
                // filter와 get 차이 ? : 하나만 뽑을땐 get, list 다 뽑을땐 filter
                this.cartItems.filter(
                    cartItem => cartItem.cartItemId !== item.cartItemId)
            this.selectedItems =
                this.selectedItems.filter(
                    selectedItem => this.selectedItem.cartItemId !== item.cartItemId)
        },
        confirmCheckout() {
            // 체크아웃 로직
            this.isCheckoutDialogVissible = true
        },
        // cartList 불러오기
        async fetchCartList() {
            try {
                const response = await this.requestCartListToDjango();
                this.cartItems = response;
            } catch (error) {
                console.error("Error fetching cart list:", error);
            }
        },

        // 실제 order로 보내는 관련하는 기능, order domain은 최종구매내역 관리하는 도메인
        async proceedToOrder () {
            this.isCheckoutDialogVissible = false

            try {
                const selectedCartItems = this.cartItems.filter(item => this.selectedItems.includes(item));
                const orderItems = selectedCartItems.map(item => ({
                    cartItemId: item.cartItemId,
                    orderPrice: item.productPrice,
                    quantity: item.quantity
                }));
                console.log('orderItems:', orderItems)
                const response = await this.requestCreateOrderToDjango({ items: orderItems });
                const orderId = response.orderId;

                this.$router.push({ name: 'OrderReadPage', params: { orderId: orderId.toString() } });

            } catch (error) {
                console.error('Order creation failed:', error);
            }

            // this.$router.push({ name: 'OrderReadPage', params: { selectedItems: this.selectedItems } });
        },
    },
    created() {
        this.fetchCartList();
    },
};
</script>

<style>
/* 필요한 스타일을 여기에 추가합니다. */
</style>