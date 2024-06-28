from typing import List

from aiomysql import Pool
from fastapi import APIRouter, Depends, HTTPException

from async_db.database import getMySqlPool
from post.controller.request_form.create_post_request_form import CreatePostRequestForm
from post.controller.response_form.create_post_response_form import CreatePostResponseForm
from post.entity.models import Post
from post.service.post_service_impl import PostServiceImpl
from post.service.request.create_post_reqeust import CreatePostRequest

postRouter = APIRouter()


async def injectPostService(db_pool: Pool = Depends(getMySqlPool)) -> PostServiceImpl:          #()안에 있는 것은 무조건 input이고 '->' 뒤에 오는건 리턴 타입
    return PostServiceImpl(db_pool)  #service에 db 환경에 접근 가능하게 하기 위해?


@postRouter.get("/list", response_model=List[Post])  #Post의 리턴 타입을 리스트로 할거라고 명시정으로 표시
async def postList(postService: PostServiceImpl =
                                Depends(injectPostService)):

    print(f"controller -> postList()")
    return await postService.postList()

#Form이 들어가면 무조건 Controller쪽에서 구현.
#request가 수신 response가 요청 수신에 대한 응답?
#:해준것은 겟 인스턴스로 클래스 객체 받아온다라고 생각하기 >> 그러므로 : 왼쪽에 있는 변수는 :오른쪽에 있는 클래스의 기능 사용 가능
@postRouter.post("/create",response_model=CreatePostResponseForm)
async def postCreate(createPostRequestForm: CreatePostRequestForm,
                     postService: PostServiceImpl =
                                Depends(injectPostService)):

    createPostResponseForm = await postService.createPost(createPostRequestForm.toCreatePostRequest())
    return createPostResponseForm

@postRouter.get("/read/{postId}", response_model=Post)
async def postRead(postId: int,
                   postService: PostServiceImpl=Depends(injectPostService)):

    post = await postService.readPost(postId)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post