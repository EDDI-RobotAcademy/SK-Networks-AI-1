// template tag 안에는 자동으로 해당 틀이 튀어나옴
// v-container는 자동으로 가운데 정렬 해주는 기능
// h2 태그는 글자크기 설정 h1 ~ h5 까지
<template>
    <v-container>
        <h2>안녕 Vue3 + Vuetify3 + TypeScript 기반 Board App이야</h2>
        <div style="text-align: left; margin: 15px;">
            <p>
                 게시물 작성
            </p>
            <!-- "pagedItems"가 실제 이 부분이 게시물 데이터임 -->
            <v-data-table 
                v-model:item-per-page="perPage"
                :headers="headerTitle"
                :items="pagedItems"
                v-model:pagination="pagination"
                class = "elevation-1" 
                @click:row="readRow" 
                item-value="boardId"/>
            <!-- <v-pagination
                v-model="pagination.page"
                :length="Math.ceil(boards.length / perPage)"
                color="primary"
                @input="updateItems"/> -->
        </div>
    </v-container>
</template>

<script>
// map 관련은 이것은 vuex 때문에 사용 가능
import {mapActions, mapState} from 'vuex'

// boardModule에 사용될 라이브러리들은 store dir에 넣어 따로 관리하자
// 왜냐면 이걸 안하면 import 할게 엄청 많음 (수십 개 이상..), yaml파일 느낌?
const boardModule = 'boardModule'

export default{
    // 게시판용도로 사용을 위한 board 도메인
    // 게시판을 위한 전초작업
    components: {
        //RouterLink
    },
    // computed : 계산 지원
    computed: {
        ...mapState(boardModule, ['boards']),
        pageItems() {
            const startIdx = (this.pagination.page - 1) * this.page
            const endIdx = startIdx + this.perPage
            return this.boards.slice(startIdx, endIdx)
        }
    },
    // Vue에는 Life Cycle이 존재합니다.
    // create -> mount -> update -> destroy의 흐름을 가지고 있습니다.
    // 보편적으로 create, mount, destroy는 단발성이며
    // 주기적으로 update는 반복적입니다.
    // 단, vue 내부의 데이터 혹은 컴포넌트가 변화한다 판단해야 갱신됩니다.

    // create의 경우 vue 컴포넌트(객체)를 생성 할 때 구동하며
    // mounted는 vue 컴포넌트 생성 이후 값들을 붙일 때 구동됩니다.
    // 값을 붙인다? >> 실제로 없는 가상의 정보를 생성해서 붙인다고 생각하면 됨
    // 대표적으로 html 태그에 없던 위의 v-data-table 같은 것입니다.
    mounted () {
        // BoardList 내용을 장고에 보냄
        this.requestBoardListToDjango()
    },
    // method : python의 def와 같은 것입니다.
    methods: {
        ...mapActions(boardModule, ['requestBoardListToDjango']),
        readRow(event, { item }) {
            console.log('지금 할 수 있는게 없다!')
        }
    },
    // ui는 template tag에서, script tag안에서 어떤 data를 처리할건지 격리해서 구현한다.
    // data : 어떠한 데이터들을 처리할건지
    data () {
        return {
            // headerTitle : 게시판의 맨 위 feature를 설정
            headerTitle : [
                {
                    title: 'No',
                    align: 'start',
                    sortable: 'true',
                    key: 'boardId' // 장고 entity의 pk와 대응하는것을 보겠다. -> boardId
                },
                // content 포함 안시킨 이유 : 내가 관심없을 수 있는데 내용이 길어버리므로 스크롤에 방해..
                // title 클릭하면 content 볼 수 있도록 event
                {title: '제목', align: 'end', key: 'title'},
                {title: '작성자', align: 'end', key: 'writer'},
                {title: '작성일자', align: 'end', key: 'regDate'},
            ],
            // 1페이지에 5개의 게시물이 올라올 수 있다.
            perPage: 5,
            // 시작은 1페이지에서 한다!
            pagination: {
                page: 1, 
            }
        }
    }
}
</script>
// 여기까지가 보드 데이터에 올라올것을 구현했고, 아직 보드가 웹에 올라오진 않음 > ui를 더 꾸며야 함