from typing import List

from aiomysql import Pool
from fastapi import APIRouter, Depends

from async_db.database import getMySqlPool
from post.controller.response_form.create_post_response_form import CreatePostResponseForm
from post.entity.models import Post
from post.service.post_service_impl import PostServiceImpl
from post.service.request.create_post_request import CreatePostRequest

postRouter = APIRouter()


async def injectPostService(db_pool: Pool = Depends(getMySqlPool)) -> PostServiceImpl:
    return PostServiceImpl(db_pool)


@postRouter.get("/list", response_model=List[Post])
async def postList(postService: PostServiceImpl =
                                Depends(injectPostService)):

    print(f"controller -> postList()")
    return await postService.postList()

@postRouter.post("/create", response_model=CreatePostResponseForm)
async def postCreate(createPostRequest: CreatePostRequest,
                     postService: PostServiceImpl =
                                Depends(injectPostService)):

    createPostResponseForm = await postService.createPost(createPostRequest)
    return createPostResponseForm
