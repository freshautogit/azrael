from django.http import HttpResponse
from yandex_tracker_client import TrackerClient
import json

client = TrackerClient(token='AgAEA7qjC7i7AAW3zSixTG743kAdoEGtjtUF8hc', org_id='2120191')

def get_results(request):
    json_task = json.loads(request.body.decode())
    issue = client.issues[json_task['issueId']]
    t1 = int(json_task['t1'])
    t2 = int(json_task['t2'])
    q = int(json_task['q'])
    p = int(json_task['p'])

    if str(json_task['CSi']) != '' and json_task['CSi'] is not None:
        linkedIssueInRateQueue = client.issues.find('"Linked To": ' + str(issue.key))
        if linkedIssueInRateQueue:
            mainTicket = client.issues[linkedIssueInRateQueue[0].key]
            if mainTicket.CSi != '' and mainTicket.CSi is not None:
                newCSi = (round(int(mainTicket.CSi)) + round(int(json_task['CSi']))) / 2
                newT1 = (round(int(mainTicket.tFirst)) + round(int(json_task['t1']))) / 2
                newT2 = (round(int(mainTicket.tSecond)) + round(int(json_task['t2']))) / 2
                newQ = (round(int(mainTicket.q)) + round(int(json_task['q']))) / 2
                newP = (round(int(mainTicket.polite)) + round(int(json_task['p']))) / 2
                mainTicket.update(tFirst=round(newT1), tSecond=round(newT2), q=round(newQ), polite=round(newP), CSi=round(newCSi))
            else:
                mainTicket.update(tFirst=json_task['t1'], tSecond=json_task['t2'], q=json_task['q'], polite=json_task['p'], CSi=json_task['CSi'])
        else:
            issue.comments.create(text='При обработке данных на сервере что-то пошло не так. feedback_rating_form.py line: 30')
    else:
        x = t1 + t2 + q + p
        CSi = (x - 4) / (20 - 4) * 100
        issue.update(CSi=round(CSi))

    return HttpResponse(status=201)
