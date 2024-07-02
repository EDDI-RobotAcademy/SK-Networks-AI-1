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
                <v-textarea v-model="content" label="내용" auto-grow/>
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

const boardModule = 'boardModule'

export default {
    // 현재 이 Vue 컴포넌트에서 사용하는 변수는 모두 data에 배치됨
    data () {
        return {
            title: '',
            writer: '',
            content: '',
        }
    },
    methods: {
        // method의 경우 실제 컴포넌트가 사용하는 기능 집합임
        // namespace 방식의 vuex board 모듈의 action 기능을 땡겨올 때 사용
        // 그러므로 이것은 boardModule의 action에 정의되어야 함
        // 쉽게 얘기해서 requestCreateBoardToDjango가 boardModule의 action에 정의되어야 한다는 말
        ...mapActions(boardModule, ['requestCreateBoardToDjango']),
        async onSubmit () {
            console.log('작성 완료 버튼 누름')

            const payload = {
                title: this.title,
                writer: this.writer,
                content: this.content,
            }

            console.log('payload check:', payload)

            const board = await this.requestCreateBoardToDjango(payload)
            await this.$router.push({
                name: 'BoardReadPage',
                params: { boardId: board.boardId.toString()} 
            })
        },
        async onCancel () {
            alert('게시글 작성이 취소되었습니다.')
            await this.$router.push({
                name: 'BoardListPage'
        })
    },
    }
}
</script>