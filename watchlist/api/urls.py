from django.urls import path, include
from watchlist.api.views import WatchListAV, ReviewCreate, particularWatch, StreamPlatformListAV, StreamPlatformDetailAV, ReviewList, ReviewDetail
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='all-movie'),
    path('<int:id>', particularWatch.as_view(), name="detail"),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:id>', StreamPlatformDetailAV.as_view(), name='streamDetail'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('stream/<int:pk>/review', ReviewList.as_view(),
         name='review-list'),  # reviews of particular movie
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(),
         name='review-create')
]
