# app/movies/views.py

# from django.http import Http404
# from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Movie
from .serializers import MovieSerializer

# from rest_framework.decorators import action


# Views using ViewSets (https://testdriven.io/blog/drf-views-part-3/)
class MovieViewSet(ViewSet):
    queryset = Movie.objects.all()

    def list(self, request):
        serializer = MovieSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = MovieSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = MovieSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views using API View.
# class MovieList(APIView):
#     def get(self, request, format=None):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MovieDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
