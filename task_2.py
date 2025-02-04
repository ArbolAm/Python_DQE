import random
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


""" 1. create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be lettered,
dict's values should be a number (0-100),
example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
"""


dict_num = random.randint(2, 10)
LIST = []

for i in range(dict_num):
    DICT = {}
    dict_len = random.randint(2, 5)
    for j in range(dict_len):
        DICT[random.choice(ALPHABET)] = random.randint(0, 100)
    LIST.append(DICT)

print(LIST)


""" 2. get previously generated list of dicts and create one common dict:
if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""


RAW_DICT = {}
for i in LIST:
    for key, value in i.items():
        if key in RAW_DICT:
            if value > RAW_DICT[key][0]:
                RAW_DICT[key] = [value, "_" + str(LIST.index(i) + 1), True]
            else:
                RAW_DICT[key][2] = True
        else:
            RAW_DICT[key] = [value, "_" + str(LIST.index(i) + 1), False]

print(RAW_DICT)


FINAL_DICT = {}
for keys, values in RAW_DICT.items():
    if values[2]:
        new_key = keys + values[1]
        FINAL_DICT[new_key] = values[0]
    else:
        FINAL_DICT[keys] = values[0]

print(FINAL_DICT)
