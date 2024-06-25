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
                                <th>Product</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Total</th>
                                <th>Actions</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="item in cartItems" :key="item.cartItemId">
                                <td>{{ item.productName }}</td>
                                <td>{{ item.productPrice }}</td>
                                <td>
                                    <v-text-field
                                        v-model="item.quantity"
                                        type="number"
                                        min="1"
                                        @change="updateQuantity(item)"
                                    ></v-text-field>
                                </td>
                                <td>{{ item.productPrice * item.quantity }}</td>
                                <td>
                                    <v-btn color="red" @click="removeItem(item)">Remove</v-btn>
                                </td>
                            </tr>
                            </tbody>
                        </v-table>
                        <v-divider></v-divider>
                        <v-row>
                            <v-col>
                                <v-btn color="blue" @click="checkout">Checkout</v-btn>
                            </v-col>
                            <v-col class="text-right">
                                <strong>Total: {{ cartTotal }}</strong>
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
    data() {
        return {
            cartItems: [],
        };
    },
    computed: {
        cartTotal() {
            if(!Array.isArray(this.cartItems)||this.cartItems.length === 0){
                return 0;
            }
            return this.cartItems.reduce((total, item) => total + item.productPrice * item.quantity, 0)
        },
    },
    methods: {
        ...mapActions("cartModule", ["requestCartListToDjango"]),
        updateQuantity(item) {
            // 수량 업데이트 로직
            },
        removeItem(item) {
            //상품 제거 로직
            this.cartItems = this.cartItems.filter(cartItem => cartItem.id !== item.id);
        },
        checkout() {
            // 체크아웃 로직
        },
        async fetchCartList(){
            try{
                const response = await this.requestCartListToDjango();
                this.cartItems = response;
            } catch(error){
                console.error("Error fetching cart list:", error);
            }
        }
    },
    created(){
        this.fetchCartList
    },
};
</script>

<style>
/* 필요한 스타일을 여기에 추가합니다. */
</style>
