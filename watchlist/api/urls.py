from django.urls import path, include
from watchlist.api.views import WatchListAV, particularWatch, StreamPlatformListAV, StreamPlatformDetailAV
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='all-movie'),
    path('<int:id>', particularWatch.as_view(), name="detail"),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:id>', StreamPlatformDetailAV.as_view(), name='streamDetail')
]
