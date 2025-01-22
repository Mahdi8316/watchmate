from django.urls import path, include
from watchlist.api.views import MovieList, particularMovie
urlpatterns = [
    path('list/', MovieList.as_view(), name='all movies as list'),
    path('<int:id>', particularMovie.as_view(), name='one movie with this id'),
]
