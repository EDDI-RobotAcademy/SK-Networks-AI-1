<template>
    <v-container>
        <v-btn @click="fetchWordCloud" color="primary" class="mt-3">Generate WordCloud</v-btn>
        <v-img v-if="wordcloud" :src="wordcloud" class="mt-3" max-width="800"></v-img>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            wordcloud: ''
        };
    },
    methods: {
        async fetchWordCloud() {
            try {
                const response = await axios.get('http://localhost:33333/word-cloud');
                this.wordcloud = 'data:image/png;base64,' + response.data.wordcloud;
            } catch (error) {
                console.error(error);
            }
        }
    }
};
</script>

<style>
.v-img {
    display: block;
    margin: 0 auto;
}
</style>
