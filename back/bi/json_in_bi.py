import datetime
import json
import requests

from yandex_tracker_client import TrackerClient

from back import config

client = TrackerClient(token=config.tracker_token, org_id=config.tracker_org_id)


def get_json(key):
    issue = client.issues[key]
    log = list(issue.changelog.get_all())
    waiting = 0
    for logs in log:
        for field in list(logs.fields):
            if field['field'].name == 'Очередь':
                if field['from'].name == 'INBOX':
                    created = datetime.datetime.strptime(issue.createdAt, '%Y-%m-%dT%H:%M:%S.%f+0000')
                    updated = datetime.datetime.strptime(logs.updatedAt, '%Y-%m-%dT%H:%M:%S.%f+0000')
                    waiting = (updated - created).seconds // 60
    type = issue.type.name
    priority = issue.priority.name
    key = issue.key
    status = issue.status.name
    try:
        resolution = issue.resolution.name
    except:
        resolution = 'Открыто'
    data = datetime.datetime.strptime(issue.createdAt, '%Y-%m-%dT%H:%M:%S.%f+0000')
    email_from = issue.emailFrom
    try:
        assignee = issue.assignee.display
    except:
        assignee = 'Нет исполнителя'
    components = 'Нет компонента'
    for component in issue.components:
        components = component.name
    queue = issue.queue.name
    data = \
        [
            {
                "type": "{0}".format(type),
                "priority": "{0}".format(priority),
                "key": "{0}".format(key),
                "status": "{0}".format(status),
                "resolution": "{0}".format(resolution),
                "email_from": "{0}".format(email_from),
                "assignee": "{0}".format(assignee),
                "component": "{0}".format(components),
                "queue": "{0}".format(queue),
                "year": "{0}".format(data.year),
                "month": "{0}".format(data.month),
                "create_at": "{0}".format(issue.createdAt),
                "waiting": "{0}".format(waiting)
            }
        ]
    return data


def send_json(key):

    json_data = get_json(key)
    url = 'https://api.powerbi.com/beta/fc0e62fa-9bca-4a57-a959-e1e6a6560165/datasets/fcd345b5-8908-4dc0-9130-cf8b5af278ab/rows?key=s6WWRK0OQuQBPr1cnsm4dNmCqRwIPw%2BC7f75ukNNUl9B09QY2XzncllZhfzalS24G6lqSd0KpcJP2zoMc0lmcw%3D%3D'
    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}

    requests.post(url, data=json.dumps(json_data), headers=headers)
