import pymysql.cursors

# Подключиться к базе данных.

def getAssignee(ip):
    assignee = ''
    try:
        connection = pymysql.connect(host='176.112.200.192',
                                user='rtel',
                                password='qaz123QAZ',
                                db='help_bd',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = "SELECT login FROM our_ext_ip_addresses WHERE ip=\'" + ip + "\';"
                cursor.execute(sql)
                for row in cursor:
                    if row['login'] != 'null':
                        assignee = (row['login'])
        except:
            pass
        connection.close()
    except:
        pass    

    return assignee if assignee != '' else 'robotfresh'
