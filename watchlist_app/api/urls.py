from django.urls import path, include
from .views import StreamPlatformAV,StreamPlatformDetail,WatchListAV,WatchDetailAV


urlpatterns = [
     
     path('list/',WatchListAV.as_view(),name='watch_list'),
     path('<int:pk>',WatchDetailAV.as_view(),name='watch_details'),

     path('stream/',StreamPlatformAV.as_view(),name='stream'),
     path('stream/<int:pk>',StreamPlatformDetail.as_view(),nam='stream_detail'),
     

]