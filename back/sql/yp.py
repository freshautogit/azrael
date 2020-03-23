from back import config
import psycopg2

dbname = config.sql_database
user = config.sql_user
password = config.sql_password
host = config.sql_host


def adding_in_dropdown_list(request):
    if request.GET.get('newCity') is not None:
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
    # elif request.GET.get('new_address') is not None:
    #     new_address = request.GET.get('new_address')
    #     connection = psycopg2.connect(dbname=dbname, user=user,
    #                                   password=password, host=host)
    #     with connection.cursor() as cursor:
    #         query = "SELECT id FROM city_address WHERE address ~* '{0}'".format(new_address)
    #         cursor.execute(query)
    #         id_in_db = 0
    #         for row in cursor:
    #             id_in_db = row[0]
    #         if id_in_db == 0:
    #             query = "select address from city_address where city='{0}';".format(request.GET.get('city'))
    #             cursor.execute(query)
    #             for row in cursor:
    #                 old_address = row[0]
    #             address = old_address + '\n' + new_address
    #             query = "update city_address set address = '{0}' where city='{1}'".format(address,
    #                                                                                       request.GET.get('city'))
    #             cursor.execute(query)
    #             connection.commit()
    #             connection.close()
    #             return True
    #         else:
    #             connection.close()
    #         return False
    # elif request.GET.get('new_unit') is not None:
    #     new_unit = request.GET.get('new_unit')
    #     connection = psycopg2.connect(dbname=dbname, user=user,
    #                                   password=password, host=host)
    #     with connection.cursor() as cursor:
    #         query = "SELECT id FROM unit_depart WHERE unit ~* '{0}'".format(new_unit)
    #         cursor.execute(query)
    #         id_in_db = 0
    #         for row in cursor:
    #             id_in_db = row[0]
    #         if id_in_db == 0:
    #             query = "INSERT INTO unit_depart (unit) VALUES ('{0}');".format(new_unit)
    #             cursor.execute(query)
    #             connection.commit()
    #             connection.close()
    #             return True
    #         else:
    #             connection.close()
    #         return False
    # elif request.GET.get('new_depart') is not None:
    #     new_depart = request.GET.get('new_depart')
    #     connection = psycopg2.connect(dbname=dbname, user=user,
    #                                   password=password, host=host)
    #     with connection.cursor() as cursor:
    #         query = "select id from depart_pos where depart ~* '{1}'".format(new_depart)
    #         cursor.execute(query)
    #         id_in_db = 0
    #         for row in cursor:
    #             id_in_db = row[0]
    #         if id_in_db == 0:
    #             query = "select depart from unit_depart where unit='{0}';".format(request.GET.get('unit'))
    #             cursor.execute(query)
    #             for row in cursor:
    #                 old_depart = row[0]
    #             depart = old_depart + '\n' + new_depart
    #             query = "update unit_depart set depart = '{0}' where unit='{1}'".format(depart, request.GET.get('unit'))
    #             cursor.execute(query)
    #             query = "INSERT INTO depart_pos (depart) VALUES ('{0}');".format(new_depart)
    #             cursor.execute(query)
    #             connection.commit()
    #             connection.close()
    #             return True
    #         else:
    #             query = "select depart from unit_depart where unit='{0}';".format(request.GET.get('unit'))
    #             cursor.execute(query)
    #             for row in cursor:
    #                 old_depart = row[0]
    #             depart = old_depart + '\n' + new_depart
    #             query = "update unit_depart set depart = '{0}' where unit='{1}'".format(depart, request.GET.get('unit'))
    #             cursor.execute(query)
    #             connection.commit()
    #             connection.close()
    #             return True
    # elif request.GET.get('new_position') is not None:
    #     new_position = request.GET.get('new_position')
    #     connection = psycopg2.connect(dbname=dbname, user=user,
    #                                   password=password, host=host)
    #     with connection.cursor() as cursor:
    #         query = "SELECT id FROM depart_pos WHERE pos ~* '{0}'".format(new_position)
    #         cursor.execute(query)
    #         id_in_db = 0
    #         for row in cursor:
    #             id_in_db = row[0]
    #         if id_in_db == 0:
    #             query = "select pos from depart_pos depart ='{0}';".format(request.GET.get('depart'))
    #             cursor.execute(query)
    #             for row in cursor:
    #                 old_position = row[0]
    #             position = old_position + '\n' + new_position
    #             query = "update depart_pos set pos = '{0}' where depart = '{1}'".format(position,
    #                                                                                     request.GET.get('depart'))
    #             cursor.execute(query)
    #             connection.commit()
    #             connection.close()
    #             return True
    #         else:
    #             connection.close()
    #         return False
    # elif request.GET.get('new_brand') is not None:
    #     new_brand = request.GET.get('new_brand')
    #     connection = psycopg2.connect(dbname=dbname, user=user,
    #                                   password=password, host=host)
    #     with connection.cursor() as cursor:
    #         query = "SELECT id FROM company WHERE company.company ~* '{0}'".format(new_brand)
    #         cursor.execute(query)
    #         id_in_db = 0
    #         for row in cursor:
    #             id_in_db = row[0]
    #         if id_in_db == 0:
    #             query = "INSERT INTO company (company) VALUES ('{0}');".format(new_brand)
    #             cursor.execute(query)
    #             connection.commit()
    #             connection.close()
    #             return True
    #         else:
    #             connection.close()
    #         return False


# def yp_find(request, full, query_sql):
#     connection = psycopg2.connect(dbname=dbname, user=user,
#                                   password=password, host=host)
#
#     result_words = []
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
#
#                 cursor.execute(sql)
#                 temp_result = ''
#                 for row in cursor:
#                     for temp in concat_id:
#                         temp_result += str(row[temp]).strip() + ';'
#                     temp_result += '\n'
#             if temp_result[len(temp_result) - 1:len(temp_result)] == '\n':
#                 temp_result = temp_result[:len(temp_result) - 1] + temp_result[len(temp_result) + 1:]
#
#             for temp in temp_result.split('\n'):
#                 count = 0
#                 for tempWord in array_words:
#                     if tempWord.lower() in temp.lower():
#                         count += 1
#                 if count == len(array_words):
#                     temp = temp[:len(temp) - 1]
#                     result_words.append(temp.split(';'))
#         connection.close()
#         return result_words
#     except Exception as e:
#         print("[!] ", e)
#         connection.close()
#         return 'Error'

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
                result.update({row[1]: row[2].split('\\n')})

        connection.close()
        return result
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
                result.update({row[1]: row[2].split('\\n')})

        connection.close()
        return result
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
                result.update({row[1]: row[2].split('\\n')})

        connection.close()
        return result
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
    depart = request.GET.get('office')
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
    address = request.GET.get('address')
    company = request.GET.get('company')
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
