import FileS3TestPage from "@/fileS3/pages/FileS3TestPage.vue";

const FileS3TestRoutes = [
    {
        path: '/aws/s3/test',
        name: 'FileS3TestPage',
        components: {
            default: FileS3TestPage
        },
    },
]

export default FileS3TestRoutes