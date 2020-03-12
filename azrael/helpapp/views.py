from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from helpapp.models import Document
from back import helpForm, wbhook

apply = [".jpeg", ".jpg", ".gif", ".png", ".svg", ".avi", ".mp4", ".zip", ".rar", ".pdf", ".doc", ".docx", ".xls",
          ".xlsx", ".pptx", ".ppt", ".mp3", ".wav", ".odp", ".7z"]


def index(request):
    visitors = request.session.get('visitors', 0)
    request.session['visitors'] = visitors + 1
    return render(request, 'indexF.html', context={'visitors': visitors})


def success(request):
    if request.method == 'POST':

        for f in request.FILES.getlist('userFile'):
            if str(f)[str(f).rindex('.'):] in apply:
                newDoc = Document(userFile=f)
                newDoc.save()

        key = helpForm.acceptTask(request, get_client_ip(request))
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
