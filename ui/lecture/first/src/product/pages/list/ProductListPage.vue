<template lang="">
    <v-container>
        <h2>안녕 Vue3 TypeScript 기반 Product App이야</h2>
        <div style="text-align: left; margin: 15px;">
            <p>상품 등록</p>
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
            :length="Math.ceil(productList.length / perPage)"
            color="primary"
            @input="updateItems"/>
    </v-container>
</template>

// npm install axios --legacy-peer-deps

<script>
// 이것은 vuex 때문에 사용 가능
import { mapActions, mapState } from 'vuex'

const productModule = 'productModule'

export default {
    components: {
        // RouterLink
    },
    computed: {
        ...mapState(productModule, ['productList']),
        pagedItems () {
            const startIdx = (this.pagination.page - 1) * this.perPage
            const endIdx = startIdx + this.perPage
            return this.productList.slice(startIdx, endIdx)
        }
    },
    mounted () {
        this.requestProductListToDjango()
    },
    methods: {
        ...mapActions(productModule, ['requestProductListToDjango']),
        readRow (event, { item }) {
            console.log('읽기 구현 할 때 사용!')
        }
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
                { title: '상품명', align: 'end', key: 'productName' },
                { title: '상품 가격', align: 'end', key: 'productPrice' },
            ],
            perPage: 5,
            pagination: {
                page: 1,
            }
        }
    }
}
</script>
