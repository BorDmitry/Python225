from fabrika import employee,valid


class Sales_Represents(employee.Employee):
    cod = valid.Valid()
    commission = valid.Valid()

    def __init__(self, cod, name, salary, commission):
        super().__init__(cod, name)
        self.salary = salary
        self.commission = commission

    def info(self):
        return (f'Заработная плата: {self.cod} - {self.name}\n'
                f'- Проверить сумму: {self.salary + self.commission}')
