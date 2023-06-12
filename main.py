import requests
import json
from pyrogram import Client, filters
from datetime import datetime, timezone, timedelta
import os
from dotenv import load_dotenv  # импортируем модуль из библиотеки для хранения констант в переменных среды
import vk_api

from test import change_time_post

load_dotenv()  # инициализируем его. Константы хранятся в файле .env

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
otloga = int(os.getenv('otloga'))
chanel = int(os.getenv('chanel'))  # блядь, внимательно смотрим совпадение ключей здесь и в .env!!!
tg_period = int(os.getenv('tg_period'))  # через сколько будет постится следующий пост в телеге

with open('times.json') as json_file:  # переписываем время на текущее
    post_time = json.load(json_file)
post_time["tg"] = int(datetime.now().timestamp())
with open('times.json', 'w') as json_file:
    json.dump(post_time, json_file)  # вот именно таким замысловатым образом

app = Client('smell2', api_id=api_id, api_hash=api_hash)  # инициализируем бота


# session = vk_api.VkApi(token=tokens.v_token)

@app.on_message(filters.chat(otloga))  # ждем обновления сообщений в канале предложки (контента)
def new_post(client, message):
    with open('times.json') as json_file:
        post_time = json.load(json_file)
    new_time = int(post_time['tg']) + tg_period  # прибавляем время периода в формате 18926473837636
    time_control = change_time_post(datetime.fromtimestamp(new_time).replace(tzinfo=timezone.utc) - timedelta(hours=2))
    new_time_control = time_control - timedelta(hours=1)
    client.copy_message(                         # отправляем сообщение в отложку основного канала
        chat_id=chanel,
        from_chat_id=message.chat.id,
        message_id=message.id,
        schedule_date= new_time_control    # тут аккуратно - долго ебся с форматом, только с .replace(tzinfo=timezone.utc) работает
    )
    print("Message uploaded to delayed publication", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Message will be published in channel in", (datetime.fromtimestamp(new_time)))  # с + timedelta(hours=3) в консоль время публикации поста в канале отображается правильно!!!

    post_time['tg'] = new_time                        # добавленное время записываем для следующего сообщения
    with open('times.json', 'w') as json_file:
        json.dump(post_time, json_file)

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
    #     session.method('wall_post', {'owner_id': '-213340641', 'attachments': phs,
    #                                  'publish_date': vk_time,
    #                                  'copyright': 'https://t.me/+YxkXh6NpvuFjMzcy'})
    #     print("publishin post in VK", datetime.fromtimestamp(vk_time))
    #     post_time['vk'] = vk_time
    #     with open('times.json', 'w') as json_file:
    #         json.dump(post_time, json_file)
    #
    #     for elems in imgs:
    #         os.remove('downloads' + '/' + elems)


app.run()
