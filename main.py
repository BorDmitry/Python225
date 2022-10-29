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
#                          ООП
#                       ---------
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

# ---------------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------


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
# ----------------------------------------------
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


#---------------------------------------------------------
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
#-----------------------------------------------------------


# coord_x = property(__get_x, __set_x, __del_x)
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# del p1.coord_x
# p1.coord_x = 7
# print(p1.__dict__)


#--------------------------------------------------------------

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



#----------------------------------------------------------


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
#-------------------------------------------------------------------------


# print("Минимальное число>", Nunbers.minimum(4, 5, 9, 2))
# print("Максимальное число>", Nunbers.maximum(4, 5, 9, 2))
# print("Среднеарифметическое число>", Nunbers.sred_arifm(4, 5, 9, 2))
# print("Факториал числа>", Nunbers.factorial(9))

#-----------------------------------------------------------------------------
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


#-----------------------------------------------------------------
#
#
#
#            2.10.22 методы в классах
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
#---------------------------------------------------------------------------


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
#---------------------------------------------------------------


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
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
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
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
# p1 = UserData("Волков Игорь Николаевич", 51, "1234 567890", 72.0)
# p1.fio = 'Соболев Игорь Николае'
# print(p1.__dict__)
# print(p1.fio)
# p1.old = 35
# p1.password = '4567 123456'
# p1.weight = 70.0
# print(p1.__dict__)
#---------------------------------------------------------------------------------


#                   Задача / Рисование
#                ------------------------


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'

# def is_int(self, sp, ep):
#     if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#         print("Координаты должны быть только целочисленными значениями")
#     else:
#         self._sp = sp
#         self._ep = ep


# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         print("Инициализатор базового класса Prop")
#         # if isinstance(sp, int) or isinstance(ep, int):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print('Переопределённый инициализатор line')
#         super().__init__(*args)
#         self.__width = 5
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.__width}')
#
#
#
# class Rect(Prop):
#
#     def __init__(self, sp, ep, color='red', width=1, bg='yellow'):
#         super().__init__(sp, ep, color, width)
#         self.background = bg
#
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width}, {self.background}')
#
#
# line = Line(Point(1, 2), Point(10, 20), 'green', 3)
# line.draw_line()
#
# # print(line._width)
# # print(type(line))
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# print(issubclass(Point, object))

#--------------------------------------------------------------------------

#  Зад: Фигура

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

#---------------------------------------------------------------------------


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#
# class Line(Prop):
#
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#
# class Rect(Prop):
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10.2, 20), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(7, 9), Point(12, 15))
# rect.draw_rect()
#
# rect.set_coords(Point(30.5, 40.2), Point(50, 60))
# rect.draw_rect()

#------------------------------------------------------------------------


# 09.10.2022
# -------------


# class Rect:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, w, h, bg):
#         super().__init__(w, h)
#         self.fon = bg
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'рамка: {self.fon}')
#
#
# class RectBorder(Rect):
#     def __init__(self, w, h, br):
#         super().__init__(w, h)
#         self.border = br
#
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка(border): {self.border}')
#
#
# shape1 = RectFon(400, 200, 'yellow')
# shape1.show_rect()
# #
# shape2 = RectBorder(600, 300, '1px solid red')
# shape2.show_rect()

#-------------------------------------------------------------

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
#
# v = Vector([1, 2, 3, 4, 5])
# print(v)
# print(type(v))


#--------------------------------------------------------------
                  # Перегрузка методов


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep


# class Line(Prop):
#
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coords(self, sp, ep = None):
#         if ep is None:
#             self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10, 20), Point(100, 200))
# line.draw_line()
#
# line.set_coords(Point(-10, -20))
# line.draw_line()

#-------------------------------------------------------------------


                        #  Абстрактные методы


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
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определён метод drow()")
#
# class Line(Prop):
#     def draw(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#     pass
#     # def draw(self) -> None:
#     #     print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Ellipse(Prop):
#     def draw(self) -> None:
#         print(f'Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()


#-------------------------------------------------------------------------------------------

                            #Задача  Стол


# import math
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):      # АБСТРАКТНЫЙ МЕТОД
#         raise NotImplementedError("В дочернем классе должен быть определён метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(math.pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())


