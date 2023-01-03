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

# ---------------------------


# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.Intern = self.Intern()
#         self.Heed = self.Heed()
#
#     def show(self):
#         print("Employee list:")
#         print(f'Name: {self.name}')
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = "657"
#
#         def display(self):
#             print(f'Name: {self.name}')
#             print(f'Id: {self.id}')
#
#     class Heed:
#         def __init__(self):
#             self.name = "Alba"
#             self.id = "007"
#
#         def display(self):
#             print(f'Name: {self.name}')
#             print(f'Id: {self.id}')
#
#
# outer = Employee()
# outer.show()
# d1 = outer.Intern
# d2 = outer.Heed
# d1.display()
# d2.display()

# --------------------------------------------------

# 15.10.22

# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Class Outer")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Class Inner")
#
#         class InnerClass:
#             def show(self):
#                 print("Class InnerClass")
#
#
# outer = Outer()
# outer.show()
# inner1 = outer.inner
# inner1.show()
# inner2 = outer.inner.inner_inner
# inner2.show()


# ===========29.10.22=====================


# class Integer:
#     @classmethod
#     def verify_coords(cls, coord):
#         if not isinstance(coord, str):
#             raise TypeError(f"Координата{coord}должна быть числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "-" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_coords(value)
#         instance.__dict__[self.name] = value
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)


# ======================МЕТАКЛАССЫ======================


# class MyList(list):
#     def get_length(self):
#         return len(self)


# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst[0] = 3
# print(lst, lst.get_length())
#
#
# --------------------------------------------


# class MyMetaClass(type):
#     def __new__(cls, *args, **kwargs):
#         print("Создание нового объекта", args[0])
#         return super(MyMetaClass, cls).__new__(cls, *args, **kwargs)
#
#     def __init__(cls, *args, **kwargs):
#         print("Инициализация класса", *args[0])
#         super(MyMetaClass, cls).__init__(*args, **kwargs)
#
#
# class Student(metaclass=MyMetaClass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student("Anna")
# print('Имя студента: ', stud.get_name())
# print('Тип объекта Student:', type(stud))
# print('Тип класса Student:', type(Student))

# --------------СОЗДАНИЕ МОДУЛЕЙ--------------------------

# import math
# print(math.pi)


# [12:46] Козякина Елена

#
# from geometry import trian, sq, rect
# # import geometry
# # from geometry import *
#
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())
#
# --------------------------------------------
# 30/10/2022

# from car import electrocar
#
# def main():
#     e_car = electrocar.ElectroCar('Tesla', "T", 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if __name__ == '__main__':
#     main()
#

# _____________________________________________________________


# from shapes import rectangle, circle, cylinder
#
#
# circles = [circle.Circle(4), circle.Circle(2), circle.Circle(6), circle.Circle(8), circle.Circle(1)]
# rects = [rectangle.Rectangle(3, 7), rectangle.Rectangle(2, 7), rectangle.Rectangle(19, 12)]
# cylinders = [cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5), cylinder.Cylinder(9, 3), cylinder.Cylinder(5, 5)]
#
# circle_max_s = max(circles, key=lambda c: c.get_circle_area())
# rect_min_p = min(rects, key=lambda r: r.get_rect_perimetr())
# cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
# cylinder_v_avr = sum(cylinders_v) / len(cylinders_v)
# print(f"Окружность с наибольшей площадью: {circle_max_s.print_circle()} = {circle_max_s.get_circle_area()}")
# print(f'Прямоугольник с наименьшим периметром: {rect_min_p.print_rect()} = {rect_min_p.get_rect_perimetr()}')
# print(f"Средний объем цилиндров: {round(cylinder_v_avr, 2)}")
#

# _______________________________________________________________________________________________________________

# ___Сериализация


# import pickle
#
# filename = "basket.txt"
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': ['морковь'],
#     'бюджет': 100
# }
#
# with open(filename, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, 'rb') as fh:
#     shop_list_2 = pickle.load(fh)
#
# print(shop_list_2)

