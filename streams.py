import os
import json
import os
from datetime import datetime, timezone, timedelta
from time import sleep

import requests
import vk_api
from dotenv import load_dotenv

import functions

load_dotenv()  # Инициализируем переменные окружения. Константы хранятся в файле .env

token = os.getenv('vk_token')
session = vk_api.VkApi(token=token)
upload = vk_api.VkUpload(session)


def post_text_message(message):
    with open('times.json') as json_file:
        post_time = json.load(json_file)
    vk_time = int(post_time['tg'])
    session.method('wall.post', {'owner_id': '-221171917',
                                 'message': f'{message}',
                                 'publish_date': vk_time + 300})
    print(f'Messege to VK published in {datetime.fromtimestamp(vk_time + 300)}')


def read_and_posting_photo():
    print('stream "photo" is run')
    while True:
        if len(os.listdir('downloads_photo')) != 0:
            sleep(5)
            functions.rename_files(dir='downloads_photo')
            imgs = os.listdir('downloads_photo')
            if len(imgs) >= 1:
                photos = []
                print('Starting upload a photos...')
                upload_url = session.method('photos.getWallUploadServer',
                                            {'group_id': "221171917"})['upload_url']
                for elems in imgs:
                    request = requests.post(upload_url,
                                            files={'file': open('downloads_photo' + '/' + elems, 'rb')})
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
                    os.remove('downloads_photo' + '/' + elems)
                print('All elements remowed from downloads_photo folder')
                sleep(5)

            else:
                print('chto-to poshlo ne tak')
                sleep(5)

        else:
            print('stream photo is running')
            sleep(5)


def read_and_posting_video():
    print('stream "video" is run')
    while True:
        if len(os.listdir('downloads_video')) != 0:
            sleep(5)
            functions.rename_files(dir='downloads_video')
            imgs = os.listdir('downloads_video')
            print('Starting upload a videos...')
            list_of_path = []
            for elems in imgs:
                file = ('downloads_video/' + elems)
                video = upload.video(
                    file,
                    group_id=221171917
                )
                vk_video_url = 'video{}_{}'.format(
                    video['owner_id'], video['video_id']
                )
                print(video, '\nLink: ', vk_video_url)
                with open('times.json') as json_file:
                    post_time = json.load(json_file)
                vk_time = int(post_time['tg'])
                session.method('wall.post', {'owner_id': '-221171917',
                                             'message': 'From Good News: t.me/+nF0gaUf4tuUzNjli',
                                             'attachments': f'{vk_video_url}',
                                             'publish_date': vk_time + 300})
                print(f'Video "publishin in VK {datetime.fromtimestamp(datetime.now().timestamp() + 300)}')

            for elems in imgs:
                os.remove('downloads_video' + '/' + elems)
            print('directory "downloads_video" is clean')
            sleep(5)
        else:
            print('stream video is running')
            sleep(5)

# def read_and_posting_audio():
#     print('stream "audio" is run')
#     while True:
#         if len(os.listdir('downloads_audio')) != 0:
#             sleep(5)
#             imgs = os.listdir('downloads_audio')
#             print('Starting upload a audios...')
#             list_of_path = []
#             for elems in imgs:
#                 file = ('downloads_audio/' + elems)
#                 audio = upload.audio(
#                     file,
#                     group_id=221171917
#                 )
#                 vk_audio_url = 'video{}_{}'.format(
#                     audio['owner_id'], audio['video_id']
#                 )
#                 print(audio, '\nLink: ', vk_audio_url)
#
#                 session.method('wall.post', {'owner_id': '-221171917',
#                                              'message': 'From Good News: t.me/+nF0gaUf4tuUzNjli',
#                                              'attachments': f'{vk_audio_url}',
#                                              'publish_date': datetime.now().timestamp() + 300})
#                 print(f'Video "publishin in VK {datetime.fromtimestamp(datetime.now().timestamp() + 300)}')
#
#             for elems in imgs:
#                 os.remove('downloads_video' + '/' + elems)
#             print('directory "downloads_video" is clean')
#             sleep(5)
#         else:
#             print('stream video is running')
#             sleep(5)
