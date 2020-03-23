from back import config
import psycopg2

dbname = config.sql_database
user = config.sql_user
password = config.sql_password
host = config.sql_host


def yp_find(request, full, query_sql):
    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)

    result = []
    result_new = []

    if full:
        concat = 'id, surname, name, middlename, city, bdate, position, depart, unit, mobile, workphone, email, ' \
                 'address, company '
        concat_id = [0, 1, 2, 3, 4, 5, 6, 7, 13, 8, 9, 10, 11, 12]
    else:
        concat = 'id, surname, name, city, position, depart, unit, mobile, workphone, email, address, company'
        concat_id = [0, 1, 2, 4, 6, 13, 7, 8, 9, 10, 11, 12]
    if request is not None:
        request = request.strip()
        array_words = request.split(' ')
    try:
        with connection.cursor() as cursor:

            for word in array_words:
                sql = "select * from phonebook where concat(" + concat + ") ~* '" + word + "' "
                sql = sql + query_sql + " and fired = 0;"
                cursor.execute(sql)
                for row in cursor:
                    row_result = ''
                    for id in concat_id:
                        row_result += str(row[id]).strip() + ';'
                    result.append(row_result.split(';'))
        connection.close()

        for row in result:
            count = 0
            temp_word = []
            for word in array_words:
                for cell in row:
                    if word.lower() in cell.lower():
                        count = count + 1
                        temp_word.append(cell + ' > ' + word)
            if count == len(array_words):
                if row not in result_new:
                    result_new.append(row)
        temp_result = []
        for row in result_new:
            for word in array_words:
                for cell in range(1,4):
                    if word.lower() in row[cell].lower():
                        if len(word) != len(row[cell]):
                            if row not in temp_result:
                                temp_result.append(row)
        for temp in temp_result:
            result_new.remove(temp)
        return result_new
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return 'Error'


array = yp_find('вадим', True, '')
# array = yp_find('иван Гребенников', True, '')
for row in array:
    print(row)

# print(len(array))
