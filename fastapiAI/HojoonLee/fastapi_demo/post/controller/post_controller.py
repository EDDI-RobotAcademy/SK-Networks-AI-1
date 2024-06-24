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

# getMySqlPool을 통해 llm_lecture_db에 있는 모든 table을 입력으로 받아서 postServiceImpl 객체로 반환
# service 객체는 db정보들에 접근할 수 있음 (db_pool)에는 id, pw 등이 다 담겨있으므로..
async def injectPostService(db_pool: Pool = Depends(getMySqlPool)) -> PostServiceImpl:
    return PostServiceImpl(db_pool) # service에 db 환경에 접근가능하게 하겠다.


@postRouter.get("/list", response_model=List[Post]) # Post를 List type으로 return 할 거야라고 명시적 표시
async def postList(postService: PostServiceImpl =
                                Depends(injectPostService)):
    # 위에 처럼 PostService는 inject하여 의존성을 받아야지만 db에 접근가능해짐
    print(f"postList()")
    return await postService.postList()

# form이 들어가는건 모두 controller에서 구현
# .get("router link", explicit return type)
# : 해준 것은 getInstace로 class 객체 받아온다라고 생각하기 >> 그러므로 : 왼쪽에 있는 변수는 : 오른쪽에 있는 클래스의 기능(함수) 사용가능
@postRouter.post("/create", response_model=CreatePostResponseForm) # create에 대한 responseform을 반환 >> 요청에 따라 반환 foramt을 다르게..
async def postCreate(createPostRequestForm: CreatePostRequestForm,
                     postService: PostServiceImpl =
                                Depends(injectPostService)):
    createPostResponseForm = await postService.createPost(createPostRequestForm.toCreatePostRequest())
    return createPostResponseForm

@postRouter.get("/read/{postId}", response_model=Post)
async def postRead(postId: int,
                   postService: PostServiceImpl =
                   Depends(injectPostService)):
    post = await postService.readPost(postId)

    if not post:
        raise HTTPException(status_code=404, detail="post not found")

    return post