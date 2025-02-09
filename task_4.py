import random
import re


""" 1. create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be lettered,
dict's values should be a number (0-100),
example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
"""


DICT_NUM = random.randint(2, 10)


def create_list(dict_quantity, dict_length_scope=(2, 5), number_scope=(0, 100)):
    custom_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result_list = []

    for i in range(dict_quantity):
        member_dict = {}
        for j in range(random.randint(dict_length_scope[0], dict_length_scope[1])):
            member_dict[random.choice(custom_alphabet)] = random.randint(number_scope[0], number_scope[1])
        result_list.append(member_dict)

    return result_list


LIST = create_list(DICT_NUM)


""" 2. get previously generated list of dicts and create one common dict:
if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""


def list_to_raw_dict(raw_list):
    raw_dict = {}
    for i in raw_list:
        for key, value in i.items():
            if key in raw_dict:
                if value > raw_dict[key][0]:
                    raw_dict[key] = [value, "_" + str(raw_list.index(i) + 1), True]
                else:
                    raw_dict[key][2] = True
            else:
                raw_dict[key] = [value, "_" + str(raw_list.index(i) + 1), False]

    return raw_dict


def list_to_dict(raw_list):
    final_dict = {}
    raw_dictionary = list_to_raw_dict(raw_list)
    for keys, values in raw_dictionary.items():
        if values[2]:
            new_key = keys + values[1]
            final_dict[new_key] = values[0]
        else:
            final_dict[keys] = values[0]

    return final_dict


if __name__ == '__main__':
    print(LIST)
    print(list_to_dict(LIST))


# task 3


text = """ tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87. """


def text_to_list(string):

    # make easy transformations at the beginning
    b = string.lower().split(".")
    b.pop()  # delete empty string generated from last "." split

    # make correct text structure
    for i in range(len(b) - 1):
        b[i] = b[i].strip().capitalize()

    return b


def add_sentence(string):
    text_list = text_to_list(string)
    # make correct text structure
    last_sentence_lst = []
    for i in range(len(text_list) - 1):
        text_list[i] = text_list[i].strip().capitalize()
        last_sentence_lst.append(text_list[i].split()[-1])

    # create sentence with last words
    text_list.append(" ".join(last_sentence_lst).capitalize())

    # construct final text
    final_text = ". ".join(text_list)
    return final_text


def correct_iz(string):
    corrected_text = re.sub(r'(?<=\s|\w)iz(?=\s|\w)', 'is', string)
    return corrected_text


def count_whitespaces(string):
    whitespace_count = len(re.findall(r'\s', string))
    return whitespace_count


if __name__ == '__main__':
    print(correct_iz(add_sentence(text)))
    print(count_whitespaces(text))
