
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
                <v-text-field v-model="content" label="내용" auto-grow/>
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
                console.log('작성 완료 버튼 눌렀지 ?')

                const payload = {
                    title: this.title,
                    writer: this.writer,
                    content: this.content,
                }

                console.log('payload check:', payload)

                const board = await this.requestCreateBoardToDjango(payload)
                // 글 작성이 완료되었다면 보편적으로 작성한 글을 볼 수 있는 읽기 페이지로 감
                // 아직 Road 구현 안했으니까 여기서 우선 정지
        
            },
            async onCancel () {
                console.log('취소 버튼 눌렀지 ?')
            }
        }
    }
    </script>