from fabrika import employee, valid


class Admininistr(employee.Employee):
    salary = valid.Valid()
    cod = valid.Valid()

    def __init__(self, cod, name, salary):
        super().__init__(cod, name)
        self.salary = salary

    def info(self):
        return (f'Заработная плата: {self.cod} - {self.name}\n'
                f'- Проверить сумму: {self.salary}')

