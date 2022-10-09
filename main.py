#    DZ from lesson
#   -----------------

# Список : [-2, 5, 18, -11, 6]
# Вычислить количество отрицательных элементов в списке с помощью рекурсии.

# import os.path
# lst = [-2, 3, 8, -11, -4, 6]
# def count_negative(item_list):
#     count = 0
#     for item in item_list:
#         if item >= 0:
#             count = count
#         else:
#             count += 1
#     return count
# print(count_negative(lst))
# -------------------------------------------------------------------------------------------

#  DZ от 11.09.22 в Журнале

# Найти дату в формате dd/vv/yyyy .
# В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021 были зафиксированы максимуьы ежедневных осадкод.
#
# ['02/06/2021','05/06/2021','14/06/2021']

# import re
# def test(name):
#     reg = r'((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(20[0-9][0-9]))'
#     return re.findall(reg,name)
#
# name = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# print(test(name))
#
# ВТОРОЙ ВАРИАНТ:
#
# # test = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# # reg = r'((0[25]|14)/(06)/(2021))'
# # print(re.findall(reg,test))
# ------------------------------------------------------------------------------------------------------------------


# size = os.path.getsize(path)
# k_size = size // 1024
# print("Размер",k_size,"KB")
# c_time = os.path.getctime(path)
# print(c_time)
# print(time.strtime("%d.%m.%Y,%H:%M:%S",time.localtime(c_time)))
#
# ------------------------------------------------------------------------------------------------------------------
#                 ООП
#              ---------
# class Point:
#     """"Класс для предоставления координат точек на плоскости"""
#
#     x = 1
#     y = 1
#
# p1 = Point()
# print(type(p1))
# Point.x = 100
# p1.x = 200
# print(p1.x,p1.y)
# print(id(p1))
# print(id(Point))
# # print(Point.__doc__)






# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные". center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self,first_name,birthday,):
#
# h1 = Human()
# h1.print_info("Юля","23.05.1986","45-46-98","Россия","Москва","Чистопрудный бульвар")
#
#     def set_name(self,name):  # установить имя
#         self,name =
# -------------------------------------------------------------------------------------
# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# print(p1.__dict__)
# # print(p1.x)
# print(getattr(p1,"x"))
# # print(p1,z)
# print(getattr(p1, "z", "Нет атрибута"))
# print(hasattr(p1, "z"))
# print(hasattr(p1, "y"))


# class Person:
#     skill = 10
#
#     def print_info(self):
#         print("Данные сотрудника:",self.name,self.surname)
#
#     def add_skill(self,k):
#         self.skill += k
#         print("Квалификация сотрудника:",self.skill, "\n")
#
#     class Robot:
#         k = 0
#
#         def __init__(self,name,surname):
#             self.name = name
#             print("Инициализация робота:",self.name)
#
#         def __del__(self):
#             print(self.name,"Выключается!")
#             Robot.k -= 1
#             if Robot.k == 0:
#                 print(self.name,"был последним.")
#             else:
#                 print("Работающихроботов осталось:", Robot.k)
#
#         def say_hi(self):
#             print(("Приветствую!Меня зовут:",self.name))
#
#
#             droid1 = Robot1("R2-D2")
#             droid1.say_hi()
#             print("Численность роботов",Robot.k)
#
#             droid2 = Robot2("C-3PO")
#             droid2.say_hi()
#             print("Численность роботов",Robot.k)
#
#             print(("Здесь роботы могут проделывать какуюто работу"))
#
#
#             class Car:
#                 def __init__(self,name,year,mode,hower,color,price):
#                    self.__name = name
#                    self.__year = year
#
#
#
#
#
#
#                     def print_info(self):
#                         print("Данные авто".center(40,"*"))
#                         print("Название модели": {self.__name})
#             Год выпуска: {self.__year}
#             Производитель: {self.__model}


# text = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;"
# with open("text1.txt", 'w', encoding='UTF-8') as f:
#     print(f.write(text))

# f = open(r'C:\Users\Dmitry\Scripts\HomeWork\text.txt', 'a', encoding='UTF-8')
# # f.write('Hello,\nWorld')
# f.write('\nnew text')
# f.close()

# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# print(len(f.readlines()))
# print(f.read(3))
# print(f.read())

# cnt = 0
# for l in f:
#     cnt += 1
# print(cnt)

# cnt = 0
# s = f.readline()
# while s != "":
#     s = f.readline()
#     cnt += 1
# print(cnt)

# print(f.readline())
# print(f.readline())
#
# print(f.readline())


