import os

from django.test import TestCase

# Create your tests here.
from yandex_tracker_client import TrackerClient
key = 'IT-20642'
client = TrackerClient(token='AgAEA7qjC7i7AAW3zSpACTlnU0zSug_NNjKvy5E', org_id='2120191')
issue = client.issues[key]
comments = list(issue.comments.get_all())
comment = comments[len(comments)-1]

print(comment.createdBy.login)
for summon in comment.summonees:
    print(summon.login)

print(comment.text)

print(dir(comment))
for comment in comments:
    print(comment.attachments)
attachments = comment.attachments
print(attachments)
path = os.path.dirname(os.path.realpath(__file__)) # получаем путь к директории, в которой лежит этот скрипт
for att in attachments:
    print(path)
    # att.download_to(path) # скачиваем все файлы из тикета туда, где лежит этот скрипт