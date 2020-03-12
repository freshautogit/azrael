from back import config
import psycopg2

def ypFind(request, full, querySql):
    connection = psycopg2.connect(dbname=config.sql_database, user=config.sql_user,
                            password=config.sql_password, host=config.sql_host)

    resultWords = []
    if full:
        concat = 'id, surname, name, middlename, city, bdate, position, depart, unit, mobile, workphone, email, address, ' \
                 'company '
    else:
        concat = 'id, surname, name, city, position, depart, unit, mobile, workphone, email, address, company'

    request = request.strip()
    arrayWords = request.split(' ')
    try:
        with connection.cursor() as cursor:

            for word in arrayWords:
                sql = "select * from phonebook where concat(" + concat + ") ~* '" + word + "' and fired = 0"

                cursor.execute(sql)
                tempResult = ''
                for row in cursor:
                    for temp in range(len(concat.split(','))):
                        tempResult += str(row[temp]).strip() + ';'
                    tempResult += '\n'
            for temp in tempResult.split('\n'):
                count = 0
                for tempWord in arrayWords:
                    if tempWord.lower() in temp.lower():
                        count += 1
                    if count == len(arrayWords):
                        temp = temp[:len(temp) - 1]
                        resultWords.append(temp.split(';'))
        connection.close()
        return resultWords
    except:
        connection.close()
        return 'Error'
