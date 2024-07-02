from aiomysql import Pool
from typing import List

from post.controller.request_form.create_post_request import CreatePostRequest
from post.controller.response_form.create_post_response_form import CreatePostResponseForm
from post.entity.models import Post
from post.repository.post_repository_impl import PostRepositoryImpl
from post.service.post_service import PostService
from post.service.response.create_post_response import CreatePostResponse


class PostServiceImpl(PostService):
    def __init__(self, db_pool: Pool):
        self.__postRepository = PostRepositoryImpl(db_pool)

    async def postList(self) -> List[Post]:
        print('service -> postList()')
        return await self.__postRepository.list()

    async def createPost(self, createPostRequest: CreatePostRequest) -> CreatePostResponseForm:
        newPost = createPostRequest.toPost()
        postId = await self.__postRepository.create(newPost)
        createPostResponse = CreatePostResponse(id = postId)
        return CreatePostResponseForm.fromCreatePostResponse(createPostResponse)