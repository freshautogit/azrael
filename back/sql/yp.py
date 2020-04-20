import itertools

from back import config
import psycopg2

dbname = config.sql_database
user = config.sql_user
password = config.sql_password
host = config.sql_host


def adding_in_dropdown_list(request):
    if request.GET.get('newCity') is not None and request.GET.get('newCity') != '':
        new_city = request.GET.get('newCity')
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        try:
            with connection.cursor() as cursor:
                query = "SELECT id FROM city_address WHERE city ~* '{0}'".format(new_city)
                cursor.execute(query)
                id_in_db = 0
                for row in cursor:
                    id_in_db = row[0]
                if id_in_db == 0:
                    last_id = get_last_id('city_address') + 1
                    query = "INSERT INTO city_address (id, city) VALUES ({0}, '{1}');".format(last_id, new_city)
                    cursor.execute(query)
                    connection.commit()
                    connection.close()
                    return True
                else:
                    connection.close()
                    return False
        except Exception as e:
            print("[!] ", e)
            connection.close()
            return 'Error'
    elif request.GET.get('newAddress') is not None and request.GET.get('newAddress') != '':
        new_address = request.GET.get('newAddress')
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        with connection.cursor() as cursor:
            query = "SELECT id FROM city_address WHERE address ~* '{0}' and city='{1}'".format(new_address, request.GET.get('city'))
            cursor.execute(query)
            id_in_db = 0
            for row in cursor:
                id_in_db = row[0]
            if id_in_db == 0:
                query = "select address from city_address where city='{0}';".format(request.GET.get('city'))
                cursor.execute(query)
                old_address = None
                for row in cursor:
                    old_address = row[0]
                if old_address != None:
                    address = str(old_address) + '\\n' + str(new_address)
                else:
                    address = str(new_address)
                query = "update city_address set address = '{0}' where city='{1}'".format(address,
                                                                                          request.GET.get('city'))
                cursor.execute(query)
                connection.commit()
                connection.close()
                return True
            else:
                connection.close()
            return False
    elif request.GET.get('newUnit') is not None and request.GET.get('newUnit') != '':
        new_unit = request.GET.get('newUnit')
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        with connection.cursor() as cursor:
            query = "SELECT id FROM unit_depart WHERE unit ~* '{0}'".format(new_unit)
            cursor.execute(query)
            id_in_db = 0
            for row in cursor:
                id_in_db = row[0]
            if id_in_db == 0:
                last_id = get_last_id('unit_depart') + 1
                query = "INSERT INTO unit_depart (id, unit) VALUES ({0}, '{1}');".format(last_id, new_unit)
                cursor.execute(query)
                connection.commit()
                connection.close()
                return True
            else:
                connection.close()
            return False
    elif request.GET.get('newDepart') is not None and request.GET.get('newDepart') != '':
        new_depart = request.GET.get('newDepart')
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        with connection.cursor() as cursor:
            query = "select id from depart_pos where depart ~* '{0}'".format(new_depart)
            cursor.execute(query)
            id_in_db = 0
            for row in cursor:
                id_in_db = row[0]
            if id_in_db == 0:
                query = "select depart from unit_depart where unit='{0}';".format(request.GET.get('unit'))
                cursor.execute(query)
                for row in cursor:
                    old_depart = row[0]
                if old_depart != None:
                    depart = str(old_depart) + '\\n' + str(new_depart)
                else:
                    depart = str(new_depart)
                query = "update unit_depart set depart = '{0}' where unit='{1}'".format(depart, request.GET.get('unit'))
                cursor.execute(query)
                last_id = get_last_id('depart_pos') + 1
                query = "INSERT INTO depart_pos (id, depart) VALUES ({0}, '{1}');".format(last_id, new_depart)
                cursor.execute(query)
                connection.commit()
                connection.close()
                return True
            else:
                query = "select depart from unit_depart where unit='{0}';".format(request.GET.get('unit'))
                cursor.execute(query)
                for row in cursor:
                    old_depart = row[0]
                if old_depart != None:
                    depart = str(old_depart) + '\\n' + str(new_depart)
                else:
                    depart = str(new_depart)
                query = "update unit_depart set depart = '{0}' where unit='{1}'".format(depart, request.GET.get('unit'))
                cursor.execute(query)
                connection.commit()
                connection.close()
                return True
    elif request.GET.get('newPosition') is not None and request.GET.get('newPosition') != '':
        new_position = request.GET.get('newPosition')
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        with connection.cursor() as cursor:
            query = "SELECT id FROM depart_pos WHERE pos ~* '{0}'".format(new_position)
            cursor.execute(query)
            id_in_db = 0
            for row in cursor:
                id_in_db = row[0]
            if id_in_db == 0:
                query = "select pos from depart_pos where depart ='{0}';".format(request.GET.get('depart'))
                cursor.execute(query)
                for row in cursor:
                    old_position = row[0]
                if old_position != None:
                    position = str(old_position) + '\\n' + str(new_position)
                else:
                    position = str(new_position)
                query = "update depart_pos set pos = '{0}' where depart = '{1}'".format(position,
                                                                                        request.GET.get('depart'))
                cursor.execute(query)
                connection.commit()
                connection.close()
                return True
            else:
                connection.close()
            return False
    elif request.GET.get('newBrand') is not None and request.GET.get('newBrand') != '':
        new_brand = request.GET.get('newBrand')
        connection = psycopg2.connect(dbname=dbname, user=user,
                                      password=password, host=host)
        with connection.cursor() as cursor:
            query = "SELECT id FROM company WHERE company.company ~* '{0}'".format(new_brand)
            cursor.execute(query)
            id_in_db = 0
            for row in cursor:
                id_in_db = row[0]
            if id_in_db == 0:
                query = "INSERT INTO company (company) VALUES ('{0}');".format(new_brand)
                cursor.execute(query)
                connection.commit()
                connection.close()
                return True
            else:
                connection.close()
            return False


