from typing import List

from aiomysql import Pool
from fastapi import APIRouter, Depends, HTTPException

from async_db.database import getMySqlPool
from post.controller.request_form.create_post_request_form import CreatePostRequestForm
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
async def postCreate(createPostRequestForm: CreatePostRequestForm,
                     postService: PostServiceImpl =
                                Depends(injectPostService)):
    createPostResponseForm = await postService.createPost(
            createPostRequestForm.toCreatePostRequest())
    # 사이즈가 커지면 controller에서 여러가지를 부를 수 있기 때문에
    # 필요에 따라 toCreatePostRequest()말고 다른 것도 부를 수 있음
    return createPostResponseForm

@postRouter.get("/read/{postId}", response_model=Post)
async def postRead(postId: int,
                   postService: PostServiceImpl = Depends(injectPostService)):
    post = await postService.readPost(postId)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post