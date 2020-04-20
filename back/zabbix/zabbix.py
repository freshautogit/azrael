from yandex_tracker_client import TrackerClient

from back import config

client = TrackerClient(token=config.tracker_token, org_id=config.tracker_org_id)


def create_task(service, type_error, ip, office):
    try:
        client.issues.create(
            queue='TI',
            summary='{0} - {1}'.format(service, type_error),
            description='IP - {0}'.format(ip),
            tags=[office]
        )
    except Exception as e:
        client.issues.create(
            queue='DEV',
            summary='Error from zabbix',
            assignee='v.gussarov',
            description='#FIX\n\nЧто то пошло не так\n{0}'.format(e)
        )
