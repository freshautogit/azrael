import psycopg2
from yandex_tracker_client import TrackerClient
from back import config

dbname = config.sql_database
user = config.sql_user
password = config.sql_password
host = config.sql_host


def get_user(number):
    mail = ''
    surname = ''
    try:
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        with connection.cursor() as cursor:
            sql = "select surname, name, email from phonebook where workphone = '{0}'".format(number)
            cursor.execute(sql)

            for row in cursor:
                mail = row['email']
                surname = row['surname'] + ' ' + row['name']

        connection.close()
        return mail, surname
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return mail, surname


def get_assignee(number):
    login = ''
    try:
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        with connection.cursor() as cursor:
            sql = "select email from phonebook where workphone = '{0}'".format(number)
            cursor.execute(sql)

            for row in cursor:
                login = row['email']

        connection.close()
        return login[:login.index('@')]
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return login


client = TrackerClient(token=config.tracker_token, org_id=config.tracker_org_id)


def create(number_user, number_assignee):
    email, fio = get_user(number_user)

    if email == '':
        fio = number_user

    try:
        client.issues.create(
            queue='helpdesk',
            emailFrom=email,
            summary='Звонок от {0}'.format(fio),
            type={'name': 'Ticket'},
            description='*Опиши проблему*',
            assignee=get_assignee(number_assignee)
        )
    except Exception as e:
        print("[!] ", e)
        issue = client.issues.create(
            queue='helpdesk',
            emailFrom=email,
            summary='Звонок от {0}'.format(fio),
            type={'name': 'Ticket'},
            description='*Опиши проблему*')
        issue.comments.create(text='#FIX\nЧто то пошло не так\n{0}'.format(e), summonees='v.gussarov')
