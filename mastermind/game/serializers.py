from rest_framework import serializers
from .models import Game, Guess


class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guess
        fields = ('id', 'guess_code', 'created', 'game', 'score')

        extra_kwargs = {
            'game': {'write_only': True, 'required': True},
            'score': {'read_only': True},
        }


class GameSerializer(serializers.ModelSerializer):
    guesses = GuessSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        # Secret code field is not present in either write or read requests, as it should always be 'secret' to have fun
        fields = ('id', 'name', 'created', 'guesses')
