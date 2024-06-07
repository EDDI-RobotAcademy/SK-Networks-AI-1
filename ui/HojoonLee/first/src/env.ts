interface Env{
    mode: string | undefined
    api: {
        MAIN_API_URL: string | undefined
    }
}

// .env 파일을 만들 것임
// 여기 있는 설정을 읽고 서버를 구성하는 옵션
// 그렇기에 .gitignore에 반드시 .env 를 추가해서 제외해야합니다. (내 정보가 저장됨)
const env: Env = {
    mode: process.env.MODE_ENV,
    api: {
        MAIN_API_URL: process.env.VUE_APP_BASE_URL,
    },
}

// export하면서 env를 default상태로 만든다.
export default env