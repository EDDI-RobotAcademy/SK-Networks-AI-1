<template>
    <div>
        <input type="file" @change="onFileChange" />
        <button @click="uploadFile">Upload</button>
        <button @click="listFiles">List Files</button>
        <div v-if="uploading">Uploading...</div>
        <div v-if="uploadSuccess">Upload Success! URL: {{ uploadedFileURL }}</div>
        <div v-if="uploadError">Upload Error: {{ uploadError }}</div>
        <ul v-if="fileList.length">
            <li v-for="file in fileList" :key="file.Key">{{ file.Key }}</li>
        </ul>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { s3Client, env } from "@/utility/awsFileS3Config";
import { PutObjectCommand, ListObjectsCommand, DeleteObjectCommand, GetObjectCommand, PutObjectAclCommand, ObjectCannedACL } from '@aws-sdk/client-s3';

export default defineComponent({
    data() {
        return {
            selectedFile: null as File | null,
            uploading: false,
            uploadSuccess: false,
            uploadError: null as string | null,
            uploadedFileURL: '',
            fileList: [] as Array<{ Key: string }>,
            fileKey: ''
        };
    },
    methods: {
        onFileChange(event: Event) {
            const input = event.target as HTMLInputElement;
            if (input.files && input.files.length > 0) {
                this.selectedFile = input.files[0];
            }
        },
        async uploadFile() {
            if (!this.selectedFile) {
                alert('Please select a file first.');
                return;
            }

            this.uploading = true;
            this.uploadSuccess = false;
            this.uploadError = null;

            const params = {
                Bucket: 'llm-lecture-bucket',
                Key: this.selectedFile!.name,
                Body: this.selectedFile,
                ACL: 'private' as ObjectCannedACL
            };

            try {
                console.log('Uploading file with params:', params); // 디버깅 정보 추가
                const data = await s3Client.send(new PutObjectCommand(params));
                this.uploading = false;
                this.uploadSuccess = true;
                this.uploadedFileURL = `https://${params.Bucket}.s3.${env.s3.AWS_REGION}.amazonaws.com/${params.Key}`;
                this.fileKey = params.Key;
                console.log('File uploaded successfully:', data);
            } catch (err) {
                this.uploading = false;
                this.uploadError = (err as Error).message;
                console.error('Error uploading file:', err);
            }
        },
        async listFiles() {
            const params = {
                Bucket: 'llm-lecture-bucket'
            };

            try {
                const data = await s3Client.send(new ListObjectsCommand(params));
                this.fileList = data.Contents as Array<{ Key: string }>;
                console.log('Files listed successfully:', data);
            } catch (err) {
                console.error('Error listing files:', err);
            }
        },
        async deleteFile(key: string) {
            const params = {
                Bucket: 'llm-lecture-bucket',
                Key: key
            };

            try {
                const data = await s3Client.send(new DeleteObjectCommand(params));
                console.log('File deleted successfully:', data);
            } catch (err) {
                console.error('Error deleting file:', err);
            }
        },
        async getFile(key: string) {
            const params = {
                Bucket: 'llm-lecture-bucket',
                Key: key
            };

            try {
                const data = await s3Client.send(new GetObjectCommand(params));
                console.log('File retrieved successfully:', data);
            } catch (err) {
                console.error('Error getting file:', err);
            }
        },
        async setFileAcl() {
            const params = {
                Bucket: 'llm-lecture-bucket',
                Key: this.fileKey,
                ACL: 'public-read' as ObjectCannedACL
            };

            try {
                const data = await s3Client.send(new PutObjectAclCommand(params));
                console.log('ACL set successfully:', data);
            } catch (err) {
                console.error('Error setting ACL:', err);
            }
        }
    }
});
</script>

<style scoped>
/* 스타일 정의 */
</style>
