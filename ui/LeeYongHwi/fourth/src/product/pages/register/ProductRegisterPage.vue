<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="productName" label="상품명"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="price" label="가격"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" class="text-right">
                <v-btn class="ml-2" color="primary" @click="onSubmit">등록</v-btn>
                <v-btn class="ml-1" color="error" @click="onCancel">취소</v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
import { mapActions } from 'vuex'

const productModule = 'productModule'

export default {
    data(){
        return {
            productName: '',
            price: '',
        }
    },

    methods: {
        ...mapActions(productModule, ['requestCreateProductToDjango']),
        async onSubmit () {
            console.log('등록 완료')

            const payload = {
                productName: this.productName,
                price: this.price,
            }

            console.log('payload check:', payload)

            const product = await this.requestCreateProductToDjango(payload)
        },
        async onCancel () {
            console.log('취소')
        }
    }
}
</script>