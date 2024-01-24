# app/tests/certifications/test_models.py

import pytest

from certifications.models import Certification


@pytest.mark.django_db
def test_certifications_model():
    certification = Certification(certification="AWS Cloud Practioner", issuer="AWS", year_obtained=2023, cert_expiry_date=2026)
    certification.save()
    assert certification.certification == "AWS Cloud Practioner"
    assert certification.issuer == "AWS"
    assert certification.year_obtained == 2023
    assert certification.cert_expiry_date == 2026
    assert certification.created_date
    assert str(certification) == certification.certification
