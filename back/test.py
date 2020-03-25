import itertools
import time
from back.sql import yp

start_time = time.time()
text = 'менеджер отдела продаж'.split(' ')
text = 'системный администратор гусаров'.split(' ')

unit_depart = yp.unit_depart()
depart_pos = yp.depart_pos()
city_address = yp.city_address()
brand = yp.get_brand()

print(text)

word_comb = []

for l in range(1, len(text)+1):
    word_comb = word_comb + list(map(" ".join, itertools.combinations(text, l)))
word_comb = list(reversed(word_comb))

print(word_comb)
for word in word_comb:
    for value in depart_pos.values():
        print(value)
        value = list(map(lambda x:x.lower(),value))
        # if word.lower() in value:
            # print(value)



<<<<<<< HEAD

# array = yp_find('Менеджер отдела продаж', True, '')
# for row in array:
#     print(row)


import keyring

print(keyring.get_password('postgresql', 'postgres'))
print(keyring.get_password('postgresql', 'user'))
print(keyring.get_password('postgresql', 'host'))
print(keyring.get_password('postgresql', 'db_name'))

print(keyring.get_password('yandex_tracker', 'token'))
print(keyring.get_password('yandex_tracker', 'org_id'))
=======
print("--- %s seconds ---" % (time.time() - start_time))
>>>>>>> ca9c4f4107accf44502b200e936dd472fd87773c