#
# --------------------------------------------------
# import pickle
#
#
# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     dct = {'first': '1', 'second': '2', 'third': '3'}
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nСловарь: {Test.dct}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
# # print(obj)
#
# d_save = pickle.dumps(obj)
# print(f"Сериализация в строку:\n{d_save}\n")
# d_read = pickle.loads(d_save)
# print(f'Десерализация в строку:\n{d_read}\n')

# import pickle
#
#
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
#
# print(item3.__dict__)
# print(item3)

#  12/11/22
# ========================================================
# import  pickle
#
#
# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename, encoding='utf-8')
#         self.count = 0
#
#     def read_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return f"{self.count}: {line}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename, encoding='utf-8')
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader("hello.txt")
# print(reader.read_line())
# print(reader.read_line())
# print(reader.read_line())
# new_reader = pickle.loads(pickle.dumps(reader)) #Сначало сохраняется внутри(dumps), затем считывается(loads) снаруже
# print(new_reader.read_line())
# print(new_reader.read_line())

# import json
#
# data = {
#     'first_name': 'Jane',
#     'last_name': 'Doe',
#     'hobbies': ('running', 'sky diving', 'singing'),
#     'age': 35,
#     'children': [
#         {
#             'first_name': 'Alice',
#             'age': 6
#         },
#         {
#             'first_name': 'Bob',
#             'age': 8
#         },
#     ],
# }
# print(data)
# with open('data_file.json', 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open('data_file.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)

# json_string = json.dumps(data,sort_keys=True)
# print(json_string)
#
# data = json.loads(json_string)
# print(data)

# x = {
#     "name": "Виктор"
# }
# y = {
#     "name": "Виктор"
# }
#
# print(json.dumps(x))
# print(json.loads(json.dumps(x)))
# print(json.dumps(y, ensure_ascii=False))
#

# --------------------------------------------------

# from random import choice
#
# # def gen_person():
# #     name = ''
# #     tel = ''
# #
# #     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# #     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# #
# #     while len(name) != 7:
# #         name += choice(letters)
# #     # print(name)
# #
# #     while len(tel) != 10:
# #         tel += choice(nums)
# #     # print(tel)
# #
# #     person = {
# #         'name': name,
# #         'tel': tel
# #     }
# #     return person
# #
# #
# # def write_json(person_dict):
# #     try:
# #         data = json.load(open('persons.json'))
# #     except FileNotFoundError:
# #         data = []
# #
# #     data.append(person_dict)
# #
# #     with open('persons.json', 'w') as f:
# #         json.dump(data, f, indent=2)
# #
# #
# # # for i in range(5):
# # #     persons.append(gen_person())
# # #     print(persons)
# # #
# # #     # data[num] = person_dict
# #
# # for i in range(5):
# #     write_json(gen_person())
# #
#
#
# # ------------------------------------------------------------
# # var 1
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ", "
#         return f"Студент: {self.name} {a[:-2]}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': stud.name, 'marks': stud.marks})
#
#         # data = {'name': stud.name, 'marks': stud.marks}   # 1й метод
#
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + "\n"
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def cheng_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_group(cls, file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1, st2]
# # Student.load_from_file('student.json')
# # Student.dump_to_json(st1, 'student.json')
# # Student.dump_to_json(st2, 'student.json')
#
#
# my_group = Group(sts, "ГК Python")
# print(my_group)
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 4)
# # print(st1)
# # print(st1.average_mark())
#
# # my_group.add_student(st3)
# # print(my_group)
# # my_group.remove_student(1)
# # print(my_group)
# group22 = [st3]
# my_group2 = Group(group22, "ГК Web")
#
# print(my_group2)
#
# # Group.dump_group('group.json', my_group2)
# Group.upload_group('group.json')
# # Group.cheng_group(my_group, my_group2, 0)
# # print(my_group)
# # print(my_group2)
# ================================================
#     ё
#       й ц у к е н г ш щ з х ъ
#       ф ы в а п р о л д ж э
#        я ч с м и т ь б ю
# -----------------------------------------------

#   var 2   (копия кода преродавателя)

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ", "
#         return f"Студент: {self.name} {a[:-2]}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#         data.append({'name': stud.name, 'marks': stud.marks})
#         with open(filename, 'w') as f:
#             json.dumps(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             json.dumps(json.load(), f)
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + "\n"
#         return f"Группа: {self.group}\n{a}"

