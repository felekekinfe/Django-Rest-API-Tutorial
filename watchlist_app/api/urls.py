from django.urls import path, include
from .views import StreamPlatformAV,StreamPlatformDetail,WatchListAV,WatchDetailAV,ReviewList,ReviewDetails


urlpatterns = [
     
     path('list/',WatchListAV.as_view(),name='watch_list'),
     path('<int:pk>',WatchDetailAV.as_view(),name='watch_details'),

     path('stream/',StreamPlatformAV.as_view(),name='stream'),
     path('stream/<int:pk>',StreamPlatformDetail.as_view(),name='stream_detail'),
     # path('review',ReviewList.as_view(), name='review-list'),
     # path('review/<int:pk>',ReviewDetails.as_view(), name='review-details'),
     path('stream/<int:pk>/review',ReviewList.as_view(), name='review-list'),
     path('stream/review/<int:pk>',ReviewDetails.as_view(), name='review-details')


]