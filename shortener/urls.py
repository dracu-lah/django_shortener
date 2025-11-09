from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet, redirect_url

router = DefaultRouter()

router.register(r"", LinkViewSet, basename="link")

urlpatterns = [
    path("", include(router.urls)),
    path("<str:shortened>/open/", redirect_url, name="redirect"),
]
