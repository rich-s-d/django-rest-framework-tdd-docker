# app/movies/urls.py

from django.urls import include, path
from rest_framework import routers

from .views import CertificationViewSet

router = routers.DefaultRouter()
router.register(r"api/certifications", CertificationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
