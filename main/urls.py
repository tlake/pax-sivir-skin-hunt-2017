from django.conf.urls import url
from main.views import MainView, GameView


urlpatterns = [
    url(r'^$', MainView.as_view()),
    url(r'^game/', GameView.as_view()),
]
