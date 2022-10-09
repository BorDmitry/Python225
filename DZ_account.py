class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix = 'EUR'

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f'Счёт #{self.num} принадлежит {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.num} был закрыт.')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_eur_rate(cls, rate):
        return rate

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.name = name


    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счёта: {usd_val} {Account.suffix}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счёта: {eur_val} {Account.suffix}')

    def print_balance(self):
        print(f'Текущий баланс {self.value} {Account.suffix}')

    def print_info(self):
        print(f'Инф о счёте')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)

    def add_percents(self):
        self.value += self.value * self.percent
        print('Проценты начислены')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f'К сожалению Вы не можете снять {val}')
        else:
            self.value -= val
            print(f'{val} RUB было успешно снято')
        self.print_balance

    def add_money(self, val):

        self.value += val
        print(f'{val} RUB было добавлено')


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_info()

acc.set_name()
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
