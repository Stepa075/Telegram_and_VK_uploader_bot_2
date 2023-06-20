import configparser
from threading import Thread
from time import sleep

import requests
import json
from pyrogram import Client, filters
from datetime import datetime, timezone, timedelta
import os
from dotenv import load_dotenv  # импортируем модуль из библиотеки для хранения констант в переменных среды

import streams
from tg_change_time import change_time_post
from vk_post_func2 import read_and_posting

load_dotenv()  # инициализируем его. Константы хранятся в файле .env
config = configparser.ConfigParser()  # создаём объекта парсера файла settings.ini
config.read("settings.ini")

posting_in_vk = int(config["VK"]["POSTING_IN_VK"])
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
otloga = int(os.getenv('otloga'))
chanel = int(os.getenv('chanel'))  # блядь, внимательно смотрим совпадение ключей здесь и в .env!!!
tg_period = int(os.getenv('tg_period'))  # через сколько будет постится следующий пост в телеге и вк

with open('times.json') as json_file:  # переписываем время на текущее при старте скрипта
    post_time = json.load(json_file)
post_time["tg"] = int(datetime.now().timestamp())
with open('times.json', 'w') as json_file:
    json.dump(post_time, json_file)  # вот именно таким замысловатым образом

app = Client('smell2', api_id=api_id, api_hash=api_hash)  # инициализируем бота


@app.on_message(filters.chat(otloga))  # ждем обновления сообщений в канале предложки (контента)
def new_post(client, message):
    change_time_post()
    with open('times.json') as json_file:
        post_time = json.load(json_file)
    new_time = int(post_time['tg']) + tg_period  # прибавляем время периода в формате 18926473837636
    client.copy_message(  # отправляем сообщение в отложку основного канала
        chat_id=chanel,
        from_chat_id=message.chat.id,
        message_id=message.id,
        schedule_date=datetime.fromtimestamp(new_time).replace(tzinfo=timezone.utc) - timedelta(hours=3))  # тут
    # аккуратно - долго ебся с форматом, только с .replace(tzinfo=timezone.utc) работает
    print("Message uploaded to delayed publication", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Message will be published in channel in", (datetime.fromtimestamp(new_time)))  # с + timedelta(hours=3) в
    # консоль время публикации поста в канале отображается правильно!!!
    try:
        app.download_media(
            message)  # грузит отправленную КАРТИНКУ в отложку в папку downloads в корневой директории проекта
    except:
        pass
    try:
        print(app.download_media(
            message.text))  # грузит отправленную
    except:
        pass
    post_time['tg'] = new_time  # добавленное время записываем для следующего сообщения
    with open('times.json', 'w') as json_file:
        json.dump(post_time, json_file)

    #
    # if posting_in_vk == 1:
    #     read_and_posting()

    # session = vk_api.VkApi(token=tokens.v_token)
    # app.download_media(message)
    # imgs = os.listdir('downloads')
    # if len(imgs) > 3:
    #     photos = []
    #     print('Starting upload a photos...')
    #     upload_url = session.method('photos.getWallUploadServer',
    #                                 {'group_id': tokens.public_id})['upload_url']
    #     for elems in imgs:
    #         request = requests.post(upload_url,
    #                                 files={'file': open('downloads' + '/' + elems, 'rb')})
    #         save_wall_photo = session.method('photos.saveWallPhoto',
    #                                          {'group_id': '213340641',
    #                                           'photo': request.json()['photo'],
    #                                           'server': request.json()['server'],
    #                                           'hash': request.json()['hash']})
    #         saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + '_' + str(save_wall_photo[0]['id'])
    #         photos.append(saved_photo)
    #         print("image uploaded to VK")
    #     phs = ','.join(photos)
    #     print(phs)
    #     with open('times.json') as json_file:
    #         post_time = json.load(json_file)
    #     vk_time = int(post_time['vk']) + 86400
    #     session.method('wall.post', {'owner_id': '-213340641', 'attachments': phs,
    #                                  'publish_date': vk_time,
    #                                  'copyright': 'https://t.me/+YxkXh6NpvuFjMzcy'})
    #     print("publishin post in VK", datetime.fromtimestamp(vk_time))
    #     post_time['vk'] = vk_time
    #     with open('times.json', 'w') as json_file:
    #         json.dump(post_time, json_file)
    #
    #     for elems in imgs:
    #         os.remove('downloads' + '/' + elems)


thread = Thread(target=streams.read_and_posting, daemon=True)
thread.start()
app.run()
