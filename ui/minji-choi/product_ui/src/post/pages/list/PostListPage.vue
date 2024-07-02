<template>
    <v-container>
        <h2> Vue + FastAPI Anonymous Post</h2>
        <div style="text-align: left; margin: 15px;">
            <router-link :to="{name: 'PostRegisterPage'}">
                익명 포스트 작성
            </router-link>
        </div>
        <v-data-table
                v-model:item-per-page="perPage"
                :headers="headerTitle"
                :items="pagedItems"
                v-model:pagination="pagination"
                class="elevation-1"
                @click:row="readRow"
                item-value="id"></v-data-table>
        <v-pagination
                v-model="pagination.page"
                :length="Math.ceil(postList.length / perPage)"
                color="primary"></v-pagination>
    </v-container> 
</template>

<script>
import { mapState, mapActions } from 'vuex'
const postModule = 'postModule'
export default {
    computed: {
        ...mapState(postModule, ['postList']),
        pagedItems () {
            const startIdx = (this.pagination.page - 1) * this.perPage
            const endIdx = startIdx + this.perPage
            return this.postList.slice(startIdx, endIdx)
        }
    },
    mounted () {
        this.reqeustPostListToFastapi()
    },
    methods: {
        ...mapActions(postModule, ['reqeustPostListToFastapi']),
        readRow(event, { item }) {
            this.$router.push({
                name: 'PostReadPage',
                params: {id: item['id'].toString()}
            })
        }
    },
    data () {
        return {
            headerTitle:[
                {title: "No.", aligin: 'start', sortable:true, key:'id', width:'20%' },         
                {title: "제목", aligin: 'start', sortable:true, key:'title', width:'80%' },       
            ],
            perPage: 10,
            pagination: {
                page: 1,

            }
        }
    }
}
</script>