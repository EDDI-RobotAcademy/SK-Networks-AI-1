<template>
    <v-container>
        <h2>안녕 Vue3 + Vuetify3 + Nuxt3 + TypeScript 기반 Board App이야</h2>
        <div style="text-align: left; margin: 15px;">
            <v-btn color="primary" @click="createPost">
                게시물 작성
            </v-btn>
        </div>
        <v-data-table
            v-model:items-per-page="perPage"
            :headers="headerTitle"
            :items="pagedItems"
            v-model:pagination="pagination"
            class="elevation-1"
            @click:row="readRow"
            item-value="boardId"/>

        <v-pagination
            v-model="pagination.page"
            :length="pageCount"
            color="primary"
            class="mt-4"/>
    </v-container>
</template>

<script>
import { computed, defineComponent, onMounted } from "vue"
import { useBoardStore } from '../stores/boardStore'

export default defineComponent({
    setup () {
        const boardStore = useBoardStore()

        const perPage = ref(5)
        const pagination = ref({ page: 1 })

        const headerTitle = [
            { title: 'No', align: 'start', sortable: true, key: 'boardId', },
            { title: '제목', align: 'end', key: 'title' },
            { title: '작성자', align: 'end', key: 'writer' },
            { title: '작성일자', align: 'end', key: 'regDate' },
        ]

        const pagedItems = computed(() => {
            const startIdx = (pagination.value.page - 1) * perPage.value
            const endIdx = startIdx + perPage.value
            return boardStore.boardList.slice(startIdx, endIdx)
        })

        const pageCount = computed(() => Math.ceil(boardStore.boardList.length / perPage.value))

        const createPost = () => {
            console.log('게시물 작성 클릭')
        }

        const readRow = (event, { item }) => {
            console.log(`게시글 읽기: ${item.title}`)
        }

        onMounted(async () => {
            console.log('requestBoardListToDjango()')
            await boardStore.requestBoardListToDjango()
        })

        return {
            perPage,
            pagination,
            headerTitle,
            pagedItems,
            createPost,
            readRow,
            pageCount,
        }
    },
})
</script>
