<template>
    <!-- v-container : 자동으로 가운데 정렬해줌 -->
    <v-container>
        <h2>안녕 Vue3 TypeScript 기반 Board App이야.</h2>
        <div style="text-align: left; margin: 15px">
            <p>게시물 작성</p>

            <v-data-table
                v-model:item-per-page="perPage"
                :headrs="headerTitle"
                :item="pagedItems"
                v-model:pagination="pagination"
                class="elevation-1"
                @click:row="readRow"
                item-value="boardId"
            />
            <!-- <v-pagination
                v-model="pagination.page"
                :length="Math.ceil(boards.length / perPage)"
                color="primary"
                @input="updateItems"
            /> -->
        </div>
    </v-container>
</template>

<script>
// 이것은 vuex 때문에 사용 가능
import { mapActions, mapState } from "vuex";

const boardModule = "boardModule";

export default {
    components: {
        // RouterLink
    },
    computed: {
        ...mapState(boardModule, ["boards"]),
        pageItems() {
            const startIdx = (this.pagination.page - 1) * this.page;
            const endIdx = startIdx + this.perPage;
            return this.boards.slice(startIdx, endIdx);
        },
    },
    // Vue에는 Life Cycle이 존재한다.
    // create -> mount -< updated -> destroy의 흐름을 가지고 있다.
    // 보편적으로 create, mount, destroy는 단발성이며
    // 주기적으로 update는 반복적이다.
    // 단, vue 내부의 데이터 혹은 컴포넌트가 변화한다 판단해야 갱신된다.
    // create의 경우 vue 컴포넌트(객체)를 생성 할 때 구동하며
    // mounted는 vue 컴포넌트 생성 이후 값들을 붙일 때 구동된다.
    // 실제로 없는 가상의 정보를 생성하여 붙인다 생각하면 좋다.
    // 대표적으로 html 태그에 없던 위의 v-data-table 같은 것이다.
    mounted() {
        this.requestBoardListToDjango();
    },
    // python의 def와 같은 것이다.
    methods: {
        ...mapActions(boardModule, ["requestBoardListToDjango"]),
        readRow(event, { item }) {
            console.log("지금 할 수 있는게 없습니다 !");
        },
    },
    data() {
        return {
            headerTitle: [
                {
                    title: "No",
                    align: "start",
                    sortable: true,
                    key: "boardId",
                },
                { title: "제목", align: "end", key: "title" },
                { title: "작성자", align: "end", key: "writer" },
                { title: "작성일자", align: "end", key: "regDate" },
            ],
            perPage: 5,
            pagination: {
                page: 1,
            },
        };
    },
};
</script>
