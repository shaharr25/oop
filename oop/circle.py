from shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, color, radios):
        """
        initializer
        :param color, radios:
        """
        super().__init__(color)
        self.radios = radios

    def get_area(self):
        """
        A function that gets the area of the circle
        :return: the area of the circle
        """
        return self.radios * self.radios * pi

    def get_perimeter(self):
        """
        A function that gets the perimeter of the circle
        :return: the perimeter of the circle
        """
        return 2 * pi * self.radios

    def get_radios(self):
        """
        A function that gets the radios of the circle
        :return: the radios of the circle
        """
        return self.radios

    def set_radios(self, radios):
        """
        A function that sets the radios of the circle
        :return:
        """
        self.radios = radios
