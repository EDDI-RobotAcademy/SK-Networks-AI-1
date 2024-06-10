// '@' 는 프로젝트 최상위에서 src 의 경로입니다.
import env from "@/env";
import axios, { AxiosInstance } from "axios";

const djangoAxiosInst: AxiosInstance = axios.create({
    baseURL: env.api.MAIN_API_URL,
    timeout: 2500,
})

export default { djangoAxiosInst }