import json
import sys

sys.path.insert(0, 'C:\\Users\\amiran_arbolishvili\\PycharmProjects\\python_DQE\\Python_DQE')
sys.path.insert(1, 'C:\\Users\\amiran_arbolishvili\\PycharmProjects\\python_DQE\\Python_DQE\\task_5')

import task_5
import task_4


def extract_json(src_file_path, tgt_file_path='../task_5/news_feed.txt'):
    raw_content = json.load(open(src_file_path))
    for keys, values in raw_content.items():
        news_type = values["news_type"]
        news_title = values["title"]
        news_city = values["city"]

        news_agent = task_5.NewsAgent(news_type, task_4.correct_iz(news_title), news_city)
        news = news_agent.create_news()

        if news:
            news.publish(tgt_file_path)

        print('news: '+news_title+' | published')


SRC_FILE_TYPE = input('please, select src file type\n')
SRC_FILE_PATH = input('enter the file path\n')
IS_CUSTOM_PATH = int(input('would you like to keep in custom folder? | no - 0 | | yes - 1 |\n'))
if IS_CUSTOM_PATH:
    CUSTOM_PATH = input('enter custom path')
    if SRC_FILE_TYPE == 'json':
        extract_json(SRC_FILE_PATH, CUSTOM_PATH)
else:
    if SRC_FILE_TYPE == 'json':
        extract_json(SRC_FILE_PATH)
