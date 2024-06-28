<template>
    <v-container>
        <h2>Vue3 + Vuetify3 + TypeScript 게시물 읽기!</h2>
        <v-card v-if="board">
            <v-card-title>게시물 정보</v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="board.title" readonly label="제목"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="board.writer" readonly label="작성자"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-textarea v-model="board.content" readonly label="내용" auto-grow/>
                        </v-col>
                    </v-row>
                    <v-row justify="end">
                        <v-col cols="auto">
                            <router-link :to="{ name: 'BoardModifyPage', params: { boardId } }">
                                <v-btn color="primary">수정</v-btn>
                            </router-link>
                        </v-col>
                        <v-col cols="auto">
                            <v-btn color="error" @click="onDelete">삭제</v-btn>
                        </v-col>
                        <v-col cols="auto">
                            <router-link :to="{ name: 'BoardListPage' }">
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
    computed: {
        ...mapState(boardModule, ['board'])
    },
    methods: {
        // 'requestDeleteBoardToDjango' 추후 처리 필요
        ...mapActions(boardModule, ['requestBoardToDjango', 'requestDeleteBoardToDjango']),
        async onDelete () {
            console.log('삭제를 누르셨습니다!')
            await this.requestDeleteBoardToDjango(this.boardId)
            await this.$router.push({ name: 'BoardListPage' })
        },
    },
    created () {
        this.requestBoardToDjango(this.boardId)
    },
}
</script>