# app/certifications/models.py


from django.db import models

class Certifications(models.Model):
    certification = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    year_obtained = models.CharField(max_length=4)
    cert_expiry_date = models.DateTimeField(max_length=4)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