# def yp_find(request, full, query_sql):
#     connection = psycopg2.connect(dbname=dbname, user=user,
#                                   password=password, host=host)
#
#     result = []
#     result_new = []
#
#     if full:
#         concat = 'id, surname, name, middlename, city, bdate, position, depart, unit, mobile, workphone, email, ' \
#                  'address, company '
#         concat_id = [0, 1, 2, 3, 4, 5, 6, 7, 13, 8, 9, 10, 11, 12]
#     else:
#         concat = 'id, surname, name, city, position, depart, unit, mobile, workphone, email, address, company'
#         concat_id = [0, 1, 2, 4, 6, 13, 7, 8, 9, 10, 11, 12]
#     if request is not None:
#         request = request.strip()
#         array_words = request.split(' ')
#     try:
#         with connection.cursor() as cursor:
#
#             for word in array_words:
#                 sql = "select * from phonebook where concat(" + concat + ") ~* '" + word + "' "
#                 sql = sql + query_sql + " and fired = 0;"
#                 cursor.execute(sql)
#                 for row in cursor:
#                     row_result = ''
#                     for id in concat_id:
#                         row_result += str(row[id]).strip() + ';'
#                     result.append(row_result.split(';'))
#         connection.close()
#
#         for row in result:
#             count = 0
#             temp_word = []
#             for word in array_words:
#                 for cell in row:
#                     if word.lower() in cell.lower():
#                         count = count + 1
#                         temp_word.append(cell + ' > ' + word)
#             if count == len(array_words):
#                 if row not in result_new:
#                     result_new.append(row)
#         temp_result = []
#         for row in result_new:
#             for word in array_words:
#                 for cell in range(1,4):
#                     if word.lower() in row[cell].lower():
#                         if len(word) != len(row[cell]):
#                             if row not in temp_result:
#                                 temp_result.append(row)
#         for temp in temp_result:
#             result_new.remove(temp)
#         return result_new
#     except Exception as e:
#         print("[!] ", e)
#         connection.close()
#         return 'Error'

def get_brand():
    result = []
    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)

    try:
        with connection.cursor() as cursor:
            sql = "select * from company"
            cursor.execute(sql)

            for row in cursor:
                result.append(row[1])

        connection.close()
        return result
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return result


def unit_depart():
    result = {}
    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)

    try:
        with connection.cursor() as cursor:
            sql = "select * from unit_depart"
            cursor.execute(sql)

            for row in cursor:
                if "\\n" in str(row[2]):
                    result.update({row[1]: row[2].split('\\n')})
                else:
                    temp_array = [row[2]]
                    result.update({row[1]: temp_array})
        connection.close()
        sorted_result = {}
        for k in sorted(result.keys()):
            sorted_result.update({k: sorted(result[k])})
        return sorted_result
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return result


def depart_pos():
    result = {}
    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)
    try:
        with connection.cursor() as cursor:
            sql = "select * from depart_pos"
            cursor.execute(sql)

            for row in cursor:
                if "\\n" in str(row[2]):
                    result.update({row[1]: row[2].split('\\n')})
                else:
                    temp_array = [row[2]]
                    result.update({row[1]: temp_array})

        connection.close()
        sorted_result = {}
        for k in sorted(result.keys()):
            sorted_result.update({k: sorted(result[k])})
        return sorted_result
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return result


def city_address():
    result = {}
    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)

    try:
        with connection.cursor() as cursor:
            sql = "select * from city_address"
            cursor.execute(sql)

            for row in cursor:
                if "\\n" in str(row[2]):
                    result.update({row[1]: row[2].split('\\n')})
                else:
                    temp_array = [row[2]]
                    result.update({row[1]: temp_array})

        connection.close()
        sorted_result = {}
        for k in sorted(result.keys()):
            sorted_result.update({k: sorted(result[k])})
        return sorted_result
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return result


