import json


class Countrier:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def __str__(self):
        a = ''
        a += "\n"
        return f'{self.name}: {self.capital}'

    def add_name(self, name):
        self.name.append(name)

    def add_capital(self, capital):
        self.capital.append(capital)

    def remove_countr(self, index):
        c.remove(index)

    def search_countr(self, name):
        return f'{self.name}: {self.capital}'

    def edit_info(self, name, new_capital):
        pass

    @classmethod
    def dump_to_json(cls, countrier, filename):
        try:
            data = json.load(open(filename, encoding='utf-8'))
        except FileNotFoundError:
            data = []

        data.append({countrier.name: countrier.capital})

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)



    @classmethod
    def upload_group(cls, file):
        with open(file, 'r', encoding='utf-8') as f:
            print(json.load(f))


ctr1 = Countrier('Россия', 'Москва')

countr = [ctr1, ]
# Countrier.dump_to_json(a, 'ctr.json')
#
# Countrier.upload_group('ctr.json')
n = 0
while n != 6:
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

        coun = input("Введите название страны (с заглавной буквы): ")
        capit = input("Введите название столицы страны(с заглавной буквы): ")

        # c = str(f'{coun}:{capit}')
        ctr1.add_name(coun)
        ctr1.add_capital(capit)
        Countrier.dump_to_json(ctr1, 'ctr.json')
        print("Файл сохранён")

    elif n == 2:
        id = int(input("Введите индекс страны для удаления: "))
        ctr1.remove_countr(id)
        print(f"Страна {id} удалена")
    elif n == 3:
        name = input("Введите название страны (с заглавной буквы): ")

    elif n == 4:
        pass
    elif n == 5:
        print(Countrier.upload_group('ctr.json'))
    elif n == 6:
        print("Программа завершена")

