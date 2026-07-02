from django.urls import path

from apps.core.views import db_check


urlpatterns = [
    path("health/db/", db_check, name="db-check"),
]