"""
URL configuration for commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.controller.views import ProductView

router = DefaultRouter()
router.register(r"product", ProductView)

urlpatterns = [
    path("", include(router.urls)),
    path("list/", ProductView.as_view({"get": "list"}), name="product_list"),
    path("register", ProductView.as_view({"post": "create"}), name="product_register"),
    path("read/<int:pk>", ProductView.as_view({"get": "read"}), name="product_read"),
]
