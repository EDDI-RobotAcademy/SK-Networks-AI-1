interface Env{
    mode: string | undefined
    api: {
        MAIN_API_URL: string | undefined
    }
}

// 위에 추상화시킨 interface 포맷에 맞게 구체화 하면 됨
const env: Env = {
    mode: process.env.MODE_ENV,
    api: {
        MAIN_API_URL: process.env.VUE_APP_BASE_URL,
    },
}
