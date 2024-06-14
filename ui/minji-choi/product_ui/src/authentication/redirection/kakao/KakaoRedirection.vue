<template>
    <div></div>
</template>

<script>
import { mapActions } from 'vuex'

const authenticationModule = 'authenticationModule'
const accountModule = 'accountModule'
export default {
    methods: {
        ...mapActions(authenticationModule, ['requestAccessTokenToDjangoRedirection', 'requestUserInfoToDjango']),
        ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango']), // 나중에 AI? 뭔지 모르겠음
        async setRedirectData () {
            const code = this.$route.query.code
            console.log('code: ', code)
            await this.requestAccessTokenToDjangoRedirection({ code })
            const userInfo = await this.requestUserInfoToDjango()
            const email = userInfo.kakao_account.email
         

            console.log('userInfo : ', userInfo)
            console.log('email : ', email)

            const isEmailDuplication = await this.requestEmailDuplicationCheckToDjango(email)
            if (isEmailDuplication === true) { // 데이터 타입과 값의 일치가 필요할 때 '===' 값만 일치 '=='
                alert('기존 가입 고객입니다!')
                console.log('기존 가입 고객입니다!')
                this.$router.push('/') // 메인으로 보낸다
            }  else {
                alert('신규 가입 고객입니다!')
                console.log('신규 가입 고객입니다!')
                this.$router.push('/account/register')
            }
        }
    },
    async created () {
        await this.setRedirectData()
    }
}
</script>