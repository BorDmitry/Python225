# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Список : [-2, 5, 18, -11, 6]
# Вычислить количество отрицательных элементов в списке с помощью рекурсии.

lst = [-2, 3, 8, -11, -4, 6]


def count_negative(item_list):
    count = 0
    for item in item_list:
        if item >= 0:
            count = count
        else:
            count += 1

    return count
print(count_negative(lst))

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#



    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyChaww.jetbrains.com/help/pycharm/
