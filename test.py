import json
import time
from datetime import datetime, timezone, date, timedelta
import os
from dotenv import load_dotenv
import configparser


def change_time_post():
    start_time = 6
    end_time = 22
    current_date_time = datetime.now()  # дата сейчас
    current_time = current_date_time.time()  # время сейчас
    hour = current_time.strftime('%H')  #переменная часы
    min = current_time.strftime('%M')   # переменная минуты
    now_day_start = current_date_time - timedelta(hours=int(hour), minutes=int(min)) + timedelta(hours=6)  # текущее время для сегодня старта
    now_day_finish = current_date_time - timedelta(hours=int(hour), minutes=int(min)) + timedelta(hours=22)  # текущее время для сегодня финиша
    tomorrow_day = current_date_time + timedelta(days=1)  # плюс сутки
    tomorrow_date = tomorrow_day - timedelta(hours=int(hour), minutes=int(min))  # отнимаем текущее время
                                                                   # чтобы получить время на начало суток
    tomorrow_date_with_start_time = tomorrow_date + timedelta(hours=start_time)   # прибавляем время начала постинга
    tomorrow_date_with_end_time = tomorrow_date + timedelta(hours=end_time)   # прибавляем время конца постинга
    print(now_day_start.strftime('%Y-%m-%d %H:%M:%S'))
    print(now_day_finish.strftime('%Y-%m-%d %H:%M:%S'))
    # print(tomorrow_date.strftime('%Y-%m-%d %H:%M:%S'))
    print(tomorrow_date_with_start_time.strftime('%Y-%m-%d %H:%M:%S'))
    print(tomorrow_date_with_end_time.strftime('%Y-%m-%d %H:%M:%S'))

    # print(hour)
    # print(tomorrow_datetime)
    # print(tomorrow_date_time_all.strftime('%Y-%m-%d %H:%M:%S'))
    # time_min = "06:00:00"
    # time_max = "22:00:00"
    # j_min = datetime.strptime(f"{time_min}", "%H:%M:%S")  # заданное время минимум
    # j_max = datetime.strptime(f"{time_max}", "%H:%M:%S")  # заданное время максимум
    # j_min_1 = j_min.time()
    # j_max_1 = j_max.time()
    # interval = 7200
    # # x = (datetime.fromtimestamp(datetime.now().timestamp() + interval).replace(
    # #     tzinfo=timezone.utc))  # прибавленное к интервалу текущее время
    # x1 = x.time()
    # if j_max_1 > x1 > j_min_1:
    #     b = 1
    # else:
    #     b = 0
    # while b == 0:
    #     x = (datetime.fromtimestamp(datetime.now().timestamp() + interval).replace(
    #         tzinfo=timezone.utc))
    #     interval += 3600
    #     x1 = x.time()
    #     if j_max_1 > x1 > j_min_1:
    #         b = 1
    #     else:
    #         b = 0
    # print(j_min_1)
    # print(x1)
    # print(j_max_1)
    # return x


if __name__ == "__main__":
    change_time_post()
