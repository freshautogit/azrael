from yandex_tracker_client import TrackerClient
import os
import Sql

client = TrackerClient(token="AgAEA7qjC7i7AAW3zSixTG743kAdoEGtjtUF8hc", org_id="2120191")


def accept_task(request, ip):
    priority = 'normal'
    type_task = 'Ticket'

    text = request.POST['ticketText'].capitalize() + '\n\n'

    if request.POST['subject'] == '1CD':
        queue = 'AA'
        type_task = 'Task'
        assignee = 'robotfresh'
    elif request.POST['subject'] == '1CP':
        queue = 'AC'
        type_task = 'Task'
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

    return create_task(queue, text, request.POST['email'], priority, type_task, assignee)


def create_task(queue, text, email_from, priority, type_task, assignee):
    path_to_files = '/home/hack/help/media/files/'

    print(os.listdir(path_to_files))

    files = []

    for file in os.listdir(path_to_files):
        files.append(path_to_files + file)

    path_to_file = check_file(files)

    key = (client.issues.create(
        queue=queue,
        summary=text[:50],
        type={'name': type_task},
        emailFrom=email_from + '@freshauto.ru',
        emailTo='vadimhacker.ru',
        assignee=assignee,
        description=text,
        priority=priority,
        attachments=path_to_file
    ).key)

    for file in path_to_file:
        os.remove(file)

    return key


def check_file(path_to_files):
    apply = [".jpeg", ".jpg", ".gif", ".png", ".svg", ".avi", ".mp4", ".zip", ".rar", ".pdf", ".doc", ".docx", ".xls",
             ".xlsx", ".pptx", ".ppt", ".mp3", ".wav", ".odp", ".7z"]
    finish_path_to_file = []

    for test in path_to_files:

        if test[test.rindex('.'):] in apply:
            finish_path_to_file.append(test)
        else:
            print("Error: {0}".format(test))

    return finish_path_to_file