#------------------------------------------------------------------------
                # АБСТРАКТНЫЙ КЛАСС


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")  # или pass
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещён e2-e4")
#
# q = Queen()
# q.draw()
# q.move()


  #     Абстрактный класс Валюта

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     sufffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.sufffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print('*' * 30)
# for elem in d:
#     elem.print_value()
#     print(f'={elem.convert_to_rub():.2f} RUB')
# print()
# for elem in e:
#     elem.print_value()
#     print(f'={elem.convert_to_rub():.2f} RUB')


#-------------------------------------------------------------------


                  # Интерфейс
# Это абстр. класс у котю ни одим из астрактных м
#
# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("display1()")
#
# class GranChild(Child):
#     def display2(self):
#         print("display2()")


# gc = GranChild()
# gc.display1()
# gc.display2()


#----------------------------------------------------------------------------------


                    # 15.10.22 Вложенне классы


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_metod(cls):
#         print("Я метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Обычный метод")
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Я метод внутреннего класса")
#
# aut = MyOuter('внешний')
# inner = aut.MyInner("внутренний")
# inner.inner_method()

#-------------------------------------------------------------------

# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print(f'Name: {self.name}')
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print(f'Name: {self.name}')
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# print(g.name)


# class Computer:
#
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#

# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())



#                  Работа и с наследованием и с вложенными классами:


# class Basse:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def displey(self):
#         print("Базовый класс")
#
#     class Inner:
#         def displey1(self):
#             print("Вложенный класс в базовый")
#
#
# class Sub_Class(Basse):
#     def __init__(self):
#         print("Дочерний класс")
#         super().__init__()
#
#     class Inner(Basse.Inner):
#         def display2(self):
#             print("Вложенный класс в дочерний")
#
# a = Sub_Class()
# a.displey()
# # b = a.db
# b = Sub_Class.Inner()
# #
# b.displey1()
# b.display2()
#
# # b.displey1()
# # b.display2()
#--------------------------------------------------------------------------
#
#                            Множественное наследование.
# #                                   Потомок
#
#
# class Creature:
#     def __init__(self, name):
#         self.name = name
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is slipping')
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# b = Dog("Buddy")
# b.sleep()
# b.play()
# b.bark()
#----------------------------------------------------------------------------

# class A:
#     # def __init__(self):
#     #     print("Инициализатор класса А")
#
#    pass
# class AA:
#     # def __init__(self):
#     #     print("Инициализатор класса АA")
#     def hi(self):
#         print("AA")
# class B(A):
#     # def __init__(self):
#     #     # super().__init__()
#     #     print("Инициализатор класса B")
#     # def hi(self):
#     #     print("B")
#     pass
# class C(AA):
#     # def __init__(self):
#     #     # super().__init__()
#     #     print("Инициализатор класса C")
#     def hi(self):
#         print("C")
# class D(B, C):
#
#     # def __init__(self):
#     #     B.__init__(self)
#     #     C.__init__(self)
#     #     print("Инициализатор класса D")
#     pass
# d = D()
# print(D.mro())
# print(D.__mro__)
# d.hi()

#--------------------------------------------------------------------------------


# class Point:                            # вспомогат. класс
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):                  # для просмотра  координат вспомогательного класса Point
#         return f'({self.x}, {self.y})'
#
#
# class Styles:
#     def __init__(self, color='red', width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.__mro__)





# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubclass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclasslog = MySubclass()
# subclasslog.display("Эта строка будет отображаться и записываться в файл")
#

#class Goods:
#....
#class MixinLog:
#...
#class Notebook(Goods, MixinLog)
# pass




#-----------------------------------------------------------------------------

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть целым числом')
#
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60    # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         self.value = value
#         self.key = key
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise TypeError('Часы должны быть целым числом')
#         if self[key] == "hour":
#             return self.value
#         elif self.key == "min":
#             return (self.sec // 60) % 60
#         elif self.key == "sec":
#             return self.sec % 60
#         return "Неверный ключ"
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec * other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec % other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec // other.sec)
#
#     def __imul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec * other.sec)
#
#     def __iadd__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __isub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec - other.sec)
#
#     def __imod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec % other.sec)
#
#     def __ifloordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд д. б. типом данных Clock")
#         return Clock(self.sec // other.sec)
#
#     def __eq__(self, other):
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 12
# print(c1["hour"], c1["min"], c1["sec"])
# c1 = Clock(40)
# c2 = Clock(100)
# c4 = Clock(300)
# print(c4.get_format_time())
# c3 = c4 - c2
# print(c3.get_format_time())
# c5 = c3 * c4
# print(c5.get_format_time())
# c6 = Clock(500)
# print(c6.get_format_time())
# c7 = c6 % c1
# print(c7.get_format_time())
# c8 = c1 // c7
# print(c8.get_format_time())
# c9 = c7 - c8
# print(c9.get_format_time())
# c10 = c9 * c8
# print(c10.get_format_time())
# c10 += c9
# print(c10.get_format_time())
# c10 -= c8
# print(c10.get_format_time())
# c10 //= c1
# print(c10.get_format_time())
# # c1 %= c9
# # print(c1.get_format_time())
# c2 = Clock(4)
# print(c2.get_format_time())
#
# if c1 == c2:
#     print("Время равно")
#
# if c1 != c2:
#     print("Время не равно")
# if c2 < c1:
#     print("Время второе меньше")
#