def add_user(request):
    id = get_last_id('phonebook') + 1
    name = request.GET.get('name')
    secondname = request.GET.get('secondName')
    middlename = request.GET.get('middlename')
    email = request.GET.get('email')
    mobile = request.GET.get('mobile')
    tel = request.GET.get('tel')
    city = request.GET.get('city')
    address = request.GET.get('addr')
    company = request.GET.get('brand')
    unit_in_yp = request.GET.get('unit')
    depart = request.GET.get('depart')
    position = request.GET.get('position')
    bdate = request.GET.get('bdate')

    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)
    with connection.cursor() as cursor:
        query = "SELECT id FROM phonebook WHERE name = '{0}' and surname = '{1}' and email = '{2}'".format(name,
                                                                                                           secondname,
                                                                                                           email)

        cursor.execute(query)
        id_in_yp = 0
        for row in cursor:
            id_in_yp = row[0]

        if id_in_yp == 0:

            query = "INSERT INTO phonebook (id, surname, name, middlename, city, bdate, position, depart, mobile, " \
                    "workphone, email, address, company, unit) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', " \
                    "'{6}', '{7}', '{8}', {9}, '{10}', '{11}', '{12}', '{13}');".format(
                id, secondname, name, middlename, city, bdate, position, depart, mobile, tel, email, address, company,
                unit_in_yp)

            cursor.execute(query)
            connection.commit()
            connection.close()

            return True
        else:
            connection.close()
            return False


def edit_user(request):
    key = request.GET.get('key')
    name = request.GET.get('name')
    secondname = request.GET.get('secondName')
    middlename = request.GET.get('middlename')
    email = request.GET.get('email')
    mobile = request.GET.get('mobile')
    tel = request.GET.get('tel')
    city = request.GET.get('city')
    address = request.GET.get('addr')
    company = request.GET.get('brand')
    unit_in_yp = request.GET.get('unit')
    depart = request.GET.get('depart')
    position = request.GET.get('position')
    bdate = request.GET.get('bdate')

    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)

    with connection.cursor() as cursor:
        query = "UPDATE phonebook SET surname = '{0}', name = '{1}', middlename = '{2}', city = '{3}', " \
                "bdate = '{4}', position = '{5}', depart = '{6}', mobile = '{7}', workphone = '{8}', " \
                "email = '{9}', address = '{10}', company = '{11}', unit = '{12}' WHERE id = {13}".format(
            secondname, name, middlename, city, bdate, position, depart, mobile, tel, email, address, company,
            unit_in_yp,
            key)

        cursor.execute(query)
        connection.commit()
        connection.close()


def get_user(request):
    key = request.GET.get('key')

    result = []

    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)
    try:
        with connection.cursor() as cursor:
            sql = "select * from phonebook WHERE id = {0}".format(key)
            cursor.execute(sql)

            for row in cursor:
                result.append(row[1])
                result.append(row[2])
                result.append(row[3])
                result.append(row[4])
                result.append(row[5].strftime("%Y-%m-%d"))
                result.append(row[6])
                result.append(row[7])
                result.append(row[8])
                result.append(row[9])
                result.append(row[10])
                result.append(row[11])
                result.append(row[12])
                result.append(row[13])

        connection.close()
        return result
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return result


def del_yp(request):
    key = request.GET.get('key')

    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE phonebook SET fired=1 WHERE id = {0}".format(key)
            cursor.execute(sql)
            connection.commit()

        connection.close()
        return True
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return False


def headers(full):
    if full:
        return ['Фамилия', 'Имя', 'Отчество', 'Город', 'Дата рождения', 'Должность', 'Подразделение', 'Отдел/Служба',
                'Мобильный', 'Внутренний', 'Эл.адрес', 'Адрес', 'Бренд']
    else:
        return ['Фамилия', 'Имя', 'Город', 'Должность', 'Подразделение', 'Отдел/Служба', 'Мобильный', 'Внутренний',
                'Эл.адрес', 'Адрес', 'Бренд']


def get_last_id(table):
    result = 0
    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)
    try:
        with connection.cursor() as cursor:
            sql = "select * from {0}".format(table)
            cursor.execute(sql)

            for row in cursor:
                if row[0] > result:
                    result = row[0]

        connection.close()
        return result
    except Exception as e:
        print("[!] ", e)
        connection.close()
        return result


def yp_find(request, full, query_sql):

    if request == '' and query_sql == '':
        return False

    text = request.lower().split(' ')
    unit_dep = unit_depart()
    depart_position = depart_pos()

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
