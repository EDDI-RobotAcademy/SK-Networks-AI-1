<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="title" label="제목"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-textarea v-model="content" label="내용" auto-grow/>
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

const postModule = 'postModule'

export default {
    data () {
        return {
            title: '',
            content: '',
        }
    },
    methods: {
        ...mapActions(postModule, ['requestCreatePostToFastapi']),
        async onSubmit () {
            console.log('작성 완료 버튼 누름')
            const payload = {
                title: this.title,
                content: this.content
            }

            const postId = await this.requestCreatePostToFastapi(payload)
            console.log('postId: ', postId)
            await this.$router.push({
                name: 'PostReadPage',
                params: {id: postId.toString()}
            })
        },
        async onCancel () {
            console.log('취소 버튼 누름')
            alert('등록이 취소되었습니다.');
            this.$router.go(-1)
        }
    }
}
</script>