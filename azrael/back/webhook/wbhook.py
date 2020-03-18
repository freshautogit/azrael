import json

from back.aster import createTask

from yandex_tracker_client import TrackerClient

client = TrackerClient(token='AgAEA7qjC7i7AAW3zSixTG743kAdoEGtjtUF8hc', org_id='2120191')

arrayFiles = []
arrayFilesFinal = []


def webhook(request):
    json_task = json.loads(request.body.decode())
    if json_task['name'] == 'aster_task':
        createTask.create(json_task['number_user'], json_task['number_assignee'])
