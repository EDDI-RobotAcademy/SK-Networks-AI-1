interface Env {
    mode: string | undefined
    api: {
        MAIN_API_URL: string | undefined
        AI_BASE_URL: string | undefined
    }
    s3: {
        AWS_REGION: string | undefined
        AWS_S3_IDENTITY_POOL_ID: string | undefined
    }
}

// .env라는 파일을 만들 것임
// 여기있는 설정을 읽고 서버를 구성하는 옵션
// .gitignore에 반드시 .env 추가해서 제외해야 합니다.
// 중요한 정보가 여기에 다 들어감
const env: Env = {
    mode: process.env.MODE_ENV,
    api: {
        MAIN_API_URL: process.env.VUE_APP_BASE_URL,
        AI_BASE_URL: process.env.VUE_APP_AI_BASE_URL
    },
    s3: {
        AWS_REGION: process.env.VUE_APP_AWS_REGION,
        AWS_S3_IDENTITY_POOL_ID: process.env.VUE_APP_AWS_S3_IDENTITY_POOL_ID
    }
}

console.log('Loaded environment variables:', env)

if (!env.s3.AWS_REGION || !env.s3.AWS_S3_IDENTITY_POOL_ID) {
    throw new Error("Missing requeired environment variables for AWS configuration")
}


export default env