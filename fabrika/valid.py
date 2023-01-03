class Valid:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.__name} должно быть положительным значением ")
        instance.__dict__[self.__name] = value