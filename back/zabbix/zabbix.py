from yandex_tracker_client import TrackerClient

from back import config

client = TrackerClient(token=config.tracker_token, org_id=config.tracker_org_id)


def create_task(subject, message, login):
    try:
        client.issues.create(
            queue='TI',
            summary='{0}'.format(subject),
            description='{0}\nlogin = {1}'.format(message, login),
        )
    except Exception as e:
        client.issues.create(
            queue='DEV',
            summary='Error from zabbix',
            assignee='v.gussarov',
            description='#FIX\n\nЧто то пошло не так\n{0}'.format(e)
        )