#     def add_student(self, student):
#         self.students.append(student)

#     def remove_student(self, index):
#         return self.students.pop(index)

#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))

#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_group(cls, file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1, st2]
#
# Student.dump_to_json(st1, 'student.json')
# Student.dump_to_json(st2, 'student.json')
# # my_group = Group(sts, "ГК Python")
# # print(my_group)
# # my_group.add_student(st3)
# # print(my_group)
# # my_group.remove_student(1)
# # print(my_group)
# #
# # group22 = [st2]
# # my_group2 = Group(group22, "ГК Web")
# # print(my_group2)
# #
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)
#
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(3)
# print(st1)
# st1.edit_mark(2, 4)
# print(st1)
# print(st1.average_mark())

# ==================================================

# import requests
# import json
#
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# # print(todos[:10])
# # print(type(todos))
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
# print(todos_by_user)
#
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
# max_users = " and ".join(users)
#
# s = "s" if len(users) > 1 else ""
# print(f"user {users} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_file.json', 'w') as data_file:
#     filtered_todos = list(filter(keep, todos))
#     # print(filtered_todos)
#     json.dump(filtered_todos, data_file, indent=2)
#
# with open('filtered_file.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)

# ---------------------------------------
#  19/11/22
#      CSV  ()
#   data.csv
# csv.reder
# csv.writer

# csv.Dict.Reader
# csv.Dict.Writer
# import csv

# with open("data.csv") as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"   {row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")
#

# with open("data.csv") as r_file:
#     file_reader = csv.DictReader(r_file)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1
# print(f"Всего в файле {count} строки.")
# ------------------------------------------------------
# with open("data.csv") as r_file:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, fieldnames= file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1
# --------------------------------------------------------
# (_19video__02:30)

# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator='\r')
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "10"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

# ------------------------------------------------------------
# import csv
#
# import json

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=",", lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
#
# with open('data_new.csv') as f:
#     print(f.read())


# with open('student1.csv', 'w') as f:
#     name = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator='\r', fieldnames=name)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     file_writer.writerow({"Имя": "Вова", "Возраст": "14"})


# data = [{
#
# 'hostname': 'sw1',
#
# 'location': 'London',
#
# 'model': '3750',
#
# 'vendor': 'Cisco'
#
# }, {
#
# 'hostname': 'sw2',
#
# 'location': 'Liverpool',
#
# 'model': '3850',
#
# 'vendor': 'Cisco'
#
# }, {
#
# 'hostname': 'sw3',
#
# 'location': 'Liverpool',
#
# 'model': '3650',
#
# 'vendor': 'Cisco'
#
# }, {
#
# 'hostname': 'sw4',
#
# 'location': 'London',
#
# 'model': '3650',
#
# 'vendor': 'Cisco'
#
# }]
#
# with open('dictwriter.csv', 'w') as f:
#     # Создаём строку из ключей 0-го индекса списка
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()),delimiter=";", lineterminator='\r')
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# --------------------------------------------
#  вставка из main.py (Homework)
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

# f = open(r'C:\Users\Dmitry\Scripts\Python\text.txt', 'a', encoding='UTF-8')
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
#                                   Потомок
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


# ПОЛИМОРФИЗМ
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

#------------------------------------ФУНКТОРЫ--------------


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


#--------------------30.10.2022-------------

# Модули и наследование


# from bs4 import BeautifulSoup
# import requests
# import csv
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_="plugin-section")[1]
#     plugins = p1.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get('href')
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


#---------------------------------------------------------
# from D_Z_4_ParsingPages import Parser
#
#
# def main():
#     for i in range(1, 3):
#         pars = Parser(f"https://www.ixbt.com/live/index/news/page{i}", "news_of_day.txt")
#         pars.run()
#
#
# if __name__ == '__main__':
#     main()

 # конец вставки из main.py (Homework)






#  20/11/22
# -----------


#from bs4 import BeautifulSoup


# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name")
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find("div", class_='links').text
# row = soup.find("div", {"class": "name"})
# row = soup.find("div", {"data-set": "salary"})
# row = soup.find("div", text="Alena").parent
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)


# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all('div', class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

