import pytest
from model_mommy import mommy
from mastermind.game.config import game_config

pytestmark = pytest.mark.django_db


class GameTests:

    def test_random_secret_code_generation(self):
        game = mommy.make('Game')
        assert len(game.secret_code) == game_config['secret_rules']['length']
        for guess in game.secret_code:
            assert guess in game_config['secret_rules']['choices']


class GuessTests:

    def test_guess_score_exists(self):
        pass

    @pytest.mark.parametrize("guess,score", [
        (['RED', 'BLUE', 'GREEN', 'YELLOW'], [1, 1, 1, 1]),
        (['GREEN', 'YELLOW', 'BLUE', 'RED'], [0, 0, 0, 0]),
        (['RED', 'BLUE', 'GREEN', 'RED'], [1, 1, 1]),
        (['RED', 'GREEN', 'BLUE', 'BLUE'], [1, 0, 0])
    ])
    def test_guess_score_is_correct(self, guess, score):
        secret_code = ['RED', 'BLUE', 'GREEN', 'YELLOW']
        game = mommy.make('Game', secret_code=secret_code)
        guess = mommy.make('Guess',
                           game=game,
                           guess_code=guess)
        assert guess.score == score
