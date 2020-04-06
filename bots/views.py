from django.http import HttpResponse
from back.aster import createTask
import json


def index_bots(request):
    pass


def aster_create_task(request):
    json_task = json.loads(request.body.decode())
    if json_task['name'] == 'aster_task':
        createTask.create(json_task['number_user'], json_task['number_assignee'], json_task['link_to_call'])
    return HttpResponse(status=200)
