import json

data = {"Россия": "Москва"}




class Paises:
    name1 = Try_Exept()

    def __init__(self, pais, capital):
        self.pais = pais
        self.capital = capital
        data[self.pais] = self.capital

    def __str__(self):
        a = ''
        a += str(f"{self.pais}: {self.capital}") + "\n"
        return f'{self.pais}: {self.capital}'

    def load_data(func):
        def wrap(*args, filename):
            try:
                data = json.load(open(file))
            except FileNotFoundError:
                data = {}
            func(*args, filename)
            print("Файл сохранён")
        return wrap()

    @ classmethod
    @ load_data
    def add_country(cls, new_pais, new_capital, file):
        try:
            data1 = json.load(open(file))
        except FileNotFoundError:
            data1 = {}

        data1[new_pais] = new_capital

        with open(file, 'w') as f:
            data1[new_pais] = new_capital
            json.dump(data1, f, indent=2, ensure_ascii=False)

    @classmethod
    def remove_country(self, del_country, file ):
        try:
            data1 = json.load(open(file))
        except FileNotFoundError:
            data1 = {}

        if del_country in data1:
            del data1[del_country]

            with open(file, 'w') as f:
                json.dump(data1, f, indent=2, ensure_ascii=False)
        else:
            print("Такой страны в базе нет.")

    @classmethod
    def search_data(cls, pais, file):
        try:
            data1 = json.load(open(file))
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


filename1 = 'list_of_countries.json'
with open(filename1, 'w') as fw:
   json.dump(data, fw, indent=2, ensure_ascii=False)


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

    def print_file(self):
        print("Файл сохранён")
