<template>
    <v-container>
        <h2>Vue3 + Vuetify3 + TypeScript 게시물 수정!</h2>
        <v-card v-if="board">
            <v-card-title>게시물 정보</v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="title" label="제목"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="board.writer" readonly label="작성자"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-textarea v-model="content" label="내용" auto-grow/>
                        </v-col>
                    </v-row>
                    <v-row justify="end">
                        <v-col cols="auto">
                            <v-btn color="primary" @click="onModify">수정 완료</v-btn>
                        
                        </v-col>
                        <v-col cols="auto">
                            <router-link :to="{ name: 'BoardReadPage' }">
                                <v-btn color="secondary">돌아가기</v-btn>
                            </router-link>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex'
const boardModule = 'boardModule'
export default {
    props: {
        boardId: {
            type: String,
            required: true,
        }
    },
    data (){
        return{
            title: '',
            writer: '',
            content: '',
        }
    },
    computed: {
        ...mapState(boardModule, ['board'])
    },
    methods: {
        // 'requestDeleteBoardToDjango' 추후 처리 필요
        ...mapActions(boardModule, ['requestBoardToDjango','requestModifyBoardToDjango']),
        async onModify () {
            console.log('수정 완료를 누르셨습니다!')

            const payload = {
                title: this.title,
                content: this.content,
                boardId: this.boardId
            }
            await this.requestModifyBoardToDjango(payload) 
            await this.$router.push({name: 'BoardReadPage', params: {boardId: this.boardId}}) // 삭제되면 다시 read 페이지로 넘어감
        },
    },
    created () {
        this.requestBoardToDjango(this.boardId).then(() => { // axios에서는 then을 써서 데이터 수정 가능
            this.title = this.board.title // 내부 데이터 수정
            this.writer = this.board.writer
            this.content = this.board.content
        }) // props에 있는 boardId
    },
    
}
</script>