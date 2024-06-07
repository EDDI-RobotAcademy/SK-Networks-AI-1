<template>
    <v-container>
        <h2> 안녕 Vue3 TypeScripts3 기반 Board App이야!</h2>
        <div style="text-align: left; margin: 15px;">
            <p>
                게시물 작성
            </p>
            <!-- pagedItems가 실제 게시물 데이터임!! -->
            <v-data-table
                v-model:item-per-page="perPage"
                :headers="headerTitle"
                :items="pagedItems"
                v-model:pagination="pagination"
                class="elevation-1"
                @click:row="readRow"
                item-value="boardId"/>
            <!-- <v-pagination
                v-model="pagination.page"
                :length="Math.ceil(boards.length / perPage)"
                :color="primary"
                @input="updateItems"/> -->

        </div>
    </v-container>
</template>

<script>
// 이것은 vuex 때문에 사용 가능
import {mapActions, mapState} from 'vuex'

const boardModule = 'boardModule'

export default {
    components: {
        // RouterLink 
    },
    computed:{
        ...mapState(boardModule, ['boards']),
        pageItems () {
            const startIdx = (this.pagination.page-1) * this.page
            const endIdx = startIdx + this.perPage
            return this.boards.slice(startIdx,endIdx)
        }
    },
    // Vue에는 Life Cycle이 존재합니다.
    // Create -> mount -> update -> destroy의 흐름을 갖고 있습니다.
    // 보편적으로 create, mount, destroy는 단발성이며, 주기적으로 update는 반복적입니다.
    // 단, vue 내부의 데이터 혹은 컴포넌트가 변화한다 판단해야 갱신됩니다.
    // create의 경우 vue 컴포넌트(객체)를 생성할 때 구동하며, mounted는 vue 컴포넌트 이후 값들을 붙일 때 구동됩니다.
    // 기본적으로 html이나 javascripts는 단발적인 구동밖에 안되는데, mounted를 통해서 가상의 데이터를 생성해서 붙인다고 생각하면 된다!
    // 실제로 없는 가상의 정볼르 생성하여 붙인다고 생각하면 좋습니다.
    // 대표적으로 html 태그에 없던 위의 v-data-table 같은 것입니다.
    // 만약 v-data-table이 없다면 tr td tr td의 연속으로 데이터를 집어넣어야 하지만 해당 태그를 통해 가상의 어떤 환경이 생겨서 가능해진다

    mounted() {
        this.requestBoardListToDjango()
    },
    // python의 def와 같은 것입니다.
    methods: {
        ...mapActions(boardModule, ['requestBoardListToDjango']),
        readRow(event, {item}) {
            console.log('지금 할 수 있는 게 아무것도 없어요')
        }
    },
    data () {
        return {
            headerTitle: [
                {
                    title : 'No',
                    align : 'start',
                    sortable : 'true',
                    key : 'boardId'
                },
                {titie : '제목', align : 'end', key: 'title'},
                {titie : '작성자', align : 'end', key: 'writer'},
                {titie : '작성일자', align : 'end', key: 'regDate'},
                ],
            perPage : 5,
            pagination : {
                page : 1,
            }
            
        }
    }
}
</script>