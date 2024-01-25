# app/certifications/serializers.py

from rest_framework import serializers

from .models import Certification


class CertificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certification
        fields = '__all__'
        read_only_fields = ('id', 'created_date',)
