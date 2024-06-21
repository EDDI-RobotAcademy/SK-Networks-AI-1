// @는 프로젝트 최상위에서 src의 경로입니다.
import axios, {AxiosInstance} from "axios";
import env from "@/env";

// ip를 털리면 문제가 되기 때문에 숨겨야한다.
// ip를 숨기는 것을 support 하는 것이 env이다.
const djangoAxiosInst: AxiosInstance = axios.create({
    baseURL: env.api.MAIN_API_URL,
    timeout: 2500,
})

const fastapiAxiosInst: AxiosInstance = axios.create({
    baseURL: env.api.AI_BASE_URL,
    timeout: 2500,
})

export default {djangoAxiosInst, fastapiAxiosInst}

