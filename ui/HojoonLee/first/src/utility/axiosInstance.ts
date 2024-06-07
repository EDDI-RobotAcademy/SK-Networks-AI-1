import axios, { AxiosInstance } from "axios";
import env from "@/env";
const djangoAxiosInst : AxiosInstance = axios.create({
    // 외부 공격에 대해서 보호하기 위해 env를 씌워서 ip를 모르게 만듦
    baseURL : env.api.MAIN_API_URL,
    timeout : 2500,
})

// 이게 aws에 올라간다. 
export default { djangoAxiosInst }