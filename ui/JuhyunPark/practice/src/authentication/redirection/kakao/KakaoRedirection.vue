<Template>
    <div></div>
</Template>

<script>
import {mapActions} from 'vuex'

const authenticationModule = 'authenticationModule'
const accountModule = 'accountModule'

export default {
    methods: {
        ...mapActions(authenticationModule, 
        ['requstAccessTokenToDjangoRedirection', 'requestCreateProductToDjango']) ,
        // ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango']),
        async setRedirectData(){
            const code = this. $route.query.code
            console.log('code:', code)

            await his.requstAccessTokenToDjangoRedirection({code})
            const userInfo = this.requestUserInfoToDjango()
        }
    },
    async created () {
        await this.setRedirectData()
    }
}
</script>
