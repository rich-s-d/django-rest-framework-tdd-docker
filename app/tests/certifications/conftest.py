# app/tests/movies/conftest.py

import pytest

from certifications.models import Certification


@pytest.fixture(scope='function')
def add_certification():
    def _add_certification(certification, issuer, year_obtained, cert_expiry_date):
        certification = Certification.objects.create(certification=certification, issuer=issuer, year_obtained=year_obtained, cert_expiry_date=cert_expiry_date)
        return certification
    return _add_certification
