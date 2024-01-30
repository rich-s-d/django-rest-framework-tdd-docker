# app/tests/certifications/test_serializers.py

from certifications.serializers import CertificationSerializer


def test_valid_certification_serializer():
    valid_serializer_data = {
        "certification": "AWS Cloud Practioner",
        "issuer": "AWS",
        "year_obtained": "1987",
        "cert_expiry_date": "2026",
    }
    serializer = CertificationSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_certification_serializer():
    invalid_serializer_data = {
        "certification": "AWS Cloud Practioner",
        "issuer": "AWS",
        "year_obtained": "1987",
    }
    serializer = CertificationSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"cert_expiry_date": ["This field is required."]}
