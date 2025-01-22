from watchlist.models import Movie
from rest_framework.response import Response
from watchlist.api.serializer import MovieSerializers
from rest_framework.decorators import api_view


@api_view()
def movie_list(request):
    movie = Movie.objects.all()
    data = MovieSerializers(movie, many=True)
    return Response(data.data)


@api_view()
def particular_movie(request, id):
    movie = Movie.objects.get(pk=id)
    data = MovieSerializers(movie)
    return Response(data.data)
