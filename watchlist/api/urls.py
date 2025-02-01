from django.urls import path, include
from watchlist.api.views import WatchList, particularWatch, StreamPlatformListAV, StreamPlatformDetailAV
urlpatterns = [
    path('list/', WatchList.as_view(), name='all movies as list'),
    path('<int:id>', particularWatch.as_view(), name='detail-movie'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:id>', StreamPlatformDetailAV.as_view(), name='streamDetail')
]
