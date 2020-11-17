from django.contrib import admin
from django.urls import path
from . import views as main_views

urlpatterns = [
    path('', main_views.home, name='home'),
    path('mark_downloaded/<int:pk>/', main_views.mark_downloaded, name='mark_downloaded'),
    path('mark_un_downloaded/<int:pk>/', main_views.mark_un_downloaded, name='mark_un_downloaded'),
    path('delete_video/<int:pk>/', main_views.delete_video, name='delete_video'),
]