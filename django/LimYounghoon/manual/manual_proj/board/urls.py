from django.urls import path, include
from rest_framework.routers import DefaultRouter

from board.controller.views import BoardView

router = DefaultRouter()
router.register(r"board", BoardView)

urlpatterns = [
    path("", include(router.urls)),
    # 어떤 경로 요청이 GET 혹은 POST로 있을 경우,
    # as_view({}) 내의 맨 뒤쪽 list 혹은 create 형태가 동작
    # 결론적으로 list는 get 요청으로 오고 이것을 수신하면 controller/views.py 에 있는 list()를 구동함
    path("list/", BoardView.as_view({"get": "list"}), name="board-list"),
    # register는 post 요청이고 이를 수신하면 views.py에 있는 create()을 구동함
    path("register", BoardView.as_view({"post": "create"}), name="board-register"),
    path("read/<int:pk>", BoardView.as_view({"get": "read"}), name="board-read"),
    path(
        "delete/<int:pk>",
        BoardView.as_view({"delete": "removeBoard"}),
        name="board-remove",
    ),
    path(
        "modify/<int:pk>",
        BoardView.as_view({"put": "modifyBoard"}),
        name="board-modify",
    ),
]

# localhost:8000/board/list
