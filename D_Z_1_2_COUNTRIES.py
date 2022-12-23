import json


class Paises:
    def __init__(self, pais, capital):
        self.pais = pais
        self.capital = capital
        data[self.pais] = self.capital

    def __str__(self):
        return f'{self.pais}: {self.capital}'

    @ classmethod
    def add_country(cls, new_pais, new_capital, filename):
        try:
            data1 = json.load(open(filename))
        except FileNotFoundError:
            data1 = {}

        data1[new_pais] = new_capital

        with open(filename, 'w') as f:
            data1[new_pais] = new_capital
            json.dump(data1, f, indent=2, ensure_ascii=False)

    @classmethod
    def remove_country(self, del_country, filename):
        try:
            data1 = json.load(open(filename))
        except FileNotFoundError:
            data1 = {}

        if del_country in data1:
            del data1[del_country]

            with open(filename, 'w') as f:
                json.dump(data1, f, indent=2, ensure_ascii=False)
        else:
            print("Такой страны в базе нет.")

    @classmethod
    def search_data(cls, pais, filename):
        try:
            data1 = json.load(open(filename))
        except FileNotFoundError:
            data1 = {}

        if pais in data1:
            print(f"Страна {pais} есть в базе."
                  f" Её столица - {data1[pais]}.")
        else:
            print(f"Страны {pais} нет в базе.")


    @classmethod
    def cheng_capital(cls, pais, new_capital, filename):
        try:
            data1 = json.load(open(filename))
        except FileNotFoundError:
            data1 = {}

        if pais in data1:
            data1[pais] = new_capital

            with open(filename, 'w') as f:
                json.dump(data1, f, indent=2, ensure_ascii=False)
        else:
            print(f"Страны {pais} нет в базе.")

    @ classmethod
    def info_from_file(cls, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


data = {"Россия": "Москва"}
filename1 = 'list_of_countries.json'
with open(filename1, 'w') as f_save:
   json.dump(data, f_save, indent=2, ensure_ascii=False)


n = 0
while 0 <= n <= 6:
    print("*" * 40)
    print('Выбор действия:\n'
          '1 - добавление данных\n'
          '2 - удаление данных\n'
          '3 - поиск данных\n'
          '4 - редактирование данных\n'
          '5 - просмотр данных\n'
          '6 - завершение работы\n')

    n = int(input('Ввод: '))
    if n == 1:
        new_pais = input("Введите название страны (с заглавной буквы): ")
        new_capital = input("Введите название столицы страны (с заглавной буквы): ")
        Paises.add_country(new_pais, new_capital, 'list_of_countries.json')
        print(f"Страна {new_pais} добавлена")
        print("Файл сохранён")
    elif n == 2:
        name = input("Введите имя страны (с заглавной буквы) для удаления: ")
        Paises.remove_country(name, 'list_of_countries.json')
        print("Файл сохранён")

    elif n == 3:
        name = input("Введите название (с заглавной буквы) страны для поиска: ")
        Paises.search_data(name, 'list_of_countries.json')

    elif n == 4:
        name = input("Введите название страны (с заглавной буквы) для редактирования: ")
        new_value = input("Введите новое название столицы (с заглавной буквы): ")
        Paises.cheng_capital(name, new_value, 'list_of_countries.json')
        print("Файл сохранён")
    elif n == 5:
        Paises.info_from_file('list_of_countries.json')
    elif n == 6:
        print("Программа завершена")
        break


# C:\Users\Dmitry\Scripts\HomeWork\venv\Scripts\python.exe C:/Users/Dmitry/Scripts/HomeWork/D_Z_1_2_COUNTRIES.py
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 5
# {'Россия': 'Москва'}
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 1
# Введите название страны (с заглавной буквы): Швейцария
# Введите название столицы страны (с заглавной буквы): Берн
# Страна Швейцария добавлена
# Файл сохранён
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 1
# Введите название страны (с заглавной буквы): Испания
# Введите название столицы страны (с заглавной буквы): Барселона
# Страна Испания добавлена
# Файл сохранён
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 3
# Введите название (с заглавной буквы) страны для поиска: Швейцария
# Страна Швейцария есть в базе. Её столица - Берн.
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 4
# Введите название страны (с заглавной буквы) для редактирования: Испания
# Введите новое название столицы (с заглавной буквы): Мадрид
# Файл сохранён
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 5
# {'Россия': 'Москва', 'Швейцария': 'Берн', 'Испания': 'Мадрид'}
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 6
# Программа завершена
#
# Process finished with exit code 0
#
# C:\Users\Dmitry\Scripts\HomeWork\venv\Scripts\python.exe C:/Users/Dmitry/Scripts/HomeWork/D_Z_1_2_COUNTRIES.py
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 1
# Введите название страны (с заглавной буквы): Германия
# Введите название столицы страны (с заглавной буквы): Берлин
# Страна Германия добавлена
# Файл сохранён
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 5
# {'Россия': 'Москва', 'Германия': 'Берлин'}
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 2
# Введите имя страны (с заглавной буквы) для удаления: Германия
# Файл сохранён
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 5
# {'Россия': 'Москва'}
# ****************************************
# Выбор действия:
# 1 - добавление данных
# 2 - удаление данных
# 3 - поиск данных
# 4 - редактирование данных
# 5 - просмотр данных
# 6 - завершение работы
#
# Ввод: 6
# Программа завершена
#
# Process finished with exit code 0


