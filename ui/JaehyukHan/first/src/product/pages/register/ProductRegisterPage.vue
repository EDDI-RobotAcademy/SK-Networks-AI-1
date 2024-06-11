<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="productName" label="상품명"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="productPrice" label="상품 가격"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="productDescription" label="상품 상세 내역" auto-grow/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" class="text-right">
                <v-btn class="ml-2" color="primary" @click="onSubmit">작성 완료</v-btn>
                <v-btn class="ml-1" color="error" @click="onCancel">취소</v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapActions } from 'vuex'

const productModule = 'productModule'

export default{
    data() {
        return {
            productName: '',
            productPrice: '',
            productDescription: '',
        }
    },
    methods: {
        ...mapActions(productModule, ['requestCreateProductToDjango']),
        async onSubmit() {
            console.log('상품 등록 눌렀음')

            const payload = {
                productName: this.productName,
                productPrice: this.productPrice,
                productDescription: this.productDescription,
            }
            
            console.log('payload check:', payload)

            const product = await this.requestCreateProductToDjango(payload)
        },
        async onCancel() {
            console.log('취소 버튼 눌렀음')
        }
    }
}
</script>