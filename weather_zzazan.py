# -*- coding: utf-8 -*-

import logging
import telegram
from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup

my_api_key = "5591497148:AAGxdQB9Snk6O4Hojt5aMQOrX5v47tdQGYo"   #내 API 키 정보
my_bot = telegram.Bot(my_api_key)

def check_username(update):
    try:
        username = update.message.from_user.first_name
        print('Chat username', username)
        return username
    except:
        username = update.channel_post.from_user.first_name
        return username

def TestPrint(bot, update):
    logging.info('>>> TestPrint')
    my_bot.sendMessage(chat_id=update.effective_chat.id, text="hello~")

def weather_crawling(update, context):
    logging.info('>>> weather info')
    try:
        logging.info('location : {}'.format(context.args[0]))
        user_name = check_username(update)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        res = requests.get(
        'https://www.google.com/search?q={}+날씨'.format(context.args[0]),
        headers=headers)
 
        soup = BeautifulSoup(res.text, 'html.parser')
     
        location = soup.select('#wob_loc')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        temperature = soup.select('#wob_tm')[0].getText().strip()
        high = soup.find_all('div', {'class':'gNCp2e'})[0].find('span', {'style':'display:inline'}).text
        low = soup.find_all('div', {'class':'QrNVmd ZXCv8e'})[0].find('span', {'style':'display:inline'}).text

        weather = "안녕하세요? 짜잔봇입니다.\r\n{} 지역의 날씨를 알려드리겠습니다.\r\n\r\n오늘의 최저기온은 {} 최고기온은 {}이며,\r\n현재온도는 {} / {}입니다.\r\n{}님 행복한 하루 보내세요 ^^*".format(
            location,low+"°C",high+"°C",temperature+"°C",info,user_name)
        my_bot.sendMessage(chat_id=update.effective_chat.id, text=weather)

    except:
        my_bot.sendMessage(chat_id=update.effective_chat.id, text="지역이 명확하지 않습니다. 다시 입력해 주세요.\r\nex) /weather 행신동")


def main():
    updater = Updater(my_api_key, use_context=True)      # 봇에게 들어온 메시지가 있는지 체크
    updater.dispatcher.add_handler(CommandHandler("hi", TestPrint))
    updater.dispatcher.add_handler(CommandHandler("weather", weather_crawling, pass_args=True))
    updater.dispatcher.stop()
    updater.job_queue.stop()
    updater.stop()
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()