<template>
    <div></div>
</template>

<script>
import { mapActions } from 'vuex'

const authenticationModule = 'authenticationModule'
const accountModule = 'accountModule'

export default {
    methods: {
        ...mapActions(authenticationModule, ['requestAccessTokenToDjangoRedirection', 'requestUserInfoToDjango', 'requestAddRedisAccessTokenToDjango']),
        ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango']),
        async setRedirectData () {
            const code = this.$route.query.code
            console.log('code', code)

            await this.requestAccessTokenToDjangoRedirection({ code })
            const userInfo = await this.requestUserInfoToDjango()
            const email = userInfo.kakao_account.email
            console.log('email:', email)

            const isEmailDuplication = await this.requestEmailDuplicationCheckToDjango(email)
            // 데이터 타입과 값의 일치가 필요함 '==='
            // 값만 일치하면 됨 '=='
            if (isEmailDuplication === true) {
                console.log('기존 가입 고객입니다!')
                const accessToken = localStorage.getItem("accessToken")
                console.log('accessToken:', accessToken)

                if (accessToken) {
                    await this.requestAddRedisAccessTokenToDjango({ email, accessToken })
                } else {
                    console.error('AccessToken is missing')
                }
                // main page로 push 한다는 뜻
                // router push가 해당 페이지로 넘어간다는 뜻
                this.$router.push('/')

            }else{
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