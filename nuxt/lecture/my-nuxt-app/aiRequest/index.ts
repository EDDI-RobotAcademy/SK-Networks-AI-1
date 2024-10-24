import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from 'path';

export default defineNuxtModule ({
    meta: {
        name: 'aiRequest',
        configKey: 'aiRequest',
    },

    setup(moduleOptions, nuxt) {
        const themeDir = resolve(__dirname, '..')

        nuxt.hook('pages:extend', (pages) => {
            pages.push({
                name: 'ai-request',
                path: '/ai-request/send',
                file: resolve(themeDir, 'aiRequest/pages/send.vue'),
            })
        })

        nuxt.hook('imports:dirs', (dirs) => {
            dirs.push(resolve(__dirname, 'store'))
        })
    },
})