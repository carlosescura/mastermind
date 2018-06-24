import pytest
from django.contrib.auth import get_user_model
from model_mommy import mommy
from rest_framework.test import force_authenticate, APIRequestFactory, APIClient


@pytest.fixture(scope='session')
def drf_factory():
    return APIRequestFactory()


@pytest.fixture
def request_factory(drf_factory):
    def factory(method, uri, payload=dict(), **kwargs):
        """A Django-Rest-Framework request factory instance."""
        methods = {
            'post': drf_factory.post,
            'get': drf_factory.get,
            'put': drf_factory.put,
            'patch': drf_factory.patch,
            'delete': drf_factory.delete
        }
        user = mommy.make(get_user_model())
        request = methods[method](uri, payload, **kwargs)
        force_authenticate(request, user=user)
        return user, request

    return factory


@pytest.fixture(scope='session')
def drf_client_factory():
    return APIClient()


@pytest.fixture
def client_factory(drf_client_factory):
    def factory():
        """A Django-Rest-Framework client factory instance."""
        user = mommy.make(get_user_model(), is_staff=True)
        drf_client_factory.force_authenticate(user=user)
        return user, drf_client_factory

    yield factory
    drf_client_factory.force_authenticate(user=None)
