import sys
import xml.etree.ElementTree as ET
from datetime import datetime

sys.path.insert(0, 'C:\\Users\\amiran_arbolishvili\\PycharmProjects\\python_DQE\\Python_DQE')
sys.path.insert(1, 'C:\\Users\\amiran_arbolishvili\\PycharmProjects\\python_DQE\\Python_DQE\\task_5')

import task_5
import task_4


def extract_xml(src_file_path, tgt_file_path='../task_5/news_feed.txt'):
    tree = ET.parse(src_file_path)
    root = tree.getroot()

    for article in root.findall('article'):
        news_type = article.find('news_type').text
        news_title = article.find('title').text
        news_city = article.find('city').text

        news_agent = task_5.NewsAgent(news_type, news_title, news_city)
        news = news_agent.create_news()

        if news:
            news.publish(tgt_file_path)

        print('news: '+news_title+' | published')


SRC_FILE_TYPE = input('please, select src file type\n')
SRC_FILE_PATH = input('enter the file path\n')
IS_CUSTOM_PATH = int(input('would you like to keep in custom folder? | no - 0 | | yes - 1 |\n'))
if IS_CUSTOM_PATH:
    CUSTOM_PATH = input('enter custom path')
    if SRC_FILE_TYPE == 'xml':
        extract_xml(SRC_FILE_PATH, CUSTOM_PATH)
else:
    if SRC_FILE_TYPE == 'xml':
        extract_xml(SRC_FILE_PATH)
