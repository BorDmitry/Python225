class Valid:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.__name} должно быть положительным значением ")
        instance.__dict__[self.__name] = value


class Employee:
    def __init__(self, cod, name):
        self.cod = cod
        self.name = name


class Admininistr(Employee):
    salary = Valid()
    cod = Valid()

    def __init__(self, cod, name, salary):
        super().__init__(cod, name)
        self.salary = salary

    def info(self):
        return (f'Заработная плата: {self.cod} - {self.name}\n'
                f'- Проверить сумму: {self.salary}')


class Wokers(Employee):
    cod = Valid()
    hour = Valid()

    def __init__(self, cod, name, hour):
        super().__init__(cod, name)
        self.hour = hour

    def info(self):
        return (f'Заработная плата: {self.cod} - {self.name}\n'
                f'- Проверить сумму: {self.hour * 20}')

class Sales_Represents(Employee):
    cod = Valid()
    commission = Valid()

    def __init__(self, cod, name, salary, commission):
        super().__init__(cod, name)
        self.salary = salary
        self.commission = commission



    def info(self):
        return (f'Заработная плата: {self.cod} - {self.name}\n'
                f'- Проверить сумму: {self.salary + self.commission}')


adm1 = Admininistr(1, 'Валерий Задорожный', 1500 )
print(f'Расчёт заработной платы')
print('=' * 45)
print(adm1.info())
print()
w1 = Wokers(2, 'Илья Кромин', 30)
print(w1.info())
print()
sal_r1 = Sales_Represents(3, 'Николай Хорольский', 1000, 250)
print(sal_r1.info())


# C:\Users\Dmitry\Scripts\HomeWork\venv\Scripts\python.exe C:/Users/Dmitry/Scripts/HomeWork/DZ_Salary_.py
# Расчёт заработной платы
# =============================================
# Заработная плата: 1 - Валерий Задорожный
# - Проверить сумму: 1500
#
# Заработная плата: 2 - Илья Кромин
# - Проверить сумму: 600
#
# Заработная плата: 3 - Николай Хорольский
# - Проверить сумму: 1250
#
# Process finished with exit code 0
