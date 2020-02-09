from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Matchmaking.models import Status
import json

@csrf_exempt
def view_get_post_status(req):

    if req.method=="GET":
        status=Status.objects.all()
        all_status=list(status.values())
        return JsonResponse({
            "Status":all_status
        })

    elif req.method=="POST":
        body=json.loads(req.body)

        current_status=Status.objects.create(fullname=body['fullname'],yourpost=body['yourpost'])
        current_status.save()
       
        return JsonResponse({
            "message":"Added Status",
            "Status":{
                "id":current_status.id,
                "fullname":current_status.fullname,
                "yourpost":current_status.yourpost
            }
        })


@csrf_exempt
def view_getByID_updateByID_deleteByID(req,ID):
    current_status=Status.objects.get(id=ID)
    if req.method=="GET":
        return JsonResponse({
            "Status":{
                "id":current_status.id,
                "fullname":current_status.fullname,
                "yourpost":current_status.yourpost
            }
        })

    elif req.method=="PUT":
        body=json.loads(req.body)

        current_status.fullname=body['fullname']
        current_status.yourpost=body['yourpost']


        current_status.save()

        return JsonResponse({
            "message":"Status Updated",
            "Status":{
                "id":current_status.id,
                "fullname":current_status.fullname,
                "yourpost":current_status.yourpost
            }
        })

    elif req.method=="DELETE":
        current_status.delete()

        return JsonResponse({
            "message":"Status Deleted",
            "Status":{
                "id":current_status.id,
                "fullname":current_status.fullname,
                "yourpost":current_status.yourpost
            }
        })


@csrf_exempt
def pagination(req,pageNo,items):
    start=(pageNo-1)*items
    end=start+items

    if req.method=="GET":
        status=Status.objects.all()
        all_status=list(status.values())
        return JsonResponse({
            "status":all_status[start:end]
        })


