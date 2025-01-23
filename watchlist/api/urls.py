from django.urls import path, include
from watchlist.api.views import WatchList, particularWatch, StreamPlatformListAV
urlpatterns = [
    path('list/', WatchList.as_view(), name='all movies as list'),
    path('<int:id>', particularWatch.as_view(), name='one movie with this id'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
]
