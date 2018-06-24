from django.contrib import admin
from .models import Game, Guess


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Guess)
class GuessAdmin(admin.ModelAdmin):
    pass
