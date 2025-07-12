import requests
import pytest


def test_unauthorized_with_mock(requests_mock):
    def matcher_admin_bad_password(request):
        return request.qs == {"username": ["admin"], "password": ["admin"]}

    requests_mock.get(
        "http://127.0.0.1:8000/data/all",
        status_code=401,
        text="",
        additional_matcher=matcher_admin_bad_password
    )

    response = requests.get("http://127.0.0.1:8000/data/all", params={
        "username": "admin",
        "password": "admin"
    })

    assert response.status_code == 401
    assert response.text.strip() == ""


def test_authorized_with_mock(requests_mock):
    def matcher_admin_good_password(request):
        return request.qs == {"username": ["admin"], "password": ["qwerty"]}

    requests_mock.get(
        "http://127.0.0.1:8000/data/all",
        status_code=200,
        text="",
        additional_matcher=matcher_admin_good_password
    )

    response = requests.get("http://127.0.0.1:8000/data/all", params={
        "username": "admin",
        "password": "qwerty"
    })

    assert response.status_code == 200
    assert response.text.strip() == ""