from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from back.sql import yp
from django.http import JsonResponse

#########################################
# TODO Доделать списки, вот две переменные
unit_depart = yp.unit_depart()
depart_pos = yp.depart_pos()
city_address = yp.city_address()
brand = yp.get_brand()


########################################

def edit_user(request):
    result = yp.get_user(request)
    key = request.GET.get('key')
    return render(request, 'add_user.html', {'result': result, 'key': key})


def save_user(request):
    yp.add_user(request)
    return get_headers(request, True)


def del_user(request):
    yp.del_yp(request)
    return render(request, 'deleted.html')


def add_user(request):
    units = yp.unit_depart().keys()
    cities = yp.city_address().keys()
    brands = brand
    return render(request, 'add_user.html', {'cities': cities, 'units': units, 'brands': brands})


def add_info(request):
    if request.GET.get('newCity') is not None:
        print(yp.adding_in_dropdown_list(request))
        units = yp.unit_depart().keys()
        cities = yp.city_address().keys()
        brands = yp.get_brand()
    else:
        units = yp.unit_depart().keys()
        cities = yp.city_address().keys()
        brands = yp.get_brand()
    return render(request, 'add_info.html', {'cities': cities, 'units': units, 'brands': brands})


def index_yp(request):
    dropdown_request(request)
    units = yp.unit_depart().keys()
    cities = yp.city_address().keys()
    brands = brand
    return render(request, 'index.html', {'cities': cities, 'units': units, 'brands': brands})


# Если пользователь не авторизирован
def regular_search(request):
    head_temp = yp.headers(False)
    key = request.GET.get('key')
    units = yp.unit_depart().keys()
    cities = yp.city_address().keys()
    brands = brand

    if key is not None:
        query = request.GET.get('secondName') + str(' ') + request.GET.get('name')
        yp.edit_user(request)
        result = yp.yp_find(str(query), False, ' ')

    else:
        query, result = search_result(request)

    return render(request, 'results.html',
                  {'result': result, 'query': query, 'key': key, 'headTemp': head_temp, 'cities': cities,
                   'units': units,
                   'brands': brands})


# Если пользователь авторизирован как менежер
@permission_required('yellowpages.can_view')
def manager_search(request):
    head_temp = yp.headers(False)

    query, result = search_result(request)

    return render(request, 'results.html', {'result': result, 'query': query, 'headTemp': head_temp})


def search_result(request):
    query = request.GET.get('searchRequest')
    result = yp.yp_find(str(query), False, query_sql(request))
    return query, result


# Если пользователь авторизирован как супервайзер
@login_required(redirect_field_name='/yp')
def search(request):
    if request.GET.get('key') is not None:
        yp.edit_user(request)

    return get_headers(request, False)


def query_sql(request):
    query = ''
    if request.GET.get('city') is not None and request.GET.get('city') != 'None':
        query += 'and city = \'' + str(request.GET.get('city')) + '\' '

    if request.GET.get('addr') is not None and request.GET.get('addr') != 'None':
        query += 'and address = \'' + str(request.GET.get('addr')) + '\' '

    if request.GET.get('brand') is not None and request.GET.get('brand') != 'None':
        query += 'and company = \'' + str(request.GET.get('brand')) + '\' '

    if request.GET.get('unit') is not None and request.GET.get('unit') != 'None':
        query += 'and unit = \'' + str(request.GET.get('unit')) + '\' '

    if request.GET.get('office') is not None and request.GET.get('office') != 'None':
        query += 'and depart = \'' + str(request.GET.get('office')) + '\' '

    return query


def get_headers(request, add):
    head_temp = yp.headers(True)
    if add:
        query = request.GET.get('email')
    else:
        query = request.GET.get('searchRequest')
    query_sql_temp = query_sql(request)
    result = yp.yp_find(query, True, query_sql_temp)
    return render(request, 'results.html', {'result': result, 'query': query, 'headTemp': head_temp})


def dropdown_request(request):
    request_city = request.GET.get('city')
    request_unit = request.GET.get('unit')
    request_position = request.GET.get('position')

    if (request_city is None) and (request_unit is None) and (request_position is None):
        units = yp.unit_depart().keys()
        cities = yp.city_address().keys()
        return render(request, 'test.html', {'units': units, 'cities': cities})

    elif request_city is not None:
        if yp.city_address().get(request_city) is None:
            response = "None"
        else:
            response = yp.city_address().get(request_city)
        return JsonResponse({'response': response})

    elif request_unit is not None:
        if yp.unit_depart().get(request_unit) is None:
            response = "None"
        else:
            response = yp.unit_depart().get(request_unit)
            response_position = yp.depart_pos().get(response[0])
        return JsonResponse({'response': response, 'response_position': response_position})

    elif request_position is not None:
        if yp.depart_pos().get(request_position) is None:
            response = "None"
        else:
            response = yp.depart_pos().get(request_position)
        return JsonResponse({'response': response})
