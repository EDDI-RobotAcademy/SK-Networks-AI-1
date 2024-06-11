<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <!-- v-model은 기본적으로 양방향으로 데이터를 주고 받을 수 있음
                 그렇기 때문에 v--model="title"은
                 script 내부에 있는 data인 title에 영향을 줌
                 이와 동일한 방식으로 v-model은 양쪽을 모두 매핑할 수 있습니다. -->
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
                <!-- auto-grow >> 세로로 늘어나야 하는데 가로로 늘어나고 있음 -->
                <v-text-field v-model="content" label="내용" auto-grow/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" class="text-right">
                <!-- 버튼 작성 시 v-btn 사용하며 클릭 트리거로 @click을 사용
                 @click="onSubmit"의 경우 클릭시 onSubmit 함수 구동을 의미함 -->
                <v-btn class="ml-2" color="primary" @click="onSubmit">작성 완료</v-btn>
                <v-btn class="ml-1" color="error" @click="onCancle">취소</v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapActions } from 'vuex'; // mapActions 인식못하면 import 하기 근데 알아서 되긴하네
const boardModule = 'boardModule' // mapActions(boardModule) 인식못하는거 이걸로 해결하기, namespace 방식으로 해결하기

export default {
    // 현재 이 Vue 컴포넌트에서 사용하는 변수는 모두 data에 배치 됨
    data () {
        return {
            title: '',
            writer: '',
            content: '',
        }
    },
    // methods의 경우엔 실제 컴포넌트가 사용하는 기능 집합
    methods: {
        // namespace 방식의 vuex board 모듈의 action 기능을 땡겨올 때 사용
        // 그러므로 이것은 boardModule의 action에 정의되어야 함
        // 쉽게 얘기해서 requestCreateBoardToDjango가 boardModule의 action에 정의되어야 한다는 말
        // 장고에게 보드만들어달라 요청하기
        ...mapActions(boardModule, ['requestCreateBoardToDjango']),
        async onSubmit() {
            console.log('작성 완료 버튼 눌렀지 ?')

            const payload = {
                title: this.title,
                writer: this.writer,
                content: this.content,
            }
            console.log('payload check:', payload)
            const board = await this.requestCreateBoardToDjango(payload)
            // 글 작성이 완료되었다면 보편적으로 작성한 글을 볼 수 있는 읽기 페이지로 감
            // 아직 Read 구현 안 했으니까 여기서 우선 정지
            await this.$router.push({
                name: 'BoardReadPage',
                params: { boardId: board.boardId.toString() }
            })
        },
        async onCancle() {
            console.log('취소 버튼 눌렀지 ?')
        }
    }
}
</script>