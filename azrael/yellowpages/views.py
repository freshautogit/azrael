from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from back.sql import yp
from django.http import JsonResponse

# city = yp.unit('city')
# address = yp.unit('address')
# company = yp.unit('company')
# unit = yp.unit('unit')
# depart = yp.unit('depart')
# position = yp.unit('position')

#########################################
#TODO Доделать списки, вот две переменные
unit_depart = yp.unit_depart()
depart_pos = yp.depart_pos()
city_address = yp.city_address()
brand = yp.get_brand()
########################################

def editUser(request):
    result = yp.get_user(request)

    key = request.GET.get('key')
    print(key)
    return render(request, 'adduser.html', {'result': result})


def saveUser(request):
    yp.add_user(request)
    query = request.GET.get('secondName')
    return getHeaders(request)


def delUser(request):
    yp.del_yp(request)
    return render(request, 'deleted.html')


def addUser(request):
    units = yp.unit_depart().keys()
    cities = yp.city_address().keys()
    brands = brand
    return render(request, 'adduser.html', {'cities': cities, 'units': units, 'brands': brands})
#                  {'depart': depart, 'city': city, 'unit': unit, 'address': address, 'company': company,
 #                  'position': position})


def indexYP(request):
    testHttpRequest(request)
    units = yp.unit_depart().keys()
    cities = yp.city_address().keys()
    brands = brand
    return render(request, 'index.html', {'cities': cities, 'units': units, 'brands': brands})
                 # {'depart': depart, 'city': city, 'unit': unit, 'address': address, 'company': company, 'unitAndDepart' : unitAndDepart, 'departAndPos' : departAndPos})


# Если пользователь не авторизирован
def regular_search(request):
    headTemp = yp.headers(False)
    key = request.GET.get('key')
    units = yp.unit_depart().keys()
    cities = yp.city_address().keys()
    brands = brand

    if key is not None:
        query = request.GET.get('secondName') + str(' ') + request.GET.get('name')
        yp.edit_user(request, False)
        # result = yp.ypFind(str(query), False, ' ')
        result = yp.yp_find(str(query), False, ' ')

    else:
        query, result = searchResult(request)

    return render(request, 'results.html', {'result': result, 'query': query, 'key': key, 'headTemp': headTemp, 'cities': cities, 'units': units, 'brands': brands})


# Если пользователь авторизирован как менежер
@permission_required('yellowpages.can_view')
def manager_search(request):
    headTemp = yp.headers(False)

    query, result = searchResult(request)

    return render(request, 'results.html', {'result': result, 'query': query, 'headTemp': headTemp})


def searchResult(request):
    query = request.GET.get('searchRequest')
    result = yp.yp_find(str(query), False, querySql(request))
    return query, result


# Если пользователь авторизирован как супервайзер
@login_required(redirect_field_name='/yp')
def search(request):
    if request.GET.get('key') is not None:
        yp.edit_user(request, False)

    return getHeaders(request)


def querySql(request):
    query_sql = ''
    if request.GET.get('city') is not None and request.GET.get('city') != 'None':
        query_sql += 'and city = \'' + str(request.GET.get('city')) + '\' '

    if request.GET.get('addr') is not None and request.GET.get('addr') != 'None':
        query_sql += 'and address = \'' + str(request.GET.get('addr')) + '\' '

    if request.GET.get('brand') is not None and request.GET.get('brand') != 'None':
        query_sql += 'and company = \'' + str(request.GET.get('brand')) + '\' '

    if request.GET.get('office') is not None and request.GET.get('office') != 'None':
        query_sql += 'and unit = \'' + str(request.GET.get('office')) + '\' '

    if request.GET.get('position') is not None and request.GET.get('position') != 'None':
        query_sql += 'and depart = \'' + str(request.GET.get('position')) + '\' '

    return query_sql


def getHeaders(request):
    headTemp = yp.headers(True)
    query = request.GET.get('searchRequest')
    result = yp.yp_find(query, True, querySql(request))
    return render(request, 'results.html', {'result': result, 'query': query, 'headTemp': headTemp})

def dropdown_request(request):
    request_city = request.GET.get('city')
    request_unit = request.GET.get('unit')
    request_position = request.GET.get('position')

    if (request_city == None) and (request_unit == None) and (request_position == None):
        units = yp.unit_depart().keys()
        cities = yp.city_address().keys()
        return render(request, 'test.html', {'units': units, 'cities': cities})

    elif request_city != None:
        if yp.city_address().get(request_city) == None:
            response = "None"
        else:
            response = yp.city_address().get(request_city)
        return JsonResponse({'response': response})

    elif request_unit != None:
        if yp.unit_depart().get(request_unit) == None:
            response = "None"
        else:
            response = yp.unit_depart().get(request_unit)
        return JsonResponse({'response': response})

    elif request_position != None:
        if yp.depart_pos().get(request_position) == None:
            response = "None"
        else:
            response = yp.depart_pos().get(request_position)
        return JsonResponse({'response': response})
