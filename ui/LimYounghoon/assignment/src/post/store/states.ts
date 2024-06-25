export interface PostState {
    postList: Post[];
    post: Post | null;
}

export interface Post {
    id: number;
    title: string;
    content: string;
}

const state: PostState = {
    postList: [],
    post: null,
};

export default state;
