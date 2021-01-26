"""Webhook listener views"""
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Listener, ListenerLog


@csrf_exempt
def listener(request, listener_id):
    """
    An endpoint ot point a webhook towards.

    Each :model:`auth.User` will have one :model:`listener.Listener` endpoint.

    **Example create command to Adobe Sign's API.**

    .. code-block:: json

        {
            "name": "Toolbox",
            "scope": "ACCOUNT",
            "state": "ACTIVE",
            "webhookSubscriptionEvents": [
                "AGREEMENT_ALL"
            ],
            "webhookUrlInfo": {
                "url": "https://adobe.krause.im/api/listener/{listener_id}"
            },
            "applicationDisplayName": "Toolbox"
        }

    """
    client_id = request.headers.get("X-ADOBESIGN-CLIENTID")

    try:
        data = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        data = {}

    target = Listener.objects.get(pk=listener_id)
    log = ListenerLog.objects.create(listener=target, data=data)
    response = JsonResponse(
        {
            "xAdobeSignClientId": client_id,
            "data": data,
            "log": log.__str__(),
        }
    )

    return response