#
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     @property
#     def coord_x(self):  # __get_x
#         print("Вызов __get_x")
#         return self.__x
#
#     @coord_x.setter
#     def coord_x(self, x):  # __set_x
#         print("Вызов __set_x")
#         self.__x = x
#
#     @coord_x.deleter
#     def coord_x(self):  # __del_x
#         print("Удаление свойства")
#         del self.__x
#
#
#     # coord_x = property(__get_x, __set_x, __del_x)
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# del p1.coord_x
# p1.coord_x = 7
# print(p1.__dict__)




# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, k):
#         self.__old = k
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
# p1 = Person('Irina', 26)
# print(p1.name)
# p1.name = 'Igor'
# del p1.name
# p1.old = '31'
# del p1.old
#
# p1.name = 'Irina'
# print(p1.__dict__)
# p1.old = '31'
# print(p1.__dict__)

# class Nunbers:
#     @staticmethod
#     def minimum(a, b, c, d):
#         minim = min(a, b, c, d)
#         return minim
#     @staticmethod
#     def maximum(a, b, c, d):
#         maxi = max(a, b, c, d)
#         return maxi
#
#     @staticmethod
#     def sred_arifm(a, b, c, d):
#         s_arif = (a + b + c + d)/4
#         return s_arif
#
#     @staticmethod
#     def factorial(a):
#         count = 1
#         for i in range(1, a + 1):
#             count = count * i
#         return count
#
#
#
# print("Минимальное число>", Nunbers.minimum(4, 5, 9, 2))
# print("Максимальное число>", Nunbers.maximum(4, 5, 9, 2))
# print("Среднеарифметическое число>", Nunbers.sred_arifm(4, 5, 9, 2))
# print("Факториал числа>", Nunbers.factorial(9))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#     @classmethod
#     def from_string(cls, data_as_string):
#         d, m, y = map(int, data_as_string.split('.'))
#         return cls(d, m, y)
#
#     @staticmethod
#     def is_date_valid(data_as_string):
#         if data_as_string.count('.') == 2:
#             d, m, y = map(int, data_as_string.split('.'))
#             return d <= 31 and m <= 12 and y <=3999
#
# dates =[
#     '30.12.2020',
#     '30-12-2020',
#     '01.31.2021',
#     '32.12.2022'
# ]
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print('Некорректная дата')


# d1 = Date.from_string('12.11.2022')
# print(d1.string_to_db())
#
# d2 = Date.from_string('30.12.2022')
# print(d2.string_to_db())

# string_date = '20.10.2022'
# d, m, y = map(int, string_date.split('.'))
# print(type(d), type(m), type(y))
# date1 = Date(d, m, y)
# print(date1.string_to_db())






#
#
#
#
#            2.10.22 методы в классах
#
#
#



# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счёт #{self.num} принадлежит {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счёт #{self.num} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         return rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счёта: {usd_val} {Account.suffix}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счёта: {eur_val} {Account.suffix}')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Инф о счёте')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению Вы не можете снять {val}')
#         else:
#             self.value -= val
#             print(f'{val} RUB было успешно снято')
#         self.print_balance
#
#     def add_money(self, val):
#
#         self.value += val
#         print(f'{val} RUB было добавлено')
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
#
# acc.add_percents()
#
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

#              Задача № 2
#
# import re
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps()
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должны быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise  TypeError("Паспорт должен быть строкой")
#
#     @property
#     def fio(cls):
#         return self.__fio
#
#     @fio.setter
#     def name(self, name):
#         self.__name = name
#
#
#
#
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return str.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#
#     @property
#     def weigth(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
# p1 = UserData("Волков Игорь Николаевич", 51, "1234 567890", 72.0)
# p1.fio = 'Соболев Игорь Николае'
#
#
#
#
#                   Задача / Рисование
#                ------------------------
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'

class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        print("Инициализатор базового класса Prop")
        if isinstance(sp, int) and isinstance(ep, int):
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты должны быть только целочисленными значениями")
            return False
        self._color = color
        self.__width = width

    def get_width(self):
        return self.__width

class Line(Prop):
    def __init__(self, *args):
        print('Переопределённый инициализатор line')
        super().__init__(*args)
        self.__width = 5
    def draw_line(self) -> None:
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.__width}')

class Rect(Prop):

    def __init__(self, sp, ep, color='red', width=1, bg='yellow'):
        super().__init__(sp, ep, color, width)
        self.background = bg

    def draw_rect(self) -> None:
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')


line = Line(Point(1, 2), Point(10, 20), 'green', 3)
line.draw_line()
print(line.__dict__)
# print(line._width)
# print(type(line))
rect = Rect(Point(30, 40), Point(70, 80))
rect.draw_rect()

# print(issubclass(Point, object))
# print(line.__dict__)




          #  Зад , Фигура

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             self.__width = 1
#             # raise ValueError
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника: ", end="")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# # rect.width = -5
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = 'red'
# print(rect.color)
# print(rect.area())




# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) and not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True





