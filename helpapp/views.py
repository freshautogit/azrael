from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from helpapp.models import Document
from back.help_form import helpForm
from back.webhook import wbhook

import time

apply = [".jpeg", ".jpg", ".gif", ".png", ".svg", ".avi", ".mp4", ".zip", ".rar", ".pdf", ".doc", ".docx", ".xls",
         ".xlsx", ".pptx", ".ppt", ".mp3", ".wav", ".odp", ".7z"]


def index(request):
    visitors = request.session.get('visitors', 0)
    request.session['visitors'] = visitors + 1
    if request.GET.get('bug') is not None:
        bug = request.GET.get('bug')
        return render(request, 'indexF.html', context={'visitors': visitors, 'bug': bug})
    elif request.GET.get('improvement') is not None:
        improvement = request.GET.get('improvement')
        return render(request, 'indexF.html', context={'visitors': visitors, 'improvement': improvement})
    return render(request, 'indexF.html', context={'visitors': visitors})

#TODO: Добавить обработку сообщений об ошибке и предложений по улучшению
def success(request):
    if request.method == 'POST':

        for f in request.FILES.getlist('userFile'):
            if str(f)[str(f).rindex('.'):] in apply:
                newDoc = Document(userFile=f)
                newDoc.save()
        start_time = time.time()
        key = helpForm.accept_task(request, get_client_ip(request))
        print("--- %s seconds ---" % (time.time() - start_time))
        return HttpResponseRedirect('https://tracker.yandex.ru/' + key)
    else:
        return HttpResponse('Error!')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def webhook(request):
    wbhook.webhook(request)

    return HttpResponse(status=200)
