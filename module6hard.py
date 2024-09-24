from math import pi

class Figure:

    sides_count = 0

    def __init__(self, color = list, sides = list, filled = bool):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, b, g):
            self.__color = (r, g, b)

    @staticmethod
    def __is_valid_color(r, g, b):
        if 0 <= r <= 255 and 0 <= b <= 255 and 0 <= g <= 255:
            return True
        else:
            return False

    def get_color(self):
        return self.__color

    def set_sides(self, *args):
        new_sides = [*args]
        if isinstance(self, Cube):
            if self.__is_valid_sides(new_sides):
                self.__sides = new_sides
                return
            elif len(new_sides) == 1:
                self.__sides = []
                for i in range(0, self.sides_count):
                    self.__sides.append(new_sides[0])
                return
        if isinstance(self, Circle):
            if self.__is_valid_sides(new_sides):
                self.__sides = new_sides[0]
                return
        if isinstance(self, Triangle):
            if self.__is_valid_sides(new_sides):
                self.__sides = new_sides

    def __is_valid_sides(self, side_list):
        if len(side_list) == self.sides_count:
            for i in side_list:
                if i < 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if isinstance(self, Cube) or isinstance(self, Triangle):
            return sum(self.__sides)
        if isinstance(self, Circle):
            return self.__sides


class Cube(Figure):

    sides_count = 12

    def __init__(self, color, sides):
        side_cube = []
        if not(isinstance(sides, int)):
            sides = 1
        for i in range(0, self.sides_count):
            side_cube.append(sides)
        super().__init__(color, side_cube)
        self.__sides = side_cube

    def get_volume(self):
        return self.__sides[0] ** 3


class Circle(Figure):

    sides_count = 1

    def __init__(self, color, sides):
        if not (isinstance(sides, int)):
            sides = 1
        super().__init__(color, sides)
        self.__sides = sides

    def __radius(self):
        return self.__sides / (2 * pi)

    def get_square(self):
        return pi * (self.__radius() ** 2)

class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, sides = list):
        if isinstance(sides, list) and len(sides) == 3:
            pass
        else:
            sides = [1, 1, 1]
        super().__init__(color, sides)
        self.__sides = sides
        self.__a = self.__sides[0]
        self.__b = self.__sides[1]
        self.__c = self.__sides[2]
        self.__semiperimeter = len(self) / 2

    def get_square(self):
        return (self.__semiperimeter *
                (self.__semiperimeter - self.__a)*
                (self.__semiperimeter - self.__b)*
                (self.__semiperimeter - self.__c)) ** 0.5

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())