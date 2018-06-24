import random
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .config import game_config


def generate_secret_code():
    length = game_config['secret_rules']['length']
    secret_choices = game_config['secret_rules']['choices']
    secret = []

    for i in range(length):
        secret.append(secret_choices[random.randint(0, length - 1)])

    return secret


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    secret_code = ArrayField(models.CharField(max_length=50),
                             default=generate_secret_code,
                             editable=False)

    class Meta:
        ordering = ('created',)


class Guess(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    guess_code = ArrayField(models.CharField(max_length=50))
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='guesses')

    class Meta:
        ordering = ('created',)
