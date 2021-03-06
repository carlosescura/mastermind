from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Game, Guess
from .serializers import GameSerializer, GuessSerializer


class GameViewSet(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, updates and retrieves games

    retrieve:
    Return the given game.

    list:
    Return a list of all the existing games.

    create:
    Create a new game instance.
    """

    # Queryset uses prefetch_related to avoid a huge amount of queries against guesses for each game, using a JOIN
    queryset = Game.objects.all().prefetch_related('guesses')
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)


class GuessViewSet(mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    Creates, updates and retrieves guesses

    retrieve:
    Return the given guess.

    list:
    Return a list of all the existing guesses.

    create:
    Create a new guess instance.
    """
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer
    permission_classes = (IsAuthenticated,)
