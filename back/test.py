from back.zabbix import zabbix
from yandex_tracker_client import TrackerClient

# zabbix.create_task('3736437 Problem: Asterisk-probeg', 'test', 'v.gussarov')
zabbix.closed_task('3736437 Resolved: Asterisk-probeg')

client = TrackerClient(token='AgAEA7qjC7i7AAW3zSixTG743kAdoEGtjtUF8hc', org_id='2120191')



issue = client.issues['TI-1580']
comments = list(issue.comments.get_all())

for comment in comments:
    print(dir(comment))