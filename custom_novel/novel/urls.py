from django.urls import path

from . import views


urlpatterns = [
    path('owntracks/logtracks', views.manage_owntrack_log, name='logtracks'),
]