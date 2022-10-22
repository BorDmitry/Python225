class Point3D:
    CH = "Коордю должна быть числом"# Вспом. класс
    RIGHT = "Правый операнд должен быть тпом данных Point3D"

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):          # для просмотра  координат вспомогательного класса Point
        return f'({self.x}, {self.y}, {self.z})'

    @staticmethod
    def __chek_value(v):
        return isinstance(v, int) or isinstance(v, float)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__chek_value(value):
            self.__x = value
        else:
            print(self.CH)

    @y.setter
    def y(self, value):
        if self.__chek_value(value):
            self.__y = value
        else:
            print(self.CH)

    @z.setter
    def z(self, value):
        if self.__chek_value(value):
            self.__z = value
        else:
            print(self.CH)

    def __add__(self, other):
            if not isinstance(other, Point3D):
                raise ValueError(self.RIGHT)
            return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый операнд д. б. типом данных Clock")
        return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый операнд д. б. типом данных Clock")
        else:
            return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)

     @staticmethod


pt1 = Point3D(12, 15, 18)
pt2 = Point3D(6, 3, 9)
print("Координаты первой точки:", pt1)
print("Координаты второй точки:", pt2)

pt3 = pt1 + pt2
print(f'Сложение кординат: ({pt3})')
pt4 = pt1 - pt2
print(f'разность коорд.:, ({pt4})')

pt5 = pt1 * pt2
print(f'разность коорд.:, ({pt5})')