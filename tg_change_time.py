import configparser
import json
from datetime import datetime, timedelta

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")


def change_time_post():
    period = int(config["TG"]["PERIOD_BETWEEN_POSTS"])
    start_time = int(config["TG"]["TIME_START_POSTING_TG"])
    end_time = int(config["TG"]["TIME_END_POSTING_TG"])
    current_date_time = datetime.now()  # дата сейчас
    current_time = current_date_time.time()  # время сейчас
    hour = current_time.strftime('%H')  # переменная часы
    min = current_time.strftime('%M')  # переменная минуты
    now_day_start = current_date_time - timedelta(hours=int(hour), minutes=int(min)) + timedelta(
        hours=start_time)  # текущее время для сегодня старта
    now_day_finish = current_date_time - timedelta(hours=int(hour), minutes=int(min)) + timedelta(
        hours=end_time)  # текущее время для сегодня финиша
    tomorrow_day = current_date_time + timedelta(days=1)  # плюс сутки
    tomorrow_date = tomorrow_day - timedelta(hours=int(hour), minutes=int(min))  # отнимаем текущее время
    # чтобы получить время на начало суток
    tomorrow_date_with_start_time = tomorrow_date + timedelta(hours=start_time)  # прибавляем время начала постинга
    tomorrow_date_with_end_time = tomorrow_date + timedelta(hours=end_time)  # прибавляем время конца постинга
    print(now_day_start.strftime('%Y-%m-%d %H:%M:%S'))
    print(now_day_finish.strftime('%Y-%m-%d %H:%M:%S'))
    # print(tomorrow_date.strftime('%Y-%m-%d %H:%M:%S'))
    print(tomorrow_date_with_start_time.strftime('%Y-%m-%d %H:%M:%S'))
    print(tomorrow_date_with_end_time.strftime('%Y-%m-%d %H:%M:%S'))

    with open('times.json') as json_file:  # переписываем время на завтрашнее время запуска
        post_time = json.load(json_file)
    if post_time["tg"] < datetime.now().timestamp():  # Если время постинга уже прошло, но еще находится в разрешенном пределе  сегодня
        post_time['tg'] = int(datetime.now().timestamp())
        print(post_time)
        with open('times.json', 'w') as json_file:
            json.dump(post_time, json_file)  # вот именно таким замысловатым образом
        print("segodnia pozge")
    else:
        print("vse ok budet segodnia")
    with open('times.json') as json_file:
        post_time = json.load(json_file)
    if current_date_time < now_day_start:  # Если пытаемся запостить до начала разрешенного времени

        new_time = int(post_time['tg'])
        if new_time < current_date_time.timestamp():
            while current_date_time < now_day_start:
                current_date_time = current_date_time + timedelta(hours=period)
            print("fuck normal  " + current_date_time.strftime('%Y-%m-%d %H:%M:%S'))
            with open('times.json') as json_file:  # переписываем время на сегодня в пределе начала постинга
                post_time = json.load(json_file)
            post_time["tg"] = current_date_time.timestamp()
            print(post_time)
            with open('times.json', 'w') as json_file:
                json.dump(post_time, json_file)  # вот именно таким замысловатым образом
            print("normal writing to file")
        else:
            print("working with file time")
    else:
        print("ne malo")

    if current_date_time > now_day_finish:  # Если пытаемся запостить после окончания разрешенного времени
        with open('times.json') as json_file:  # переписываем время на завтрашнее время запуска
            post_time = json.load(json_file)
        if post_time["tg"] > tomorrow_date_with_start_time.timestamp():
            pass
        else:
            post_time["tg"] = tomorrow_date_with_start_time.timestamp()  # int(datetime.now().timestamp())
            print(post_time)
            with open('times.json', 'w') as json_file:
                json.dump(post_time, json_file)  # вот именно таким замысловатым образом
            print("fuck")
    else:
        print("ne mnogo")

    with open('times.json') as json_file:  # переписываем время на завтрашнее время запуска
        post_time = json.load(json_file)

    if (post_time["tg"] + 3600) > now_day_finish.timestamp():  # Если время постинга находится вне разрешенного времени сегодня
        with open('times.json') as json_file:  # переписываем время на завтрашнее время запуска
            post_time = json.load(json_file)
        if post_time["tg"] > tomorrow_date_with_start_time.timestamp():
            pass
        else:
            post_time["tg"] = tomorrow_date_with_start_time.timestamp()  # int(datetime.now().timestamp())
            print(post_time)
            with open('times.json', 'w') as json_file:
                json.dump(post_time, json_file)  # вот именно таким замысловатым образом
            print("zavtra")
    else:
        print("ne zavtra")


if __name__ == "__main__":
    change_time_post()
