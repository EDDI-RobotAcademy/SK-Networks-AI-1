<template>
    <v-container>
        <h2>Vue + FastAPI Anonymous Post</h2>
        <div style="text-align: left; margin: 15px">
            <router-link :to="{ name: 'PostRegisterPage' }">
                익명 포스트 작성
            </router-link>
        </div>
        <v-data-table
            v-model:items-per-page="perPage"
            :headers="headerTitle"
            :items="pagedItems"
            v-model:pagination="pagination"
            class="elevation-1"
            @click:row="readRow"
            item-value="id"
        />
        <v-pagination
            v-model="pagination.page"
            :length="Math.ceil(postList.length / perPage)"
            color="primary"
        />
    </v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";
const postModule = "postModule";

export default {
    computed: {
        ...mapState(postModule, ["postList"]),
        pagedItems() {
            const startIdx = (this.pagination.page - 1) * this.perPage;
            const endIdx = startIdx + this.perPage;
            return this.postList.slice(startIdx, endIdx);
        },
    },
    mounted() {
        this.requestPostListToFastapi();
    },
    methods: {
        ...mapActions(postModule, ["requestPostListToFastapi"]),
        readRow(event, { item }) {
            this.$router.push({
                name: "PostReadPage",
                params: { id: item["id"].toString() },
            });
        },
    },
    data() {
        return {
            headerTitle: [
                {
                    title: "No",
                    align: "start",
                    sortable: true,
                    key: "id",
                    width: "20%",
                },
                { title: "제목", align: "start", key: "title", width: "30%" },
                { title: "내용", align: "start", key: "content", width: "50%" },
            ],
            perPage: 10,
            pagination: {
                page: 1,
            },
        };
    },
};
</script>
