#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
from datetime import date


def get_train():
    """
    Запросить данные о поездах.
    """
    nomer = input("Номер поезда? ")
    punkt = input("Пункт назначения? ")
    time = int(input("Время отправления? "))
    # Создать словарь.
    return {
            'nomer': nomer,
            'punkt': punkt,
            'time': time,
        }


def display_trains(punkts):
    """
    Отобразить список поездов.
    """
    # Проверить, что список поездов не пуст.
    if punkts:
       # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )
        print(line)
        print('| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Номер поезда",
            "Пункт назначения",
            "Время отправления"
            )
        )
        print(line)
        # Вывести данные о всех поездах.
        for idx, train in enumerate(punkts, 1):
            print('| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                train.get('nomer', ''),
                train.get('punkt', ''),
                train.get('time', 0)
                )
            )
        print(line)
       
    else:
        print("Список поездов пуст.")
       
       
def select_trains(punkts, period):
    """
    Выбрать поезда с заданным временем.
    """
    result = []
    for van in punkts:
        if van.get('time', 0) >= period:
            result.append(van) 
   # Возвратить список выбранных поездов.
    return result


def save_trains(filename, punkts):
    """
    Save all trains in JSON file
    """
    with open(filename, "w", encoding = "utf-8") as fout:
        json.dump(punkts, fout, ensure_ascii=False, indent = 4)


def load_trains(filename):
    """
    Load trains from file JSON
    """
    with open(filename, "r", encoding = "utf-8") as fin:
        return json.load(fin)


def main():
    """
    Главная функция программы.
    """
    trains = []
    
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
           break
        elif command == 'add':
            train = get_train()
            trains.append(train) 
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get("train", ""))
        elif command == 'list':
            display_trains(trains)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            period = int(parts[1])
            # Выбрать поезда с заданным временем.
            selected = select_trains(trains, period)
            display_trains(selected)
        
        elif command.startswith('save'):
            parts = command.split(maxsplit=1)
            filename = parts[1]
            save_trains(filename, trains)

        elif command.startswith('load'):
            parts = command.split(maxsplit = 1)
            filename = parts[1]
            trains = load_trains(filename)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <время> - запросить поезда с временем отправления;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла:")
            print("save - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()