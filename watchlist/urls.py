from django.urls import path, include
from watchlist.views import movie_list, particular_movie
urlpatterns = [
    path('list/', movie_list, name='all movies as list'),
    path('<int:id>', particular_movie, name='one movie with this id'),
]
