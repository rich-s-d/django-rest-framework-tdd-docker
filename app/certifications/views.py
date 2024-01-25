# app/certifications/views.py

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

from django.shortcuts import get_object_or_404
from .models import Certification
from .serializers import CertificationSerializer


class CertificationViewSet(ViewSet):
    queryset = Certification.objects.all()

    def list(self, request):
        serializer = CertificationSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = CertificationSerializer(item)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
