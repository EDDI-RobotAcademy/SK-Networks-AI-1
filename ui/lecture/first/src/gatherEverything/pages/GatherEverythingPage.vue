<template>
    <v-container>
        <h2>Deep Learning Local Server Test</h2>
        <v-btn color="primary" @click="onClickRollDice">딥러닝 학습 시작 버튼</v-btn>
        <v-btn color="secondary" @click="onClickListDice">딥러닝 추론 요청 버튼</v-btn>
        <v-btn color="success" @click="onClickGetResult">결과 확인 버튼</v-btn>
    </v-container>
</template>

<script>
import { mapActions } from 'vuex'

const aiCommandModule = 'aiCommandModule'

export default {
    methods: {
        ...mapActions(aiCommandModule, [
            'requestAICommandToFastAPI', 
            'requestProcessedAICommandResultToFastAPI'
        ]),
        onClickRollDice () {
            console.log("학습 버튼 누름")
            this.requestAICommandToFastAPI(1)
        },
        onClickListDice () {
            console.log("추론 버튼 누름")
            this.requestAICommandToFastAPI(2)
        },
        onClickGetResult () {
            console.log("결과 확인 버튼 누름")
            const processedAICommandResult = this.requestProcessedAICommandResultToFastAPI()
            console.log('AI 명령 처리 결과:', processedAICommandResult)
        },
    }
}
</script>