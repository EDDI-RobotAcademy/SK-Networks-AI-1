from typing import List, Optional
from aiomysql import Pool

from post.controller.response_form.create_post_response_form import CreatePostResponseForm
from post.entity.models import Post
from post.repository.post_repository_impl import PostRepositoryImpl
from post.service.post_service import PostService
from post.service.request.create_post_request import CreatePostRequest
from post.service.response.create_service_response import CreatePostResponse


class PostServiceImpl(PostService):
    # __init__ : 생성자(new) + 초기화
    def __init__(self, db_pool: Pool): # db_pool에 연결
        self.__postRepository = PostRepositoryImpl(db_pool)


    async def postList(self) -> List[Post]: # postList를 호출하면 return은 -> List[Post] 입니다!
        print("service -> postList()")
        return await self.__postRepository.list()

    async def createPost(self, createPostRequest: CreatePostRequest) -> CreatePostResponseForm:
        newPost = createPostRequest.toPost() # 게시글 내용 반환받기
        postId = await self.__postRepository.create(newPost)
        createPostResponse = CreatePostResponse(id=postId)
        return CreatePostResponseForm.fromCreatePostResponse(createPostResponse) # response -> responseform 변환

    async def readPost(self, postId: int) -> Optional[Post]: # Optional : pk none이어도 처리하기 위함
        return await self.__postRepository.findById(postId) # 왜 id=postId 를 하면 안 되지?
