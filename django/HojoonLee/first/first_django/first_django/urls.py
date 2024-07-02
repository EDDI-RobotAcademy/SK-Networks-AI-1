"""
URL configuration for first_django project.

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('board/', include('board.urls')), # board의 url 참고하겠다.
    path('product/', include('product.urls')), # 여기에 추가해줘야 migrate할 때 db상에 테이블 생김
    path('oauth/', include('oauth.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls'))
]