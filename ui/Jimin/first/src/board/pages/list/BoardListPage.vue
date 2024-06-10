<!-- 상품 게시판, 자유 게시판 부분 -->
<!-- template html에는 없는 문법 틀 만드는 문법, 가능한 언어가 vue와 react -->
<!-- v-container 가운데 정렬해준다. 노가다 최소화해줌 -->
<!-- ui는 여기다가(template) data는 여기다가(script) 표현하세요라는 뜻 -->
<!-- headertitle no-번호 align-시작하는 위치에서 정렬 sortable-true로 오름차순 정렬 key는 boardId (django board entity에 보면 있음) -->
<!-- content, updDate는 굳이 볼 필요가 없기 때문에 넣지 않았음 -->
<!-- perpage 페이지가 5개씩 들어온다. page 시작페이지는 1페이지라는 뜻 -->
<!-- v-data-table로 tr td 죽어라 치는거 퉁치는거 -->
<!-- pageItems가 실제 게시물 데이터임 -->
<!-- 지금 하고 있는 것들 vuetify 태그들임 -->


<template>
    <v-container>
        <h2>안녕 Vue3 + Vuetify3 +  TypeScript 기반 Board App이야</h2>
        <div style="text-align: left; margin: 15px;">
            <router-link :to="{ name:'BoardRegisterPage'}">
                게시물 작성
            </router-link>
            <!-- pagedItems가 실제 게시물 데이터임 -->
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
        </div>
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
            const startIdx = (this.pagination.page - 1)*this.page
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
    // mounted는 vue 컴포넌트 생성 이후 값들을 붙일 때 구동됩니다.
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
        readRow(event, {item}){
            console.log('지금 할 수 있는게 없다')
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