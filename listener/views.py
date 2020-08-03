from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ListenerLog


@csrf_exempt
def listener(request):
    """
    {
        "name": "Toolbox",
        "scope": "ACCOUNT",
        "state": "ACTIVE",
        "webhookSubscriptionEvents": [
            "AGREEMENT_ALL"
        ],
        "webhookUrlInfo": {
            "url": "https://adobe.krause.im/listener"
        },
        "applicationDisplayName": "Toolbox"
    }
    """
    client_id = request.headers.get("X-ADOBESIGN-CLIENTID")
    data = request.body.decode("utf-8")
    log = ListenerLog.objects.create(data=data)
    response = JsonResponse({"xAdobeSignClientId": client_id})
    return response
