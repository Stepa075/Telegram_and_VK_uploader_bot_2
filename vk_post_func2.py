import json
import os
from datetime import datetime, timezone, timedelta
from time import sleep

import requests
import vk_api
from dotenv import load_dotenv

load_dotenv()  # инициализируем переменные окружения. Константы хранятся в файле .env

token = os.getenv('vk_token')
session = vk_api.VkApi(token=token)


def read_and_posting():
    imgs = os.listdir('downloads')
    # if len(imgs) == 1:
    #     print('Starting upload a photos...')
    #     upload_url = session.method('photos.getWallUploadServer',
    #                                 {'group_id': "221171917"})['upload_url']
    #     for elems in imgs:
    #         request = requests.post(upload_url,
    #                                 files={'file': open('downloads' + '/' + elems, 'rb')})
    #         save_wall_photo = session.method('photos.saveWallPhoto',
    #                                          {'group_id': '221171917',
    #                                           'photo': request.json()['photo'],
    #                                           'server': request.json()['server'],
    #                                           'hash': request.json()['hash']})
    #         saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + '_' + str(save_wall_photo[0]['id'])
    #         print("image uploaded to VK")
    #         with open('times.json') as json_file:
    #             post_time = json.load(json_file)
    #         vk_time = int(post_time['tg'])
    #         wall_post_photo = session.method('wall.post', {'owner_id': '-221171917',
    #                                                        'message': 'From Good News: t.me/+nF0gaUf4tuUzNjli',
    #                                                        'attachments': saved_photo,
    #                                                        'publish_date': vk_time+86400})
    #         print("publishin post in VK", datetime.fromtimestamp(vk_time))
    #     # for elems in imgs:
    #     #     os.remove('downloads' + '/' + elems)


    if len(imgs) >= 1:
        photos = []
        print('Starting upload a photos...')
        upload_url = session.method('photos.getWallUploadServer',
                                    {'group_id': "221171917"})['upload_url']
        for elems in imgs:
            request = requests.post(upload_url,
                                    files={'file': open('downloads' + '/' + elems, 'rb')})
            save_wall_photo = session.method('photos.saveWallPhoto',
                                             {'group_id': '221171917',
                                              'photo': request.json()['photo'],
                                              'server': request.json()['server'],
                                              'hash': request.json()['hash']})
            saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + '_' + str(save_wall_photo[0]['id'])
            photos.append(saved_photo)
            print("image uploaded to VK")
        phs = ','.join(photos)
        print(phs)
        with open('times.json') as json_file:
            post_time = json.load(json_file)
        vk_time = int(post_time['tg'])

        wall_post_photo = session.method('wall.post', {'owner_id': '-221171917',
                                                       'message': 'From Good News: t.me/+nF0gaUf4tuUzNjli',
                                                       'attachments': phs,
                                                       'publish_date': vk_time + 300})
        print("publishin post in VK", datetime.fromtimestamp(vk_time))
    else:
        print('chto-to poshlo ne tak')

    # for elems in imgs:
    #     os.remove('downloads' + '/' + elems)
    print('All elements remowed from download folder')

if __name__ == "__main__":
    read_and_posting()