import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="testpassword")


@pytest.fixture
def api_client():
    return APIClient()


def test_obter_par_de_token(api_client, user):
    url = reverse("token_obtain_pair")
    data = {"username": "testuser", "password": "testpassword"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


def test_refresh_token(api_client, user):
    url_obtain = reverse("token_obtain_pair")
    data = {"username": "testuser", "password": "testpassword"}
    response = api_client.post(url_obtain, data, format="json")
    refresh = response.data["refresh"]
    url_refresh = reverse("token_refresh")
    response = api_client.post(url_refresh, {"refresh": refresh}, format="json")
    assert response.status_code == 200
    assert "access" in response.data


def test_token_verifiy(api_client, user):
    url_obtain = reverse("token_obtain_pair")
    data = {"username": "testuser", "password": "testpassword"}
    response = api_client.post(url_obtain, data, format="json")
    access = response.data["access"]
    url_verify = reverse("token_verify")
    response = api_client.post(url_verify, {"token": access}, format="json")
    assert response.status_code
