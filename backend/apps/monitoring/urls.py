from django.urls import path

from apps.monitoring.views import *


urlpatterns = [
    path("health/", health_beat, name="health_beat"),
]