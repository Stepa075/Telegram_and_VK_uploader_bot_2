# -*- coding: utf-8 -*-

import os
from datetime import datetime
import vk_api
from dotenv import load_dotenv

load_dotenv()


def upload_video_to_wall():
    token = os.getenv('vk_token')
    session = vk_api.VkApi(token=token)

    upload = vk_api.VkUpload(session)

    video = upload.video(
        'downloads/IMG_7460.mp4',
        group_id=221171917
    )
    vk_video_url1 = 'video{}_{}'.format(
        video['owner_id'], video['video_id']
    )
    print(video, '\nLink: ', vk_video_url1)

    session.method('wall.post', {'owner_id': '-221171917',
                                 'message': 'From Good News: t.me/+nF0gaUf4tuUzNjli',
                                 'attachments': f'{vk_video_url1}',
                                 'publish_date': datetime.now().timestamp() + 300})
    print(f'Video "publishin in VK {datetime.now().timestamp() + 300}')


if __name__ == '__main__':
    upload_video_to_wall()
