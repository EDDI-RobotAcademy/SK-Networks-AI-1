import axios, { AxiosInstance } from "axios";
import { useRuntimeConfig } from "nuxt/app";

let djangoAxiosInst: AxiosInstance | null = null
let fastapiAxiosInst: AxiosInstance | null = null

export function createAxiosInstances() {
    const config = useRuntimeConfig()

    const mainApiUrl: string = config.public.MAIN_API_URL as string
    const aiBaseUrl: string = config.public.AI_BASE_URL as string

    if (!djangoAxiosInst) {
        djangoAxiosInst = axios.create({
            baseURL: mainApiUrl,
            timeout: 2500,
        })
    }
    
    if (!fastapiAxiosInst) {
        fastapiAxiosInst = axios.create({
            baseURL: aiBaseUrl,
            timeout: 2500,
        })
    }

    return { djangoAxiosInst, fastapiAxiosInst }
}