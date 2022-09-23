# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Список : [-2, 5, 18, -11, 6]
# Вычислить количество отрицательных элементов в списке с помощью рекурсии.

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
#
# print("Вносим изменения")
# print("Опять вносим изменения")
#
#

# №2 (dz от 11.09.22 в Журнале)
# Найти дату в формате dd/vv/yyyy .
# В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021 были зафиксированы максимуьы ежедневных осадкод.
#
# ['02/06/2021','05/06/2021','14/06/2021']

import re
def test(name):
    reg = r'((0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(20[0-9][0-9]))'
    return re.findall(reg,name)

name = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
print(test(name))

# ВТОРОЙ ВАРИАНТ:

# test = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# reg = r'((0[25]|14)/(06)/(2021))'
# print(re.findall(reg,test))

print("PyCharm")