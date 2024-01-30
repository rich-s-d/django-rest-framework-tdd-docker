# app/tests/certifications/test_views.py

import pytest

from certifications.models import Certification


@pytest.mark.django_db
def test_add_movie(client):
    certifications = Certification.objects.all()
    assert len(certifications) == 0

    resp = client.post(
        "/api/certifications/",
        {
            "certification": "AWS Certifified DevOps Professional",
            "issuer": "AWS",
            "year_obtained": "2023",
            "cert_expiry_date": "2026",
        },
        content_type="application/json",
    )
    assert resp.status_code == 201
    assert resp.data["certification"] == "AWS Certifified DevOps Professional"

    certifications = Certification.objects.all()
    assert len(certifications) == 1


@pytest.mark.django_db
def test_add_certification_invalid_json(client):
    certifications = Certification.objects.all()
    assert len(certifications) == 0

    resp = client.post("/api/certifications/", {}, content_type="application/json")
    assert resp.status_code == 400

    certifications = Certification.objects.all()
    assert len(certifications) == 0


@pytest.mark.django_db
def test_add_certification_invalid_json_keys(client):
    certifications = Certification.objects.all()
    assert len(certifications) == 0

    resp = client.post(
        "/api/certifications/",
        {
            "certification": "AWS Certifified DevOps Professional",
            "issuer": "AWS",
            "year_obtained": "2023",
        },
        content_type="application/json",
    )
    assert resp.status_code == 400

    certifications = Certification.objects.all()
    assert len(certifications) == 0


@pytest.mark.django_db
def test_get_single_certification(client, add_certification):
    certification = add_certification(
        certification="AWS Certifified DevOps Professional",
        issuer="AWS",
        year_obtained="2023",
        cert_expiry_date="2026",
    )
    resp = client.get(f"/api/certifications/{certification.id}/")
    assert resp.status_code == 200
    assert resp.data["certification"] == "AWS Certifified DevOps Professional"


@pytest.mark.django_db
def test_get_all_certifications(client, add_certification):
    certification_one = add_certification(
        certification="AWS Certifified DevOps Professional",
        issuer="AWS",
        year_obtained="2023",
        cert_expiry_date="2026",
    )
    certification_two = add_certification(
        certification="AWS Certifified Developer Associate",
        issuer="AWS",
        year_obtained="2023",
        cert_expiry_date="2026",
    )
    resp = client.get("/api/certifications/")
    assert resp.status_code == 200
    assert resp.data[0]["certification"] == certification_one.certification
    assert resp.data[1]["certification"] == certification_two.certification
