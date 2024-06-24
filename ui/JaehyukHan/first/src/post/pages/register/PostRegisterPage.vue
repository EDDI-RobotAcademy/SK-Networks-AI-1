<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <!-- v-model은 기본적으로 양방향으로 데이터를 주고 받을 수 있음
                    그렇기 때문에 v-model='title'은
                    script 내부에 있는 data인 title에 영향을 줌
                    이와 동일한 방식으로 맵핑을 할 수 있습니다. -->
                <v-text-field v-model="title" label="제목" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-textarea v-model="content" label="내용" auto-grow />
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

const postModule = 'postModule'

export default {
    data() {
        return {
            title: '',
            content: '',
        }
    },
    methods: {
        ...mapActions(postModule, ['requestCreatePostToFastapi']),
        async onSubmit() {
            console.log('작성 완료 버튼 눌렀지?')

            const payload = {
                title: this.title,
                content: this.content,
            }
            const postId = await this.requestCreatePostToFastapi(payload)
            await this.$router.push({
                name: 'PostReadPage',
                params: { id: postId.toString() }
            })
        },
        async onCancel() {
            console.log('취소 버튼 눌렀지?')
            this.$router.go(-1)
        }
    }
}
</script>