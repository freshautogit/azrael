# from yandex_tracker_client import TrackerClient
# from back import config
#
# client = TrackerClient(token=config.tracker_token, org_id=config.tracker_org_id)
#
# client.issues.create(
#     queue='AA',
#     summary='Звонок от {0}',
#     type={'name': 'Ticket'},
#     description='*Опиши проблему*\n\n{0}',
#     assignee='v.gussarov',
#     components=['Звонок']
# )
from back.aster import createTask

print(createTask.get_assignee('1298'))