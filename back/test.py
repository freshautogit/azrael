from back.sql import yp

unit_depart = yp.unit_depart()
sorted_unit_depart = {}
for k in sorted(unit_depart.keys()):
    sorted_unit_depart.update({k: sorted(unit_depart[k])})

result = yp.yp_find('Менеджер', True, '')
result = result.sort(key=lambda x: x[0][1])
# for row in result:
#     print(row)