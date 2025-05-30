from abc import ABC, abstractmethod

from math import sqrt, pi


class LessThanZeroError(Exception):
    def __init__(self, message="Число больше или равно нулю!"):
        super().__init__(message)
    pass


class IrregularFigureError(Exception):
    def __init__(self, message="Неверная фигура"):
        super().__init__(message)
    pass


class Figure(ABC):

    @abstractmethod
    def _calculate_area(self) -> float:
        pass


class Circle(Figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise LessThanZeroError()
        self.radius = radius

    def _calculate_area(self) -> float:
        return pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

        self._validate(self.a, self.b, self.c)

    @staticmethod
    def _validate(a: float, b: float, c: float) -> None:
        if any(x <= 0 for x in [a, b, c]):
            raise LessThanZeroError()
        if not a + b > c and a + c > b and b + c > a:
            raise IrregularFigureError("Такого треугольника не существует")

    def _calculate_area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def check_right_triangle(self):
        conditions = [
            self.a ** 2 + self.b ** 2 == self.c ** 2,
            self.c ** 2 + self.b ** 2 == self.b ** 2,
            self.a ** 2 + self.c ** 2 == self.a ** 2,
        ]
        if any(conditions):
            return True
        return False


def calculate_area(figure: Figure) -> float:
    return figure._calculate_area()
