from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ListenerLog

def listener(request):
    client_id = request.headers.get("HTTP_X_ADOBESIGN_CLIENTID")
    data = request.body.decode("utf-8")
    log = ListenerLog.objects.create(data=data)
    return JsonResponse({"xAdobeSignClientId": client_id})
