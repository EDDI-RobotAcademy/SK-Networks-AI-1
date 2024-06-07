// '@'는 프로젝트 최상위에서 src의 경로이다.
import env from "@/env";
import axios, { AxiosInstance } from "axios";

const djangoAxiosInst: AxiosInstance = axios.create({
    baseURL: env.api.MAIN_API_URL,
    timeout: 2500,
});

export default { djangoAxiosInst };
