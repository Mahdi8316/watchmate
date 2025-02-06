from watchlist.models import WatchList, StreamPlatform, Review
from rest_framework.response import Response
from watchlist.api.serializer import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from watchlist.api.permission import AdminOrReadOnly, ReviewUserOrReadOnly


class ReviewDetail(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, user=user)
        if review_queryset.exists():
            raise ValidationError("you have already reviewed this.")
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating +
                                    serializer.validated_data['rating'])/2

        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        serializer.save(watchlist=watchlist, user=user)


class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView
#                  ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamPlatformListAV(APIView):
    def get(self, request):
        try:
            platforms = StreamPlatform.objects.all()
        except platforms.notFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = StreamPlatformSerializer(
            platforms, many=True, context={'request': request})
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAV(APIView):
    def get(self, request, id):
        platform = StreamPlatform.objects.get(pk=id)
        data = StreamPlatformSerializer(platform, context={'request': request})
        return Response(data.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        platform = StreamPlatform.objects.get(pk=id)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        platform = StreamPlatform.objects.get(pk=id)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
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