#-----------------------------------------------------
# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)
# --------------------------------------------------
# from bs4 import BeautifulSoup
#
# import requests
# import re
# import csv

 #     1й способ  ( вывод всего контента )
# req = requests.get("https://ru.wordpress.org/")
# req.encoding = 'utf-8'
# print(req.content)

# def main():
#     url = "https://ru.wordpress.org/"
#     (get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# 2й способ ( вывод конкретных мест из html- разметки )


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_="plugin-section")[1]
#     plugins = p1.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a")['href']
#         url = plugin.find("h3").find("a").get('href')
#         rating = plugin.find('span',  class_="rating-count").find("a").text
#         r = refined(rating)
#
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
#     # return len(plugins)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     (get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()





#-------------------------------------------
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refind(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find("h3")
#         # url = plugin.find("h3").find("a")['href']
#         url = plugin.find("h3").find("a").get('href')
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refind(rating)
#
#     # return len(plugins)
#
#         data ={'name': 'url'}
#
# def main():
#     url = "https://ru.wordpress.org/plugins"
#     get_data(get_html(url))
#
# if __name__== '__main__':
#     main()


#-----------------------------------------
# 26/11/2022     |   27/11  изменения в строке url для пагинации нескольких страниц

# from bs4 import BeautifulSoup
#
# import requests
#
# import csv



# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def write_csv(data):
#     with open('plugins1.csv', 'a', encoding='utf-8') as f:        # ДОБАВИЛ encoding и не выдаёт ошибок при прочтении
# writer = csv.writer(f, lineterminator="\r", delimiter=";")        # спецсимволов(сердечко, галочка)
# #         writer.writerow((data['name'],
# #                          data['url'],
# #                          data['snippet'],
# #                          data['active_install'],
# #                          data['tested']))
# #
#
#
# def refine_cy(s):
#     return s.split()[-1]  #   Для принятия строки,разбиения её методом split на массив по
#                           # символу пробел и взятия только по индексу [-1] последнего числа
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#         try:
#             url = el.find('h3').find('a').get('href')
#         except ValueError:
#             url = ''
#         try:
#             snippet = el.find('div', class_='entry-excerpt').text.strip()
#         except ValueError:
#             snippet = ''
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ''
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ''
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active_install': active,
#             'tested': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(1, 3):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
# if __name__ == '__main__':
#     main()

#___________________________________________________________
                            #  Парсинг с классами
#
# from parse import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#     # pars.get_html()
#
#
# if __name__ == '__main__':
#      main()

#-----------------------------------------------------------

                  # Взатмосвязь клиента с СЕРВЕРОМ


# import socket
# from view import index, blog
# #
# # Съимитируем , что есть какая то страница
# #для этого  создадим словарь с url-адресами
#
# URLS = {
#     "/": index,
#     "/blog": blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()  # разбиение данных по пустой строке
#     method = parsed[0]        # GET
#     url = parsed[1]           # / или /blog
#     return method, url
#
#
# def generate_headers(method, url):  #  метод для проверки приходящих аргументов-методов
#     if method != "GET":
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:             #  Если url не находится в нашем словаре URLS
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page not found!</h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Method not Allowed!</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):          #  МЕТОД ДЛЯ СОЕДИНЕНИЯ ДАННЫХ
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)                   # создадит тело ответа
#     return (headers + body).encode()              #  ЧТОБЫ  могли разкодРАЗКОДИРОВАТЬ ДАННЫЕ
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Какой протакол используется, указать двунаправленный сокет
#     server_socket.bind(('127.0.0.1', 5000))      # инициализация адреса локального сервера(IP либо доменное имя:localhost, порт)
#     server_socket.listen()                                             # сервер ожидает приёма
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())  #переменная = метод
#         client_socket.sendall(response)  # отправить данные в сокет
#         client_socket.close()            # сокет после работы нужно закрыть
#
#
# if __name__ == '__main__':
#     run()


#_______________________________________________________________

# from bs4 import BeautifulSoup
# import requests
# import csv
# import re
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


#---------------------------------------------------------------------------------------
# 04.12.2022

# import sqlite3 as sq
#
#
# with sq.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE users")
#
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # data TEXT
#     # )""")
#-------------------------------------------------------
#10.12

