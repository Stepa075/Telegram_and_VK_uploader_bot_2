import json
import os
import time
from datetime import datetime

import requests
import vk_api
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('vk_token')
session = vk_api.VkApi(token=token)

upload = vk_api.VkUpload(session)

if len(os.listdir('downloads_video')) != 0:
    time.sleep(5)
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

        session.method('wall.post', {'owner_id': '-221171917',
                                     'message': 'From Good News: t.me/+nF0gaUf4tuUzNjli',
                                     'attachments': f'{vk_video_url}',
                                     'publish_date': datetime.now().timestamp() + 300})
        print(f'Video "publishin in VK {datetime.fromtimestamp(datetime.now().timestamp() + 300)}')
# import variables
#
# # load_dotenv()  # инициализируем переменные окружения. Константы хранятся в файле .env
# # token = os.getenv('vk_token')
# # session = vk_api.VkApi(token=token)
# list_of_path = []
# imgs = os.listdir('downloads_video')
# for elems in imgs:
#     list_of_path.append('downloads_video/'+ elems)
# files = ",".join(list_of_path)
# print(files)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # print(int(datetime.now().timestamp()))
# # print(int(time.time()))
#
# # if len(os.listdir('downloads')) != 0:
# #     print(len(os.listdir('downloads')))
# #     print(os.listdir('downloads'))
# # else:
# #     print('nema nixuya')
# # dir1 = 'downloads'
# # print(len(os.listdir(dir1)))
#
#
# # wall_post_message = session.method('wall.post', {'owner_id': '-221171917',
# #                                                    'message': f'{variables.message}',
# #                                                    'publish_date': datetime.now().timestamp() + 300})
#
# # curl 'https://api.vk.com/method/video.save' \
# #   -F 'access_token=vk1.a.S5vuNVlN9MKLrjPsHiU7y3B47Fb462DwakdVEMpb7p1dv1UxyfSPbMFyzCF7I90Nv4KVjEnR5IJifwuWZ9hTbtByeN6eE8Nbf1GNkzCab2ydydVqzQExzxoF7cBA4w-IOwIDvtQ_D4CTwAvm0qNAR4Z-SF1ZXage8Z_zyAeRCkLVIJrWbaraalhWfF_5yAhA' \
# #   -F 'v=5.131'
#
#
# # with open('times.json') as json_file:
# #     post_time = json.load(json_file)
# # vk_time = int(post_time['tg'])
# # session.method('wall.post', {'owner_id': '-221171917',
# #                              'message': f'Hi!',
# #                              'publish_date': vk_time + 300})