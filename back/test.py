from back.sql import yp

unit_depart = yp.unit_depart()
sorted_unit_depart = {}
for k in sorted(unit_depart.keys()):
    sorted_unit_depart.update({k: sorted(unit_depart[k])})
print(sorted_unit_depart)