# import sqlite3 as sq
#
#
# with sq.connect("users2.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT '+79090000000',
#     age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
#     email TEXT UNIQUE
#     )
#     """)
#     cur.execute("""
#       INSERT INTO  person(email, name, age)
#       VALUES('igor@mail.com', 'Игорь', 20 )
#       """)

    # cur.execute("""
    # INSERT INTO  person
    # VALUES(1, 'Ирина', '+75052031177', 23, 'irina@mail.com')
    # """)


#--------------------------------------------------------------------------------------------------------
# 11.12.22
# import sqlite3 as sq
#
#
# with sq.connect("users1.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT '+79090000000',
#     age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
#     email TEXT UNIQUE
#     )
#     """)

    # # Переименовать, Изменение таблицы:
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT NOT NULL;
    # """)

    # cur.execute("""
    #    ALTER TABLE person_table
    #    RENAME COLUMN address TO home_address;
    #    """)
    #
    # """)

    # cur.execute("""
    #     INSERT INTO person_table
    #     VELUES (1, 'Ирина', '+7505520457658', 23, 'irina@gmail.com')
    #     """)

    # cur.execute("""
    # DROP TABLE person_table;
    # """)

    # cur.execute("""
    # INSERT INTO person
    # VALUE (1, '', '+75053564632', 23, 'irina2@gmail.com')
    # """)

#---------------------------------------------
#  11.12.22

# import sqlite3 as sq
#
#
# with sq.connect("db_4.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5;
#     """)
#
#     # res = cur.fetchall()  # МЕТОД ВОЗВРАЩАЕТ ВСЁ, ЧТО В ТЕКУЩЕМ ЗАПРОСЕ
#     # print(res)
#     # res = cur.fetchone()   # возвращается только одна первая строка
#     res2 = cur.fetchmany(2)
#     # print(res)
#     print(res2)
#
#     # res = cur.fetchall()
#     # print(res)
#
#     # for res in cur:
#     #     print(res)

#-------------------------------------------------------------------------------

# 18.12.22

# import sqlite3 as sq

# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]

# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#         CREATE TABLE IF NOT EXISTS cars (
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#         UPDATE cars SET price = price + 100;
#         """)
#     con.commit()
# except sq.Error as e:
#     if con:  # если сое
#         con.rollback()   # при ошибке откатывается до состояния BEGIN и изменения вноситься не будут
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()



# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
    # cur.execute("UPDATE cars SET price =:Price WHERE model LIKE 'B%'",{'Price': 0})

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

#     for car in cars:
#         cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # con.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
    # con.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
    # con.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
    # con.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
    # con.execute("INSERT INTO cars VALUES(5, 'Audy',52000)")






#con.commit(0 - сохраняет все изменения в базу данных
#con.close() - закрывает соединение с БД

# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     )
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец',1000)")
#     last_row_id = cur.lastrowid # возвращает id последней записи
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))



#--------------------------------------------------------------------
# 24.12.22

# import sqlite3 as sq

# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     # print(con.row_factory)
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users3(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)
#
#     cur.execute("SELECT ava FROM users3 LIMIT 1")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)


    # img = read_ava(1)
    # if img:
    #     binary = sq.Binary(img)
    #     cur.execute("INSERT INTO users3 VALUES ('Илья', ?, 1000)", (binary,))


    # cur.execute("SELECT model, price FROM cars")
    # rows = cur.fetchall()  # получить все данные из текущ. запроса
    # rows = cur.fetchmany(5)
    # for res in cur:
    #     print(res['model'], res['price'])

#-----------------------------------

# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     # with open("sql_dump.sql", "w") as f:
#     #     for sql in con.iterdump():
#     #         f.write(sql)
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)


#--------------------------------------

# data = [('car', "Машина"), ('house', 'дом'), ('tree', 'дерево'), ('color', 'цвет')]
#
# con = sq.connect(':memory:')
# with con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     ru TEXT
#     )""")
#
#     cur.executemany("INSERT INTO dict VALUES (?, ?)", data)
#
#     cur.execute("SELECT ru FROM dict WHERE eng")

#--------------------------------

import os

from models.database import DATABASE_NAME
import create_database as db_creator

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
