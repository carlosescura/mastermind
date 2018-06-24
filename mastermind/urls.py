"""mastermind URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy, re_path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from .game.views import GameViewSet, GuessViewSet

admin.autodiscover()

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'guess', GuessViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
