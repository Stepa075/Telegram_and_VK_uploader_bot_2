import os
import time
from datetime import datetime

# print(int(datetime.now().timestamp()))
# print(int(time.time()))

if len(os.listdir('downloads')) != 0:
    print(len(os.listdir('downloads')))
    print(os.listdir('downloads'))
else:
    print('nema nixuya')
# dir1 = 'downloads'
# print(len(os.listdir(dir1)))