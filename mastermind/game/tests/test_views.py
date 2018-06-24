# -*- coding: utf-8 -*-
import pytest
from model_mommy import mommy

pytestmark = pytest.mark.django_db

api_version = 'v1'


def test_get_games(client_factory):
    mommy.make('Game', _quantity=3)
    user, client_factory = client_factory()
    response = client_factory.get('/api/{}/games/'.format(api_version))
    assert response.status_code == 200
    assert response.data['count'] == 3


def test_get_single_game(client_factory):
    game = mommy.make('Game')
    user, client_factory = client_factory()
    response = client_factory.get('/api/{}/games/{}/'.format(api_version, game.id))
    assert response.status_code == 200
    assert response.data['id'] == game.id

