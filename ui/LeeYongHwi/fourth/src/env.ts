interface Env {
    mode: string | undefined
    api: {
        MAIN_API_URL: string | undefined
    }
}

const env: Env = {
    mode: process.env.MODE_ENV,
    api: {
        MAIN_API_URL: process.env.VUE_APP_BASE_URL,
    },
}

export default env