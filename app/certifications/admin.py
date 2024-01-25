# app/certifications/admin.py

from django.contrib import admin

from .models import Certification


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    fields = (
        "certification", "issuer", "year_obtained", "created_date", "cert_expiry_date",
    )
    list_display = (
        "certification", "issuer", "year_obtained", "created_date", "cert_expiry_date",
    )
    readonly_fields = (
        "created_date",
    )
