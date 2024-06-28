"""
URL configuration for llm_class_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 사용자가 요청한 URL에 따른 대응 지침을 작성함.

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # board domain으로 요청이 들어가는 모든 것을
    # board 디렉토리 하위의 urls.py에서 관리하겠다는 의미
    path('board/', include('board.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('account/', include('account.urls')),
    path('oauth/', include('oauth.urls'))
]
