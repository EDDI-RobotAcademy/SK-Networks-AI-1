from django.contrib import admin
from django.urls import path, include
# from django.urls import path, include
# board에 대한 url 정보 추가
urlpatterns = [
    path("admin/", admin.site.urls),
    # board Domain으로 요청이 들어가는 모든 것을
    # board 디렉토리 하위의 urls.py에서 관리하겠다는 의미
    path('product/', include('product.urls')) # product dirs의 url 참고하겠다.
]