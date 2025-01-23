from watchlist.models import WatchList, StreamPlatform
from rest_framework.response import Response
from watchlist.api.serializer import WatchListSerializer, StreamPlatformSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status


class StreamPlatformListAV(APIView):
    def get(self, request):
        try:
            platforms = StreamPlatform.objects.all()
        except platforms.notFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = StreamPlatformSerializer(platforms, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchList(APIView):
    def get(self, request):
        try:
            movie = WatchList.objects.all()
        except WatchList.notFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = WatchListSerializer(movie, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class particularWatch(APIView):
    def get(self, request, id):
        movie = WatchList.objects.get(pk=id)
        data = WatchListSerializer(movie)
        return Response(data.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        movie = WatchList.objects.get(pk=id)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = WatchList.objects.get(pk=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.all()
#         except Movie.notFound:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         data = MovieSerializers(movie, many=True)
#         return Response(data.data, status=status.HTTP_200_OK)
#     if request.method == 'POST':
#         serializer = MovieSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'DELETE', 'PUT'])
# def particular_movie(request, id):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=id)
#         data = MovieSerializers(movie)
#         return Response(data.data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=id)
#         serializer = MovieSerializers(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
