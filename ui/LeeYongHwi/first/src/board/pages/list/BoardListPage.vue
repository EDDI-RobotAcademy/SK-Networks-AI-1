<template lang="">
    <v-container>
        <h2>게시판</h2>
        <div style="text-align: left; margin: 15px;">
            <router-link :to="{ name: 'BoardRegisterPage' }">
                게시물 작성
            </router-link>
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
            :length="Math.ceil(boards.length / perPage)"
            color="primary"
            @input="updateItems"/>
    </v-container>
</template>

// npm install axios --legacy-peer-deps

<script>
// 이것은 vuex 때문에 사용 가능
import { mapActions, mapState } from 'vuex'

const boardModule = 'boardModule'

export default {
    components: {
        // RouterLink
    },
    computed: {
        ...mapState(boardModule, ['boards']),
        pagedItems () {
            const startIdx = (this.pagination.page - 1) * this.perPage
            const endIdx = startIdx + this.perPage
            return this.boards.slice(startIdx, endIdx)
        }
    },
    mounted () {
        this.requestBoardListToDjango()
    },
    methods: {
        ...mapActions(boardModule, ['requestBoardListToDjango']),
        readRow (event, { item }) {
            this.$router.push({
                name: 'BoardReadPage',
                params: { boardId: item['boardId'].toString() }
            })
        }
    },
    data () {
        return {
            headerTitle: [
                {
                    title: 'No',
                    align: 'start',
                    sortable: true,
                    key: 'boardId',
                },
                { title: '제목', align: 'end', key: 'title' },
                { title: '작성자', align: 'end', key: 'writer' },
                { title: '작성일자', align: 'end', key: 'regDate' },
            ],
            perPage: 5,
            pagination: {
                page: 1,
            }
        }
    }
}
</script>
