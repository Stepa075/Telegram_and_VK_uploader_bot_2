import json
import time
from datetime import datetime, timezone, date, timedelta
import os
from dotenv import load_dotenv
import configparser


# new_time = int(post_time['tg']) + 7800
# print(new_time)
# date_string = "16:30"
# date = datetime.strptime(date_string, "%H:%M").replace(tzinfo=timezone.utc)
# schedule_date = (datetime.fromtimestamp(new_time))
# print(date)
# print(int(datetime.now().timestamp()))
# print(datetime.now().timestamp())
# with open('times.json') as json_file:
#     post_time = json.load(json_file)
# post_time["tg"] = int(datetime.now().timestamp())
# with open('times.json', 'w') as json_file:
#     json.dump(post_time, json_file)
#
#
# load_dotenv()
# print(datetime.now())

# config = configparser.ConfigParser()  # создаём объекта парсера
# config.read("settings.ini")  # читаем конфиг
# a = config["Twitter"]["username"]
# print(a)  # обращаемся как к обычному словарю!
# f = current_date = date.today()  # берем текущую дату
def change_time_post(x):
    time_min = "06:00:00"
    time_max = "22:00:00"
    j_min = datetime.strptime(f"{time_min}", "%H:%M:%S")  # заданное время минимум
    j_max = datetime.strptime(f"{time_max}", "%H:%M:%S")  # заданное время максимум
    j_min_1 = j_min.time()
    j_max_1 = j_max.time()
    interval = 0
    # x = (datetime.fromtimestamp(datetime.now().timestamp() + interval).replace(
    #     tzinfo=timezone.utc))  # прибавленное к интервалу текущее время
    x1 = x.time()
    if j_max_1 > x1 > j_min_1:
        b = 1
    else:
        b = 0
    while b == 0:
        interval += 3600
        x = (datetime.fromtimestamp(datetime.now().timestamp() + interval).replace(
            tzinfo=timezone.utc))
        x1 = x.time()
        if j_max_1 > x1 > j_min_1:
            b = 1
        else:
            b = 0
    print(j_min_1)
    print(x1)
    print(j_max_1)
    return x
