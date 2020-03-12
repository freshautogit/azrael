from yandex_tracker_client import TrackerClient
import os

client = TrackerClient(token="AgAEA7qjC7i7AAW3zUqvtZ8J-kwds9ogfL4iChk", org_id="2120191")


def acceptTask(request, ip):

    

    queue = ''
    priority = 'normal'
    typeTask = 'Ticket'

    text = request.POST['ticketText'].capitalize() + '\n\n'

    if(request.POST['subject'] == '1CD'):
        queue = 'AA'
        typeTask = 'Task'
    elif (request.POST['subject'] == '1CP'):
        queue = 'AC'
    else:
        queue = 'HELPDESK'
        if request.POST['subject'] == 'newAccaunt':

            text += 'Создать учетку: ' + request.POST['username'] + '\n'
            priority = 'critical'

        elif request.POST['subject'] == 'delAccount':

            text += 'Удалить учетку: ' + request.POST['username'] + '\n'
            priority = 'critical'

        elif request.POST['subject'] == 'changeAccount':

            text += 'Изменить учетку: ' + request.POST['username'] + '\n'
            priority = 'critical'


    
   

    if(request.POST['phone'] != ''):
        text += 'Номер телефона: ' + request.POST['phone'] + '\n'
    

    if(request.POST['subPhone'] != ''):
        text += 'Внутренний номер: ' + request.POST['subPhone'] + '\n'
    

    if(request.POST['localIp'] != ''):
        text += 'Внутренний ip: ' + request.POST['localIp'] + '\n'


    
    return createTask(queue, text, ip, request.POST['email'], priority, typeTask, "")





def createTask(queue, text, ip, emailFrom, priority, typeTask, files):

    #pathToFile = checkFile(pathToFile)
    file = ['/home/hack/test3.txt']


    return (client.issues.create(
        queue=queue,
        summary=text[:50],
        type={'name': typeTask},
        emailFrom=emailFrom + '@freshauto.ru',
        emailTo='vadimhacker.ru',
        assignee=getAssignee(ip),
        description=text,
        priority=priority,
        attachments=file
    ).key)




def getAssignee(ip):

    if '185.216.81.72' in ip:
        return '1130000033904338'
    elif '185.216.81.77' in ip:
        return '1130000033904458'

def checkFile(request):

    # transferFiles = null

    # if(request.FILES['userFile']['name'][0] == null){
    #     for i in len(request.FILES['userFile']['tmp_name']):
    #         uploadFile = (os.tempnam(tempfile.gettempdir(), hashlib.sha1(request.FILES['userFile']['name'][i])))
    #         filename = reques.FILES['userFile']['name'][i]
    #         if 
    # }


    applay = [".jpeg", ".jpg", ".gif", ".png", ".svg", ".avi", ".mp4", ".zip", ".rar", ".pdf", ".doc", ".docx", ".xls",
              ".xlsx", ".pptx", ".ppt", ".mp3", ".wav", ".odp", ".7z"]
    finishPathToFile = []

    for test in pathToFiles:

        if test[test.rindex('.'):] in applay:
            finishPathToFile.append(test)
        else:
            print("Error: {0}".format(test))

    return finishPathToFile
