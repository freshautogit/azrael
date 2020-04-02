import itertools

from back import config
from back.sql import yp
import psycopg2

dbname = config.sql_database
user = config.sql_user
password = config.sql_password
host = config.sql_host

def yp_find(request, full, query_sql):

    if request == '' and query_sql == '':
        return False

    text = request.lower().split(' ')
    unit_dep = yp.unit_depart()
    depart_position = yp.depart_pos()

    word_comb = []

    for length in range(0, len(text) + 1):
        word_comb = word_comb + list(map(" ".join, itertools.combinations(text, length)))
    word_comb = list(reversed(word_comb))

    position = []
    for word in word_comb:
        for value in depart_position.values():
            value = list(map(lambda x: x.lower(), value))
            if word.lower() in value:
                position.append(word)
    depart = []
    for word in word_comb:
        for value in depart_position.keys():
            value = value.lower()
            if word.lower() in value:
                depart.append(value)
    unit = []
    for word in word_comb:
        for value in unit_dep.keys():
            value = value.lower()
            if word.lower() in value:
                unit.append(value)

    temp_word = word_comb.copy()
    result_pos = []
    for pos in position:
        for word in temp_word:
            if word == pos:
                result_pos.append(pos)
                temp_word.remove(word)

    temp_word = word_comb.copy()
    result_dep = []
    for dep in depart:
        for word in temp_word:
            if word == dep:
                result_dep.append(dep)
                temp_word.remove(word)

    temp_word = word_comb.copy()
    result_un = []
    for un in unit:
        for word in temp_word:
            if word == un:
                result_un.append(un)
                temp_word.remove(word)

    for pos in result_pos:
        for word_pos in pos.split(' '):
            if word_pos in text:
                text.remove(word_pos)

    for dep in depart_position:
        for word_dep in dep.split(' '):
            if word_dep in text:
                text.remove(word_dep)

    for un in result_un:
        for word_un in un.split(' '):
            if word_un in text:
                text.remove(word_un)

    if full:
        concat = 'id, surname, name, middlename, city, bdate, position, depart, unit, mobile, workphone, email, address, company '
        concat_id = [0, 1, 2, 3, 4, 5, 6, 7, 13, 8, 9, 10, 11, 12]
    else:
        concat = 'id, surname, name, city, position, depart, unit, mobile, workphone, email, address, company'
        concat_id = [0, 1, 2, 4, 6, 13, 7, 8, 9, 10, 11, 12]

    result_query_sql = []
    text.append('')
    result_un.append('')
    result_dep.append('')
    result_pos.append('')
    for word in text:
        for unit in result_un:
            if unit == '':
                query_sql_unit = ""
            else:
                query_sql_unit = " and unit ~* '{0}'".format(unit)
            for depart in result_dep:
                if depart == '':
                    query_sql_depart = ""
                else:
                    query_sql_depart = " and depart ~* '{0}'".format(depart)
                for position in result_pos:
                    if position == '':
                        query_sql_position = ""
                    else:
                        query_sql_position = " and position ~* '{0}'".format(position)
                    sql = "select * from phonebook where concat(" + concat + ") ~* '" + word + "' "
                    sql = sql + query_sql_unit + query_sql_depart + query_sql_position + query_sql + " and fired = 0 ORDER by surname;"
                    result_query_sql.append(sql)

    try:
        result_query_sql.remove(
            "select * from phonebook where concat(id, surname, name, middlename, city, bdate, mobile, workphone, email, address, company ) ~* ''  and fired = 0 ORDER by surname;")
    except:
        pass

    try:
        result_query_sql.remove(
            "select * from phonebook where concat(id, surname, name, city, position, depart, unit, mobile, workphone, email, address, company) ~* ''  and fired = 0 ORDER by surname;")
    except:
        pass

    try:
        result_query_sql.remove("select * from phonebook where concat(id, surname, name, middlename, city, bdate, position, depart, unit, mobile, workphone, email, address, company ) ~* ''  and fired = 0 ORDER by surname;")
    except:
        pass
    result = []

    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)
    try:
        with connection.cursor() as cursor:

            for sql in result_query_sql:
                print(sql)
                cursor.execute(sql)
                for row in cursor:
                    row_result = ''
                    for id in concat_id:
                        row_result += str(row[id]).strip() + ';'
                    if row_result.split(';') not in result:
                        result.append(row_result.split(';'))
                if len(result) != 0:
                    break
    except Exception as e:
        print("[!] ", e)
        connection.close()

    temp_result = []
    text.remove('')
    for row in result:
        for word in text:
            for cell in range(1, 4):
                if word.lower() in row[cell].lower():
                    if len(word) != len(row[cell]):
                        if row not in temp_result:
                            temp_result.append(row)
    for temp in temp_result:
        result.remove(temp)
    return result



print(yp_find('Ушакова', True, ''))