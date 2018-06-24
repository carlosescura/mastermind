import random
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .config import game_config


def generate_secret_code():
    """
    Generates a random secret code based on the config rules and the available choices on them

    :return: A list of random choices conforming the secret code
    """
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
    score = ArrayField(models.IntegerField(), default=[])

    class Meta:
        ordering = ('created',)

    '''
    Overriding the Model save method seems a clearer option to allow the inclusion of the score property in the model
    on creation time. Other option could have been use the 'default' value as used in Game model for secret_code 
    generation.
    '''
    def save(self, *args, **kwargs):
        self.score = self.calculate_score()
        super(Guess, self).save(*args, **kwargs)

    def calculate_score(self):
        """
        Calculates the guess score against the related game secret code.
        It returns a score list of values being:
        1 -> Full match (color and position)
        0 -> Color match (but not position)

        :returns: List containing the achieved score
        """
        score = []
        guess_secret_code = self.guess_code
        game_secret_code = self.game.secret_code

        remaining_secrets = []
        remaining_guesses = []

        # Match one by one and search for full matches
        for guess, secret in zip(game_secret_code, guess_secret_code):
            if guess == secret:
                score.append(1)
            else:
                # If we don't have full match , save the rest of the list items in a temporary list
                remaining_guesses.append(guess)
                remaining_secrets.append(secret)

        # Search for each guess element to be present in the remaining secret_code options for partial matches
        for guess in remaining_guesses:
            if guess in remaining_secrets:
                score.append(0)
                remaining_secrets.remove(guess)

        return score
