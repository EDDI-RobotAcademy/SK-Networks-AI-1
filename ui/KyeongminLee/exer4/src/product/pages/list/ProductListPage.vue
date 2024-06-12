<template>
    <v-container>
        <h2>상품 리스트 조회 페이지</h2>
        <!-- <div style="text-align: left; margin: 15px;">
            <p>
                게시물 작성
            </p>
            
            <v-data-table
                    v-model:item-per-page="perPage"
                    :headers="headerTitle"
                    :item="pageItems"
                    v-model:pagination="pagination"
                    class="elevation-1"
                    @click:row="readRow"
                    item-value="boardId"/>
        </div> -->
    </v-container>
</template>

<script>
export default{
    components: {
        // RouterLink
    },
    data () {
        return {
            headerTitle: [
                {
                    title: 'No',
                    align: 'start',
                    // sortable: true,
                },
                { title: '제품명', align: 'end', key: 'product_name' },
                { title: '가격', align: 'end', key: 'price' },
                { title: '제품 설명', align: 'end', key: 'product_description' },
                { title: '등록일자', align: 'end', key: 'created_at' },
            ],
            perPage: 5,
            pagination: {
                page: 1,
            }
        }
    }
}
</script>