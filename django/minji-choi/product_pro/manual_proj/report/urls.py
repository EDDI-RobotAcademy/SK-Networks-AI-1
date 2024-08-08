from django.urls import path, include
from rest_framework.routers import DefaultRouter
from report.controller.views import ReportView

router = DefaultRouter()
router.register(r'report', ReportView, basename='report')

urlpatterns = [
    path('', include(router.urls)),
    path('register', ReportView.as_view({'post': 'reportCreate'}), name='report-register'),
]

# localhost:8000/board/list