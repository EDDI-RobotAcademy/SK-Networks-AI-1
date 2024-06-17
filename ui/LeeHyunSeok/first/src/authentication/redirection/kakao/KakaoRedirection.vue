<template>
    <div></div>
</template>

<script>
import { mapActions } from 'vuex'

const authenticationModule = 'authenticationModule'
const accountModule = 'accountModule'

export default {
    methods: {
        ...mapActions(authenticationModule, 
            ['requestAccessTokenToDjangoRedirection', 'requestUserInfoToDjango']),
        // ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango']),
        async setRedirectData () {
            const code = this.$route.query.code
            console.log('code:', code)

            await this.requestAccessTokenToDjangoRedirection({ code })
            const userInfo = this.requestUserInfoToDjango()
        }
    },
    async created () {
        await this.setRedirectData()
    }
}
</script>