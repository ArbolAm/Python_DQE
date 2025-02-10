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
            letter_dict[lower_letter] = {'count_all': 1, 'count_uppercase': 0}
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


def word_publish_csv(word_dict):
    with open('published/words.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Word', 'Count'])

        for key, value in word_dict.items():
            writer.writerow([key, value])

    print('file updated/ published')


def letter_publish_csv(letter_dict):
    with open('published/letters.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['letter', 'count_all', 'count_uppercase', 'percentage'])

        for key, value in letter_dict.items():
            writer.writerow([key, value['count_all'], value['count_uppercase'], value['percentage']])

    print('file updated/ published')


word_publish_csv(word_count(raw_text))
letter_publish_csv(letter_count(raw_text))
