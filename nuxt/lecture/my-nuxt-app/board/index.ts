import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from 'path';

export default defineNuxtModule ({
    meta: {
        name: 'board',
        configKey: 'board',
    },

    setup(moduleOptions, nuxt) {
        const themeDir = resolve(__dirname, '..')

        // 쉽게 얘기해서 사실상 여기가 board Domain의 router를 설정하는 부분임
        // 기존에 vue에서는 domain/routes.ts에서 작성하고 main router에 연결하는 방식으로 구성하였음
        // Nuxt에서 Domain 규칙을 깨지 않으려면 Domain 패키지 마다
        // nuxt.config.ts에 이러한 라우팅 규칙을 추가해줘야함
        nuxt.hook('pages:extend', (pages) => {
            pages.push({
                name: 'board-list',
                path: '/board/list',
                file: resolve(themeDir, 'board/pages/list.vue'),
            })
        })

        nuxt.hook('imports:dirs', (dirs) => {
            dirs.push(resolve(__dirname, 'store'))
        })
    },
})