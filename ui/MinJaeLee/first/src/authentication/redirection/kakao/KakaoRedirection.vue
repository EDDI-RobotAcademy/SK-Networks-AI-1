<template>
    <div></div>
</template>

<script>
import { mapActions } from 'vuex'

const authenticationModule = 'authenticationModule'
const accountModule = 'accountModule'

export default {
    methods: {
        ...mapActions(authenticationModule, [
            'requestAccessTokenToDjangoRedirection',
            'requestUserInfoToDjango',
            'requestAddRedisAccessTokenToDjango',
        ]),
        ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango']),
        async setRedirectData () {
            const code = this.$route.query.code

            await this.requestAccessTokenToDjangoRedirection({ code })
            const userInfo = await this.requestUserInfoToDjango()
            const email = userInfo.kakao_account.email
            console.log('email:', email)

            const isEmailDuplication = 
                await this.requestEmailDuplicationCheckToDjango(email)
            // 데이터 타입과 값의 일치가 필요함 '===',
            // 값만 일치하면 됨 '==' (0, NULL, None, [])
            if (isEmailDuplication === true) {
                console.log('기존 가입 고객입니다!')
                const accessToken = localStorage.getItem("accessToken");

                if (accessToken) {
                    await this.requestAddRedisAccessTokenToDjango({ email, accessToken });  // Fix: Pass as object directly
                } else {
                    console.error('AccessToken is missing');
                }

                this.$router.push('/')
            } else {
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