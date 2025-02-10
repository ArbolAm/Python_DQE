import csv
import re


with open('../task_5/news_feed.txt', 'r') as f:
    raw_text = f.read()
    f.close()


def letter_count(text):
    letters = re.findall(r'[a-zA-Z]', text)
    total_count = len(letters)
    letter_dict = {}

    for letter in letters:
        lower_letter = letter.lower()

        if lower_letter not in letter_dict:
            letter_dict[lower_letter] = {'count_all': 0, 'count_uppercase': 0}
        else:
            letter_dict[lower_letter]['count_all'] += 1

        if letter.isupper():
            letter_dict[lower_letter]['count_uppercase'] += 1

    for key in letter_dict.keys():
        letter_dict[key]['percentage'] = round(((letter_dict[key]['count_all']/total_count) * 100), 2)

    return letter_dict


def word_count(text):
    word_count_dict = {}
    words = re.findall(r'[a-zA-Z]+', text.lower())
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    return word_count_dict


def publish_csv():
    pass
