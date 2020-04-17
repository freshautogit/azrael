from django.http import HttpResponse
from back.aster import createTask
from back.bi import json_in_bi
import json


def index_bots(request):
    pass

def aster_create_task(request):
    json_task = json.loads(request.body.decode())
    if json_task['name'] == 'aster_task':
        createTask.create(json_task['number_user'], json_task['number_assignee'], json_task['link_to_call'])
    return HttpResponse(status=200)


def bi(request):
    json_task = json.loads(request.body.decode())
    if json_task['name'] == 'bi':
        json_in_bi.send_json(json_task['key'])
    return HttpResponse(status=200)

