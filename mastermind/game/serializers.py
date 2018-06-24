from rest_framework import serializers
from .models import Game, Guess


class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guess
        fields = ('id', 'guess_code', 'created', 'game')

        extra_kwargs = {
            'game': {'write_only': True, 'required': True}
        }


class GameSerializer(serializers.ModelSerializer):
    guesses = GuessSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'name', 'created', 'guesses', 'secret_code')

        extra_kwargs = {
            'secret_code': {'read_only': True}
        }

