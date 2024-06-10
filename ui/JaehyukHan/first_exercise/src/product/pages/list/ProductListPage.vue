<template lang="">
    <v-container>
        <h2>안녕 Vue3 TypeScript 기반 Product App이야</h2>
        <div style="text-align: left; margin: 15px;">
            <router-link :to="{ name: 'ProductRegisterPage' }">
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
            item-value="productId"/>
        <v-pagination
            v-model="pagination.page"
            :length="Math.ceil(products.length / perPage)"
            color="primary"
            @input="updateItems"/>
    </v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex'

const productModule = 'productModule'

export default {
    components: {
        // RouterLink
    },
    computed: {
        ...mapState(productModule, ['products']),
    },
    mounted () {
        this.requestProductListToDjango()
    },
    methods: {
        ...mapActions(productModule, ['requestProductListToDjango']),
    },
    data () {
        return {
            headerTitle: [
                {
                    title: 'No',
                    align: 'start',
                    sortable: true,
                    key: 'productId',
                },
                { title: '상품 이름', align: 'end', key: 'productName' },
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