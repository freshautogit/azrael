from django.shortcuts import render
from django.http import HttpResponse
from yandex_tracker_client import TrackerClient
import json

client = TrackerClient(token='AgAEA7qjC7i7AAW3zSixTG743kAdoEGtjtUF8hc', org_id='2120191')


def form(request):
    ticketId = 'https://ya.ru/'
    if request.GET:
        ticketId = request.GET.get('id')
    return render(request, 'form.html', {'ticketId': ticketId})


def get_results(request):
    json_task = json.loads(request.body.decode())
    issue = client.issues[json_task['issueId']]
    t1 = json_task['t1']
    t2 = json_task['t2']
    q = json_task['q']
    if json_task['CSi'] != '0' and json_task['CSi'] != '' and json_task['CSi'] is not None:
        linkedIssueInRateQueue = client.issues.find('"Linked To": ' + str(issue.key))
        # if len(linkedIssueInRateQueue) >= 1:
        if linkedIssueInRateQueue:
            mainTicket = client.issues[linkedIssueInRateQueue[0].key]
            if mainTicket.CSi != '' and mainTicket.CSi != '0' and mainTicket.CSi is not None:
                newCSi = (float(mainTicket.CSi) + float(json_task['CSi'])) / 2
                mainTicket.update(CSi=round(newCSi, 2))
            else:
                mainTicket.update(CSi=json_task['CSi'])
        else:
            issue.comments.create(text='При обработке данных на сервере что-то пошло не так.')
    else:

        if json_task['t1'] == '4026420':
            t1 = 1
        elif json_task['t1'] == '4026425':
            t1 = 2
        elif json_task['t1'] == '4026426':
            t1 = 3
        if json_task['t2'] == '4026427':
            t2 = 1
        elif json_task['t2'] == '4026458':
            t2 = 2
        elif json_task['t2'] == '4026459':
            t2 = 3
        if json_task['q'] == '4026460':
            q = 1
        elif json_task['q'] == '4026493':
            q = 2
        elif json_task['q'] == '4026494':
            q = 3
        CSi = 3 / (t1 ** t1 + t2 ** t2 + q ** q)
        issue.update(tFirst=t1, tSecond=t2, q=q, CSi=round(CSi, 2))
    return HttpResponse(status=201)
