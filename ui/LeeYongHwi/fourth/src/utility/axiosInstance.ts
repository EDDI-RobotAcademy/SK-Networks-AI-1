import env from "@/env";
import axios, { AxiosInstance } from "axios";

const djangoAxiosInst: AxiosInstance = axios.create({
    baseURL: env.api.MAIN_API_URL,
    timeout: 2500,
})

export default { djangoAxiosInst }