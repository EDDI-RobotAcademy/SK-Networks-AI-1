<template>
    <v-container>
        <v-row>
            <v-col cols="12">
        
                <v-text-field v-model="prodname" label="상품명"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="price" label="상품가격"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="writer" label="상품등록자"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-textarea v-model="content" label="상품상세설명" auto-grow/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" class="text-right">
                <v-btn class="ml-2" color="primary" @click="onSubmit">등록</v-btn>
                <router-link :to="{ name: 'ProductListPage' }">
                    <v-btn class="ml-1" color="error" @click="onCancel">취소</v-btn>
                </router-link>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapActions } from 'vuex'

const productModule = 'productModule'

export default {
    // 현재 이 Vue 컴포넌트에서 사용하는 변수는 모두 data에 배치됨
    data () {
        return {
            prodname: '',
            price: '',
            writer: '',
            content: '',
        }
    },
    methods: {
        ...mapActions(productModule, ['requestCreateProductToDjango']),
        async onSubmit () {
            console.log('작성 완료 버튼 누름')

            const payload = {
                prodname: this.prodname,
                price: this.price,
                writer: this.writer,
                content: this.content,
            }
            console.log('payload check:', payload)
            const product = await this.requestCreateProductToDjango(payload)

            await this.$router.push({
                name: 'ProductReadPage',
                params: { productId: product.productId.toString() }
            })
        },
        async onCancel () {
            console.log('취소 버튼 누름')
            alert('상품 등록이 취소되었습니다.');
        }
    }
}
</script>