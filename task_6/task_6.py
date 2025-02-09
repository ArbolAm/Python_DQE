import sys

sys.path.insert(0, 'path\\Python_DQE')
sys.path.insert(1, 'path\\Python_DQE\\task_5')

import task_4
import task_5


NEWS_TYPE = input('Select news type: | PrivateAdd | | News | \n__enter the fullname of desired type \n')
news_title = input('\nWrite the title\n')

news_agent = task_5.NewsAgent(NEWS_TYPE, task_4.correct_iz(news_title))
news = news_agent.create_news()

IS_CUSTOM_PATH = int(input('would you like to keep in custom folder? | no - 0 | | yes - 1 |'))
if IS_CUSTOM_PATH:
    CUSTOM_PATH = input('enter custom path')
else:
    CUSTOM_PATH = 'news_feed.txt'

if news:
    news.publish(CUSTOM_PATH)

