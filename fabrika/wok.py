from fabrika import employee, valid


class Wokers(employee.Employee):
    cod = valid.Valid()
    hour = valid.Valid()

    def __init__(self, cod, name, hour):
        super().__init__(cod, name)
        self.hour = hour

    def info(self):
        return (f'Заработная плата: {self.cod} - {self.name}\n'
                f'- Проверить сумму: {self.hour * 20}')
