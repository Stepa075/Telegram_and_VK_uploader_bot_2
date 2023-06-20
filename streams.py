import os
import json
import os
from datetime import datetime, timezone, timedelta
from time import sleep

import requests
import vk_api
from dotenv import load_dotenv

import variables

load_dotenv()  # инициализируем переменные окружения. Константы хранятся в файле .env

token = os.getenv('vk_token')
session = vk_api.VkApi(token=token)


def post_text_message(message):
    with open('times.json') as json_file:
        post_time = json.load(json_file)
    vk_time = int(post_time['tg'])
    session.method('wall.post', {'owner_id': '-221171917',
                                 'message': f'{message}',
                                 'publish_date': vk_time + 300})
    print(f'Messege to VK published in {datetime.fromtimestamp(vk_time + 300)}')


def read_and_posting():
    print('stream is run')
    while True:
        if len(os.listdir('downloads')) != 0:
            sleep(5)
            imgs = os.listdir('downloads')
            if len(imgs) == 1:
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
                    print("image uploaded to VK")
                    with open('times.json') as json_file:
                        post_time = json.load(json_file)
                    vk_time = int(post_time['tg'])
                    wall_post_photo = session.method('wall.post', {'owner_id': '-221171917',
                                                                   'message': 'From Good News: t.me/+nF0gaUf4tuUzNjli',
                                                                   'attachments': 'saved_photo',
                                                                   'publish_date': vk_time + 300})
                    print("publishin post in VK", datetime.fromtimestamp(vk_time))
                for elems in imgs:
                    os.remove('downloads' + '/' + elems)
                print('directory "downloads" is clean')
                sleep(5)

            elif len(imgs) > 1:
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
                for elems in imgs:
                    os.remove('downloads' + '/' + elems)
                print('All elements remowed from download folder')
                sleep(5)

            # elif variables.message != "":
            #
            #     print('Starting upload a message...')
            #     upload_url = session.method('photos.getWallUploadServer',
            #                                 {'group_id': "221171917"})['upload_url']
            #
            #     request = requests.post(upload_url, variables.message 'rb')})
            #     save_wall_photo = session.method('photos.saveWallPhoto',
            #                                      {'group_id': '221171917',
            #                                       'photo': request.json()['photo'],
            #                                       'server': request.json()['server'],
            #                                       'hash': request.json()['hash']})
            #     with open('times.json') as json_file:
            #         post_time = json.load(json_file)
            #     vk_time = int(post_time['tg'])
            #
            #     wall_post_message = session.method('wall.post', {'owner_id': '-221171917',
            #                                                    'message': f'{variables.message}',
            #                                                    'publish_date': vk_time + 300})
            #     print("publishin post in VK", datetime.fromtimestamp(vk_time))
            #     variables.message = ""
            #     sleep(5)
            else:
                print('chto-to poshlo ne tak')
                sleep(5)


        else:
            print('stream is running')
            sleep(5)
