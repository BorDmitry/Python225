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


# [10:47] Козякина Елена
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p1.z = 2
# print(p1.z)
# print(p1.__dict__)

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#
#     @property
#     def name(self):
#         return self.name
#
#     @name.setter
#     def name(selfself,n):
#         self.name = n
#
#     @name.deleter
#     def name(self):
#         del self.name
#
# p1 = Person['Irina', 26]
# print(p1.name)
# p1.name = 'Igor'
# del p1.name
# print(p1.__dict__)
# p1.old = '31'
# del p1.old
# print(p1.__dict__)
#

# class Nunbers:
#     @staticmethod
#     def minimum(a,b,c,d):
#         min = min(a,b,c,d)
#         return min
# print("Минимальное число>", Nunbers.minimum(4,5,9,2))

# f = open('text.txt', 'r')


            # Д.Задание из класса
           # -------------------------
class Weight:
    def __init__(self, k=0):
        self.__k = k

    @ property
    def kg_k(self):
        return self.__k

    @kg_k.setter
    def kg_k(self, k):
        if isinstance(k, (int, float)):
            self.__k = k
        else:
            print("Килограммы должны быть заданны числами")

    def to_pounds(self):
        return round(self.__k * 2.205, 2)


w1 = Weight(12)
print(w1.kg_k, "кг => ", end='')
print(w1.to_pounds(), "фунтов")
w1.kg_k = 41
print(w1.kg_k, "кг => ", end='')
print(w1.to_pounds(), "фунтов")
w1.kg_k = "sixty"
print(w1.kg_k, "кг => ", end='')
print(w1.to_pounds(), "фунтов")



           # 2.10.22 методы в классах

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix = 'EUR'
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
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_eur_rate(cls, value, rate ):
#         return value * rate
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
#     def add_money(self, ):
#         self.value += val
#         print(f'{val} RUB было добавлено')
#
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





             # Задача № 2

# import re
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#
#         self.__fio = fio.split()
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
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
# p1 = UserData("Волков Игорь Николаевич", 51, "1234 567890", 72.0)



