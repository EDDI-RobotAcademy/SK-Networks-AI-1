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

# 원래의 입력은 db_pool인데 Pool의 포맷을 따르고 있다 -> 여기서 Pool은 getMySqlPool에 의존
async def injectPostService(db_pool: Pool = Depends(getMySqlPool)) -> PostServiceImpl:
    return PostServiceImpl(db_pool)

# def func(input) -> return type

@postRouter.get("/list", response_model=List[Post])  # Post를 list type으로 return 할 거야라고 명시적 표시
async def postList(postService: PostServiceImpl =
                                Depends(injectPostService)):
    # 위에 처럼 PostService는 inject하여 의존성을 받아야지만 db에 접근가능
    print(f"controller -> postList()")
    return await postService.postList()


# : 해준것은 getInstance로 class 객체 받아온다라고 생각하기
# -> 그러므로 : 왼쪽에 있는 변수는 : 오른쪽에 있는 클래스의 기능(함수) 사용가능
@postRouter.post("/create", response_model=CreatePostResponseForm)
async def postCreate(createPostRequestForm: CreatePostRequestForm,
                     postService: PostServiceImpl =
                                Depends(injectPostService)):
    createPostResponseForm = await postService.createPost(
            createPostRequestForm.toCreatePostRequest())

    return createPostResponseForm
    # form이 들어가는 건 모두 controller에서 실행
    # 사이즈가 커지면 controller에서 여러가지를 부를 수 있기 때문에
    # 필요에 따라 toCreatePostRequest()말고 다른 것도 부를 수 있음

@postRouter.get("/read/{postId}", response_model=Post)
async def postRead(postId: int,
                   postService: PostServiceImpl = Depends(injectPostService)):
    post = await postService.readPost(postId)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post