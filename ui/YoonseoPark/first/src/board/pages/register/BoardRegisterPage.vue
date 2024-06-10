<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="title" label="제목"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="writer" label="작성자"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="content" label="내용" auto-grow/>    <!-- auto grow : 내용 많으면 자동으로 공간 증가-->
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" class="text-right">
                <v-btn class="ml-2" color="primary" @click="onSubmit">작성 완료</v-btn> <!-- method에서 선언한 부분 클릭 트리거-->
                <v-btn class="ml-1" color="error" @click="onCancel">취소</v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapActions } from 'vuex'
const boardModule = 'boardModule'

export default {
    data () {
        return {
            title: '',
            writer: '',
            content: '',
        }
    },
    methods: {
        ...mapActions(boardModule, ['requestCreateBoardToDjango']),
        async onSubmit () {
            console.log('작성 완료 버튼 누름')
            
            const payload = {
                title: this.title,
                writer: this.writer,
                content: this.content
            }

            const board = await this.requestCreateBoardToDjango(payload)
            // 글 작성이 완료되었다면 보편적으로 작성한 글을 볼 수 있는 읽기 페이지로 감
            // 아직 Read 구현 안했으니까 여기서 우선 정지
        },
        async onCancel () {
            console.log('취소 버튼 누름')
        }
    }
}
</script>