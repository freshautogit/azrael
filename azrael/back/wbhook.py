import datetime
import json
import os
import pymysql.cursors
import traceback

from yandex_tracker_client import TrackerClient

client = TrackerClient(token='AgAEA7qjC7i7AAW3zSixTG743kAdoEGtjtUF8hc', org_id='2120191')

arrayFiles = []
arrayFilesFinal = []


def webhook(request):
    jsonTask = json.loads(request.body.decode())

    if jsonTask['key'] != 'null':

        createLink(jsonTask)

    elif jsonTask['print']:

        print_out()


def print_out():
    issue = client.issues['BUH-32']
    links = issue.links
    array_files_final = []

    now = datetime.datetime.now()

    for attachments in issue.attachments:
        attachments.delete()

    for i in issue.comments:
        i.delete()

    array_files = os.listdir('media/files/')
    for i in array_files:
        array_files_final.append('media/files/' + i)

    if array_files_final:
        issue.comments.create(text=now.strftime("%d-%m-%Y %H:%M"), attachments=array_files_final)

    for i in links:
        i.delete()

    for i in array_files_final:
        os.remove(i)


def createLink(json_task):
    issueKey = json_task['key']

    issue = client.issues[issueKey]
    for attachment in issue.attachments:
        attachment.download_to("media/files/")

    issue = client.issues['BUH-32']
    issue.links.create(issue=issueKey, relationship='relates')


#######################      КАТОК КОДИТ ЕПТЕЛЬ   ##############################
"""
Яндекс.Трекер отправляет запрос вида:
{
"issueKey":"{{issue.key}}",         Ключ заявка
"issueQueue":"{{issue.queue}}",     Очередь
"emailFrom":"{{issue.emailFrom}}"   С какого мыла
}
"""


def queue_selector(request):
    jsonReceivedData = json.loads(request.body.decode())
    try:
        jsonData = {
            'issueKey': jsonReceivedData['issueKey'],
            'issueQueue': jsonReceivedData['issueQueue'],
            'issueFrom': jsonReceivedData['emailFrom'],
        }
    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())

    if jsonData['issueQueue'] == 'Техническая поддержка':
        assignee_autodetect(jsonData, False)
    elif jsonData['issueQueue'] == 'Платежи':
        assignee_autodetect(jsonData, True)
        # assignee_autodetect_buh(jsonData)
    else:
        assignee_autodetect(jsonData, False)


def assignee_autodetect(jsonData, isBuh):
    issue = client.issues[jsonData['issueKey']]
    emailFrom = jsonData['issueFrom']

    try:
        connectionToYp = pymysql.connect(host='176.112.200.192',
                                         user='rtel',
                                         password='qaz123QAZ',
                                         db='TESTyellowpages',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)

        try:
            with connectionToYp.cursor() as cursor:
                queryToPhonebook = "SELECT address FROM phonebook WHERE email=\'" + emailFrom + "\';"
                cursor.execute(queryToPhonebook)
                for row in cursor:
                    if row['address'] != 'null':
                        emailFromAddress = (row['address'])
                    else:
                        print('emailFromAddress = NULL')
                        """
                        TODO: Иначе, прислать уведомление о пустом значении админу
                        """

                queryToUnits = "SELECT * FROM units WHERE address=\'" + emailFromAddress + "\';"
                cursor.execute(queryToUnits)
                for row in cursor:
                    if isBuh:
                        if row['buh_assignee_login'] != 'null':
                            newAssignee = (row['buh_assignee_login'])
                            newTag = (row['tag'])
                            issue.update(assignee=newAssignee, tags=newTag)
                    else:
                        if row['assignee_login'] != 'null':
                            newAssignee = (row['assignee_login'])
                            issue.update(assignee=newAssignee)
                    """
                    TODO: Иначе, прислать уведомление о пустом значении админу
                    """
                connectionToYp.close()
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
            # TODO: Записать ошибку и время в лог
            pass


    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
        pass
        # TODO: Прислать уведомление админу об ошибке подключения к базе
