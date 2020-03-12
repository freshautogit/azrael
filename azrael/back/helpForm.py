from yandex_tracker_client import TrackerClient
import os
import Sql

client = TrackerClient(token="AgAEA7qjC7i7AAW3zSixTG743kAdoEGtjtUF8hc", org_id="2120191")


def acceptTask(request, ip):
    priority = 'normal'
    typeTask = 'Ticket'

    text = request.POST['ticketText'].capitalize() + '\n\n'

    if request.POST['subject'] == '1CD':
        queue = 'AA'
        typeTask = 'Task'
        assignee = 'robotfresh'
    elif request.POST['subject'] == '1CP':
        queue = 'AC'
        typeTask = 'Task'
        assignee = 'robotfresh'
    else:
        queue = 'HELPDESK'
        assignee = Sql.getAssignee(ip)
        if request.POST['subject'] == 'newAccount':
            text += 'Создать учетку: ' + request.POST['username'] + '\n'
            priority = 'critical'

        elif request.POST['subject'] == 'delAccount':

            text += 'Удалить учетку: ' + request.POST['username'] + '\n'
            priority = 'critical'

        elif request.POST['subject'] == 'changeAccount':

            text += 'Изменить учетку: ' + request.POST['username'] + '\n'
            priority = 'critical'

    if request.POST['phone'] != '':
        text += 'Номер телефона: ' + request.POST['phone'] + '\n'

    if request.POST['subPhone'] != '':
        text += 'Внутренний номер: ' + request.POST['subPhone'] + '\n'

    if request.POST['localIp'] != '':
        text += 'Внутренний ip: ' + request.POST['localIp'] + '\n'

    return createTask(queue, text, request.POST['email'], priority, typeTask, assignee)


def createTask(queue, text, emailFrom, priority, typeTask, assignee):
    pathToFiles = '/home/hack/help/media/files/'

    print(os.listdir(pathToFiles))

    files = []

    for file in os.listdir(pathToFiles):
        files.append(pathToFiles + file)

    pathToFile = checkFile(files)

    key = (client.issues.create(
        queue=queue,
        summary=text[:50],
        type={'name': typeTask},
        emailFrom=emailFrom + '@freshauto.ru',
        emailTo='vadimhacker.ru',
        assignee=assignee,
        description=text,
        priority=priority,
        attachments=pathToFile
    ).key)

    for file in pathToFile:
        os.remove(file)

    return key


def getAssignee(ip):
    if '185.216.81.72' in ip:
        return '1130000033904338'
    elif '185.216.81.77' in ip:
        return '1130000033904458'


def checkFile(pathToFiles):
    apply = [".jpeg", ".jpg", ".gif", ".png", ".svg", ".avi", ".mp4", ".zip", ".rar", ".pdf", ".doc", ".docx", ".xls",
             ".xlsx", ".pptx", ".ppt", ".mp3", ".wav", ".odp", ".7z"]
    finishPathToFile = []

    for test in pathToFiles:

        if test[test.rindex('.'):] in apply:
            finishPathToFile.append(test)
        else:
            print("Error: {0}".format(test))

    return finishPathToFile