#                            16.10.22 Перегрузка операторов
#--------------------------------------------------------------------------------

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item <= len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотриц. числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым неотриц. числом")
#         del self.marks[key]
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)


#                                         ПОЛИМОРФИЗМ
# --------------------------------------------------------------------------

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я кот.Меня зовут {self.name}. Мне {self.age} года."
#     def make_sound(self):
#         return f'Кот мяукает'
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я пёс.Меня зовут {self.name}. Мне {self.age} года.'
#     def make_sound(self):
#         return f'Пёс гавкает.'
#
#
# c1 = Cat("Рыжик", 2.5)
# d1 = Dog("Барбос", 4)
# for i in [c1, d1]:
#     print(i.info(), '\n', i.make_sound())


#   video #13 /2:24----------------------------------------------------------------------
# class Human:
#     def __init__(self, lastname, name, age):
#         self.lastname = lastname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'\n{self.lastname} {self.name} {self.age}', end='')
#
#
# class Student(Human):
#     def __init__(self, lastname, name, age, speciality, group, make):
#         super().__init__(lastname, name, age)
#         self.speciality = speciality
#         self.group = group
#         self.make = make
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.group} {self.make}', end='')
#
#
# class Teacher(Human):
#     def __init__(self, lastname, name, age, subject, exp):
#         super().__init__(lastname, name, age)
#         self.subject = subject
#         self.exp = exp
#
#     def info(self):
#         super().info()
#         print(f' {self.subject} {self.exp}', end='')
#
#
# class Graduate(Student):
#     def __init__(self, lastname, name, age, speciality, group, make, protect):
#         super().__init__(lastname, name, age, speciality, group, make)
#         self.protect = protect
#
#     def info(self):
#         super().info()
#         print(f' {self.protect}',end='')
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for k in group:
#     k.info()



#23.10.22



# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
# cat = Cat("Пушок")
# print(cat)





# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
# p = Point(5, 7, 9)
# print(len(p))



# import math
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# # pt.z = 5
# # print(pt.__dict__)
# pt.length = 10
# print(pt.x, pt.y, pt.length)



# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#
# pt = Point(10, 20)
# pt2 = Point2D(10, 20)
#
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())

# --------------------------------------------------

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     # def __init__(self, x, y):
#     #     self.x = x
#     #     self.y = y
#     pass
#
#
# pt = Point(1, 2)
# pt2 = Point3D(10, 20)
# pt2.z = 30
# print(pt2.z)
# print(pt2.__dict__)

#------------------------------------ФУНКТОРЫ----------------------------------------------


# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c2()
#----------------------------------------------------------


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# print(s1("  ?Hello World!  "))
#
# -----------------------------------------------------------
#   КЛАСС КАК ДЕКОРАТОР
#
#
# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("Перед вызовом функции")
#         self.func()
#         print("После вызова функции")
# @MyDecorator
# def func1():
#     print("func")
#
#
# func1()


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print(("перед выз функ"))
#             print(self.name)
#             func(a, b)
#             print('после выз функции')
#
#         return wrap
#
# @MyDecorator("test2")
# def add(a, b):
#     print(a, b)
# #
#
#
#
# add(2, 5)

#     ДЕКОРАТОРЫ КЛАССОВ
# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print('Инициадизатор ActualClass')
#
#     def quad(self, value):
#         return value * 4
#
#
#
# obj = ActualClass()
#
# print(obj.quad(4))
# print(obj.doubler(5))

#----------------------------------------------------------------

# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def get(self):
#         return self.__value
#
#     def set(self, value):
#         self.value = value
#
# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     @property
#     def name(self, value):
#         self.__name = value
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def surname(self, value):
#         self.__surname = value
#
#     @surname.setter
#     def name(self, value):
#         self.__name = value
