import json

import telebot
from back.aster import createTask
from yandex_tracker_client import TrackerClient
from telebot import apihelper
from back.sql import sql_tracker

client = TrackerClient(token='AgAEA7qjC7i7AAW3zSixTG743kAdoEGtjtUF8hc', org_id='2120191')

arrayFiles = []
arrayFilesFinal = []


def webhook(request):
    json_task = json.loads(request.body.decode())
    if json_task['name'] == 'aster_task':
        createTask.create(json_task['number_user'], json_task['number_assignee'])


def new_task_no_assignee(key):
    issue = client.issues[key]
    trash = 'Предупреждение: Информация, содержащаяся в настоящем сообщении и документах, приложенных к нему, ' \
            'является конфиденциальной. Передача указанной информации третьим лицам без предварительного письменного ' \
            'согласия правообладателя может повлечь ответственность, предусмотренную законодательством Российской ' \
            'Федерации. '

    result = '🔥[{0}](https://tracker.yandex.ru/{0})🔥\n\n{1}\n\n{2}\n\n```новая```'.format(issue.key, issue.summary,
                                                                                            issue.description).replace(
        trash, '')
    bot = telebot.TeleBot('1156708983:AAGI10srt8dG0_MfsDtyZihNG5S4Knqrv-I')
    chat_id_array = sql_tracker.get_distribution()
    for chat_id in chat_id_array:
        try:
            bot.send_message(chat_id, result, parse_mode='markdown')
        except:
            pass


def new_assignee(key):
    issue = client.issues[key]
    trash = 'Предупреждение: Информация, содержащаяся в настоящем сообщении и документах, приложенных к нему, ' \
            'является конфиденциальной. Передача указанной информации третьим лицам без предварительного письменного ' \
            'согласия правообладателя может повлечь ответственность, предусмотренную законодательством Российской ' \
            'Федерации. '

    result = '[{0}](https://tracker.yandex.ru/{0})\n\n{1}\n\n{2}\n\n`назначена на тебя`'.format(issue.key,
                                                                                                issue.summary,
                                                                                                issue.description).replace(
        trash,
        '')
    apihelper.proxy = {'https': 'socks5://fresh:qwe123QWE@freserv.ru:34567'}
    bot = telebot.TeleBot('798242963:AAHJDqan4pAok0FOCwt6qjNaLylRPuQ_wxc')
    try:
        bot.send_message(sql_tracker.get_chat_id(issue.assignee.login), result, parse_mode='markdown')
    except:
        pass
