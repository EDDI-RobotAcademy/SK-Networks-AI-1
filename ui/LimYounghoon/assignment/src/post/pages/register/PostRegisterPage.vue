<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-text-field v-model="title" label="제목" />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <v-textarea v-model="content" label="내용" auto-grow />
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" class="text-right">
                <v-btn class="ml-2" color="primary" @click="onSubmit"
                    >작성 완료</v-btn
                >
                <v-btn class="ml-1" color="error" @click="onCancel">취소</v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapActions } from "vuex";

const postModule = "postModule";

export default {
    data() {
        return {
            title: "",
            content: "",
        };
    },
    methods: {
        ...mapActions(postModule, ["requestCreatePostToFastapi"]),
        async onSubmit() {
            const payload = {
                title: this.title,
                content: this.content,
            };

            const postId = await this.requestCreatePostToFastapi(payload);
            await this.$router.push({
                name: "PostReadPage",
                params: { id: postId.toString() },
            });
        },
        async onCancel() {
            console.log("취소 버튼 눌럿음");
            this.$router.go(-1);
        },
    },
};
</script>
