<template lang="">
    <v-container>
        <h2>Shopping Cart</h2>
        <div style="text-align: left; margin: 15px;">
            <router-link :to="{ name:'BoardRegisterPage'}">
                게시물 작성
            </router-link>
            
            
        </div>
        <v-data-table
                v-model:item-per-page="perPage"
                :headers="headerTitle"
                :items="pageItems"
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

<script>
// 밑에 있는 건 vuex 때문에 사용 가능
import {mapActions, mapState} from 'vuex'

const boardModule = 'boardModule'

export default{
    components:{
        // RouterLink
    },
    computed:{
        ...mapState(boardModule, ['boards']),
        pageItems(){
            
            const startIdx = (this.pagination.page - 1)*this.perPage
            const endIdx = startIdx + this.perPage
            return this.boards.slice(startIdx, endIdx)
        }
    },
    // vue에는 Life Cycle이 존재합니다.
    // create -> mount -> update -> destroy의 흐름을 가지고 있습니다.
    // 보편적으로 create, mount, destroy는 단발성이며
    // 주기적으로 update는 반복적입니다.
    // 단, vue 내부의 데이터 혹은 컴포넌트가 변화한다 판단해야 갱신됩니다.
    // create의 경우 vue 컴포넌트(객체)를 생성할 대 구동하며
    // mounted는 vue 컴포넌트 생성 이후 값들을 붙일 때 구동됩니다. 한마디로 페이지가 구성되는 시점을 의미함.
    // html이나 javascript는 단발성 대입밖에 안된다.
    // vue는 없는걸 있는것 처럼 쓴다. 그 시간이 mount이다.
    // 가상의 데이터를 생성해서 붙인다 라는 의미로 받아들이면 된다.
    // 대표적으로 html 태그에 없던 위의 v-data-table 같은 것입니다.
    mounted () {
        this.requestBoardListToDjango()
    },
    // python의 def와 같은 것입니다.
    methods: {
        ...mapActions(boardModule, ['requestBoardListToDjango']),
        readRow (event, { item }) {
            this.$router.push({
                name: 'BoardReadPage',
                params: { boardId: item['boardId'].toString() } // boardreadpage에서 props설정을 했기 때문에 파라미터를 넘길 수 있다
            })
        }
    },
    data(){
        return{
            headerTitle: [
                {
                    title: 'No',
                    align: 'start',
                    sortable: true,
                    key: 'boardId'
                },
                {title: '제목', align: 'end', key: 'title'},
                {title: '작성자', align: 'end', key: 'writer'},
                {title: '작성일자', align: 'end', key: 'regDate'},
            ],
            perPage: 5,
            pagination: {
                page: 1,
            }
        }
    }
}
</script>