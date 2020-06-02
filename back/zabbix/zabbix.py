from yandex_tracker_client import TrackerClient

from back import config

client = TrackerClient(token=config.tracker_token, org_id=config.tracker_org_id)


def create_task(subject, message, login):
    try:
        client.issues.create(
            queue='TI',
            summary='{0}'.format(subject),
            description='{0}'.format(message),
            assignee='{0}'.format(login),
            components=['zabbix']
        )
    except Exception as e:
        if e.status_code == 429:
            create_task(subject, message, login)
        else:
            client.issues.create(
                queue='DEV',
                summary='Error from zabbix',
                assignee='v.gussarov',
                description='#FIX\n\nЧто то пошло не так\n{0}'.format(e)
            )


def closed_task(id):
    try:
        id = id[:id.find('Resolved')].strip()
        find = 'Summary: {0} Author: "robotfresh" Status: backlog'.format(id)
        issues = client.issues.find(find)
        for issue in issues:
            transition = issue.transitions['resolved']
            issue.comments.create(text='Fixed', summonees=['v.gussarov'])
            transition.execute()
    except Exception as e:
        if e.status_code == 429:
            closed_task(id)
        else:
            client.issues.create(
                queue='DEV',
                summary='Error from zabbix',
                assignee='v.gussarov',
                description='#FIX\n\nЧто то пошло не так\n{0}'.format(e)
            )