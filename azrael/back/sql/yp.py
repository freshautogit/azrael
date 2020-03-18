from back import config
import psycopg2

dbname = config.sql_database
user = config.sql_user
password = config.sql_password
host = config.sql_host


def yp_find(request, full, query_sql):
    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)

    result_words = []
    if full:
        concat = 'id, surname, name, middlename, city, bdate, position, depart, unit, mobile, workphone, email, ' \
                 'address, company '
        concat_id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    else:
        concat = 'id, surname, name, city, position, depart, unit, mobile, workphone, email, address, company'
        concat_id = [0, 1, 2, 4, 6, 13, 7, 8, 9, 10, 11, 12]
    print(request)
    if request is not None:
        request = request.strip()
        array_words = request.split(' ')
    try:
        with connection.cursor() as cursor:

            for word in array_words:
                sql = "select * from phonebook where concat(" + concat + ") ~* '" + word + "' "
                sql = sql + query_sql + " and fired = 0;"

                cursor.execute(sql)
                temp_result = ''
                for row in cursor:
                    for temp in concat_id:
                        temp_result += str(row[temp]).strip() + ';'
                    temp_result += '\n'
            if temp_result[len(temp_result) - 1:len(temp_result)] == '\n':
                temp_result = temp_result[:len(temp_result) - 1] + temp_result[len(temp_result) + 1:]

            for temp in temp_result.split('\n'):
                count = 0
                for tempWord in array_words:
                    if tempWord.lower() in temp.lower():
                        count += 1
                    if count == len(array_words):
                        temp = temp[:len(temp) - 1]
                        result_words.append(temp.split(';'))
        connection.close()
        return result_words
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
    id = get_last_id() + 1
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

        print(query)
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
            print(query)
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

        print(query)

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
                result.append(row['surname'])
                result.append(row['name'])
                result.append(row['middlename'])
                result.append(row['city'])
                result.append(row['bdate'].strftime("%Y-%m-%d"))
                result.append(row['position'])
                result.append(row['depart'])
                result.append(row['mobile'])
                result.append(row['workphone'])
                result.append(row['email'])
                result.append(row['address'])
                result.append(row['company'])
                result.append(row['unit'])

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


def get_last_id():
    result = 0
    connection = psycopg2.connect(dbname=dbname, user=user,
                                  password=password, host=host)
    try:
        with connection.cursor() as cursor:
            sql = "select * from phonebook"
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
