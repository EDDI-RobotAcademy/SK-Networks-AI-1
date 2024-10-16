import axios, { AxiosInstance } from "axios";
import { useRuntimeConfig } from "nuxt/app";

let djangoAxiosInst: AxiosInstance | null = null
let fastapiAxiosInst: AxiosInstance | null = null

export function createAxiosInstances() {
    if (!djangoAxiosInst) {
        const config = useRuntimeConfig()
        djangoAxiosInst = axios.create({
            baseURL: config.public.MAIN_API_URL,
            timeout: 2500,
        })
    }
    
    if (!fastapiAxiosInst) {
        const config = useRuntimeConfig()
        fastapiAxiosInst = axios.create({
            baseURL: config.public.AI_BASE_URL,
            timeout: 2500,
        })
    }

    return { djangoAxiosInst, fastapiAxiosInst }
}