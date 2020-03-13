import json
import pymysql.cursors
import traceback

from back.aster import createTask

from yandex_tracker_client import TrackerClient

client = TrackerClient(token='AgAEA7qjC7i7AAW3zSixTG743kAdoEGtjtUF8hc', org_id='2120191')

arrayFiles = []
arrayFilesFinal = []


def webhook(request):
    json_task = json.loads(request.body.decode())
    if json_task['name'] == 'aster_task':
        createTask.create(json_task['number_user'], json_task['number_assignee'])


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
