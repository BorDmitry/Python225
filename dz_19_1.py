# text = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;"
# with open("text1.txt", "w") as f:
#     f.write(text)
#
# pos1 = int(input("Введите индекс первой строки для замены"))
# pos2 = int(input("Введите индекс второй строки для замены"))
#
# if 0 <= pos1 <= len(text) and 0 <= pos2 <= len(text) and pos1 != pos2:
#     read_file

my_file = open('text1.txt', 'w')
my_file.write(("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;"))
my_file.close()

my_file =open("text1.txt", 'r')
a = my_file.readlines()
print(a)

if 0 <= pos1 <= len(text) and 0 <= pos2 <= len(text) and pos1 != pos2:
#     a[1] = a[2]:
    for pos in range(len(a)):
        c = a[pos1], a[pos1] = a[pos2], a[pos2] = c
print(a)
my_file.close()

my_file = open('text1.txt','w')
my_file.writelines(a)
my_file.close()