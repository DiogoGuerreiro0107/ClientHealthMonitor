from django.shortcuts import render
from django.views.decorators.http import require_GET

from apps.core.services.health import check_database_connection
from common.responses import *


@require_GET
def db_check(request):
    is_connected = check_database_connection()

    if is_connected:
        return success_response(message="DB is online")

    return unavailable_response(message="BD is offline")