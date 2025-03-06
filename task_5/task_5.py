from datetime import datetime
import sqlite3


"""Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format

You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.
"""


class NewsAgent:
    def __init__(self, news_type, news_title, json_city=''):
        self.news_type = news_type
        self.news_title = news_title
        self.json_city = json_city

    def create_news(self):
        if self.news_type == 'News':
            return News(self.news_title)
        elif self.news_type == 'News_sql':
            news = News(self.news_title)
            self.insert_news(news)
        elif self.news_type == 'PrivateAdd':
            return PrivateAdd(self.news_title)
        elif self.news_type == 'JsonAdd':
            return JsonAdd(self.news_title, self.json_city)
        elif self.news_type == 'XmlAdd':
            return JsonAdd(self.news_title, self.json_city)  # for xml also
        else:
            print("Invalid news type selected!")
            return None

    @staticmethod
    def save_to_file(record, publish_path='news_feed.txt'):
        with open(publish_path, 'a') as file:
            file.write(record + '\n')
            file.close()

    @staticmethod
    def insert_news(news):
        with sqlite3.connect('task_10.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS news (title TEXT, city TEXT)''')
            cursor.execute('''INSERT INTO news (title, city) VALUES (?, ?)''',
                           (news.news_title, news.city))
            connection.commit()
            print(f"News '{news.news_title}' inserted into the database.")


class News(NewsAgent):
    def __init__(self, news_title):
        super().__init__('News', news_title)
        self.city = input("Please, provide the name of the city: ")
        self.date = datetime.now().strftime('%d/%m/%Y %H:%M')

    def publish(self, publish_path):
        record = f"News | Title: {self.news_title} \nCity: {self.city}, Date: {self.date}"
        self.save_to_file(record, publish_path)
        print(f"News published: {record}")


class JsonAdd(NewsAgent):
    def __init__(self, news_title, city):
        super().__init__('PrivateAdd', news_title, city)
        self.date = datetime.now().strftime('%d/%m/%Y %H:%M')

    def publish(self, publish_path):
        record = f"News | Title: {self.news_title} \nCity: {self.json_city}, Date: {self.date}"
        self.save_to_file(record, publish_path)
        print(f"News published: {record}")


class PrivateAdd(NewsAgent):
    def __init__(self, news_title):
        super().__init__('PrivateAdd', news_title)
        self.expiration_date = input("Please, provide the expiration date (DD/MM/YYYY): ")
        self.expiration_date_obj = datetime.strptime(self.expiration_date, '%d/%m/%Y')
        self.days_left = (self.expiration_date_obj - datetime.now()).days

    def publish(self, publish_path):
        record = f"PrivateAd | Title: {self.news_title} \nExpiration Date: {self.expiration_date} | Days Left: {self.days_left}"
        self.save_to_file(record, publish_path)
        print(f"Private ad published: {record}")


if __name__ == '__main__':
    NEWS_TYPE = input('Select news type: | PrivateAdd | | News | \n__enter the fullname of desired type \n')
    news_title = input('\nWrite the title\n')

    news_agent = NewsAgent(NEWS_TYPE, news_title)
    news = news_agent.create_news()

    IS_CUSTOM_PATH = int(input('would you like to keep in custom folder? | no - 0 | | yes - 1 |'))
    if IS_CUSTOM_PATH:
        CUSTOM_PATH = input('enter custom path')
    else:
        CUSTOM_PATH = 'news_feed.txt'

    if news:
        news.publish(CUSTOM_PATH)
