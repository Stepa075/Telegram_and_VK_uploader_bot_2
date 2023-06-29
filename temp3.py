import os
from time import sleep

import functions

def rename_files():

    imgs = os.listdir('test_downloads_photo')
    print('Starting upload a videos...')
    for elems in imgs:
        file = ('test_downloads_photo/' + elems)
        name_file = os.path.splitext(file)[0]
        name_file_sample = name_file.split('/')[1]
        extension = os.path.splitext(file)[1]
        new_gen_name = functions.random_gen()
        new_name_of_file = f"{name_file.split('/')[0]}/{new_gen_name}{extension}"
        sleep(1)
        os.rename(file, new_name_of_file)
        print(new_name_of_file)
