import AccountLoginPage from '../pages/login/AccountLoginPage.vue'
import AccountRegisterPage from '../pages/register/AccountRegisterPage.vue'


const AccountRoutes = [
    {
        path: '/account/login',
        name: 'AccountLoginPage',
        component: AccountLoginPage
      },
      {
        path: '/account/register',
        name: 'AccountRegisterPage',
        component: AccountRegisterPage
      },
]

export default AccountRoutes