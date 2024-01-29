# app/movies/urls.py

from django.urls import path, include
from rest_framework import routers

# Using API View
# from .views import MovieList, MovieDetail
# Using ViewSets
from .views import MovieViewSet

router = routers.DefaultRouter()
router.register(r'api/movies', MovieViewSet)


# Using API View
# urlpatterns = [
#     path("api/movies/", MovieList.as_view()),
#     path("api/movies/<int:pk>/", MovieDetail.as_view()),
# ]

urlpatterns = [
    path('', include(router.urls)),
]
