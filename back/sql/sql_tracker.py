import psycopg2
from back import config

dbname = config.sql_database_tracker
user = config.sql_user
password = config.sql_password
host = config.sql_host


def get_distribution():
    try:
        tracker_id_array = []
        chat_id_array = []
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        cursor = connection.cursor()
        cursor.execute("SELECT tracker_id FROM functional WHERE new_tasks='1'")
        for row in cursor:
            tracker_id_array.append(row[0])
        for tracker_id in tracker_id_array:
            cursor.execute("SELECT chat_id FROM workers WHERE tracker_id='{0}'".format(tracker_id))
            for row in cursor:
                chat_id_array.append(row[0])
        return chat_id_array
        connection.close()
    except Exception as e:
        print('#' * 100)
        print("[!] ", e)
        return 'Error'


def get_chat_id(login):
    try:
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        cursor = connection.cursor()
        cursor.execute("SELECT chat_id FROM workers WHERE login='{0}'".format(login))
        for row in cursor:
            return row[0]
        connection.close()
    except Exception as e:
        print('#' * 100)
        print("[!] ", e)
        return 'Error'