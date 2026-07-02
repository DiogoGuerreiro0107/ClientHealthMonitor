from django.shortcuts import render
from django.views.decorators.http import require_GET

from common.responses import *


@require_GET
def health_beat(request):
    return success_response()