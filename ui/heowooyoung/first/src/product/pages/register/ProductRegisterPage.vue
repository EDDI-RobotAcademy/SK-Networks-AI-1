<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="productName" label="상품명"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="productPrice" label="가격" type="number"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-textarea v-model="productDescription" label="상품 세부 정보" auto-grow/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-file-input v-model="productImage" label="이미지 파일" prepend-icon="mdi-camera"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <p v-if="uploadedFileName">업르드된 파일: {{ uploadedFileName }}</p>
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

export default {
    data () {
        return {
            productName: '',
            productPrice: 0,
            productDescription: '',
            productImage: null,
            uploadedFileName: '',
        }
    },
    methods: {
        ...mapActions(productModule, ['requestCreateProductToDjango']),
        async onSubmit () {
            console.log('상품 등록 눌렀음')

            try {
                if (this.productImage) {
                    const imageFormData = new FormData()
                    imageFormData.append('productName', this.productName)
                    imageFormData.append('productPrice', this.productPrice.toString())
                    imageFormData.append('productDescription', this.productDescription)
                    imageFormData.append('productImage', this.productImage)

                    const response = await this.requestCreateProductToDjango(imageFormData)
                    this.uploadedFileName = response.data.imageName
                    this.$router.push({ name: 'ProductListPage' })
                } else {
                    console.log('이미지 파일을 선택하세요!')
                }
            } catch (error) {
                console.log('파일 처리 과정에서 에러 발생:', error)
            }
            // 상품 상세 정보 읽기
        },
        async onCancel () {
            console.log('취소 버튼 눌럿음')
            // '이전 routing 경로로 이동해줘' 를 의미함
            this.$router.go(-1)
        }
    }
}
</script>