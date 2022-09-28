# Список : [-2, 5, 18, -11, 6]
# Вычислить количество отрицательных элементов в списке с помощью рекурсии.
# import os.path
#
# lst = [-2, 3, 8, -11, -4, 6]
#
#
# def count_negative(item_list):
#     count = 0
#     for item in item_list:
#         if item >= 0:
#             count = count
#         else:
#             count += 1
#
#     return count
# print(count_negative(lst))

# print("Вносим изменения")
# print("Опять вносим изменения")



# №2 (dz от 11.09.22 в Журнале)

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
#
# # ВТОРОЙ ВАРИАНТ:
#
# # test = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# # reg = r'((0[25]|14)/(06)/(2021))'
# # print(re.findall(reg,test))
#
# print("PyCharm")


# size = os.path.getsize(path)
# k_size = size // 1024
# print("Размер",k_size,"KB")
# c_time = os.path.getctime(path)
# print(c_time)
# print(time.strtime("%d.%m.%Y,%H:%M:%S",time.localtime(c_time)))
#
#
# ООП
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
#
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


text = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;"
with open("text1.txt", 'w',encoding='UTF-8') as f:
    print(f.write(text))
