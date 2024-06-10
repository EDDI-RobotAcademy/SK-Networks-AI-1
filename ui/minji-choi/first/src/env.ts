interface Env {
    mode: string | undefined
    api: {
        MAIN_API_URL: string | undefined
    }
}

// .env 파일을 만들 것임
// 여기있는 설정을 읽고 서버를 구성하는 옵션
// 그러니 .gitignore에 반드시 .env 를 추가해서 제외해야합니다.
const env: Env = {
    mode: process.env.MODE_ENV,
    api: {
        MAIN_API_URL: process.env.VUE_APP_BASE_URL,
    },
}

export default env