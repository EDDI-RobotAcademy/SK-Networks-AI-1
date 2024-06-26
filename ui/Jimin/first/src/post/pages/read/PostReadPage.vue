<template>
    <v-container>

        <v-card v-if="post">
            <v-card-title>포스팅</v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="post.title" readonly label="제목"/>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12">
                            <v-textarea v-model="post.content" readonly label="내용"/>
                        </v-col>
                    </v-row>
                   
                </v-container>
            </v-card-text>
        </v-card>

        <v-alert v-else type="info">현재 등록된 포스트가 없습니다.</v-alert>
        <div class="button-container">
            
            <router-link :to="{ name: 'PostListPage' }" class="router-link no-underline">
                <v-btn color="secondary" class="action-button">
                    <v-icon>mdi-arrow-left</v-icon>
                    <span class="button-text">돌아가기</span>
                </v-btn>    
            </router-link>
        </div>
    </v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex'
const postModule = 'postModule'

export default {
    props: {
        id: {
            type: String,
            required: true,
        }
    },
    computed: {
        ...mapState(postModule, ['post'])
    },
    methods: {
        
        ...mapActions(postModule, ['requestPostToFastapi']),
        
    },
    created () {
        this.requestPostToFastapi(this.id) 
    },
    
}
</script>