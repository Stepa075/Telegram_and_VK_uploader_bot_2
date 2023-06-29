import os
import random
import string
from time import sleep


def rename_files(dir):
    imgs = os.listdir(dir)
    print('Starting upload a videos...')
    for elems in imgs:
        file = (f'{dir}/' + elems)
        name_file = os.path.splitext(file)[0]
        name_file_sample = name_file.split('/')[1]
        extension = os.path.splitext(file)[1]
        new_gen_name = random_gen()
        new_name_of_file = f"{name_file.split('/')[0]}/{new_gen_name}{extension}"
        sleep(1)
        os.rename(file, new_name_of_file)
        print(new_name_of_file)


def random_gen():
    a = ""
    b = ""
    c = ""
    for i in range(5):
        a = random.randint(0, 999)
        b = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(
            string.ascii_letters) + random.choice(string.ascii_letters)
        c = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(
            string.ascii_letters) + random.choice(string.ascii_letters)
        i += 1
    x = str(c) + str(a) + str(b)
    print(x)
    return x


if __name__ == '__main__':
    rename_files(dir='test_downloads_photo')
