from watchlist.models import Movie
from rest_framework.response import Response
from watchlist.api.serializer import MovieSerializers
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        data = MovieSerializers(movie, many=True)
        return Response(data.data)
    if request.method == 'POST':
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
def particular_movie(request, id):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=id)
        data = MovieSerializers(movie)
        return Response(data.data)
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return Response()
