from rectangle import Rectangle
from circle import Circle
from square import Square
import random

COLORS = ["red", "yellow", "pink", "green", "blue", "orange", "grey", "black"]


class ShapeContainer:
    def __init__(self):
        """
        initializer

        """
        self.shape_list = []
        self.color_counter = {}

    def generate(self, x):
        """
        creates x random shapes(square/rectangle/circle)
        with random color, length and width
        :param x:
        :return:
        """
        for i in range(0, x):
            type_num = random.randint(1, 3)
            color = COLORS[random.randint(0, 7)]
            length = random.randint(1, 10)
            width = random.randint(1, 10)
            if type_num == 1:
                self.shape_list.append(Square(color, length))
            if type_num == 2:
                self.shape_list.append(Circle(color, length))
            if type_num == 3:
                self.shape_list.append(Rectangle(color, length, width))

    def sum_areas(self):
        """
        a function that calculates the sum areas
        :return:the sum of the areas
        """
        sum1 = 0
        for i in self.shape_list:
            sum1 += i.get_area()
        return sum1

    def sum_perimeters(self):
        """
        a function that calculates the sum perimeters
        :return:the sum of the perimeters
        """
        sum2 = 0
        for i in self.shape_list:
            sum2 += i.get_perimeter()
        return sum2

    def count_colors(self):
        """
        counts the number of shapes in each color
        :return: a dict with the color and the number of shapes in each color
        """
        for i in self.shape_list:
            if i.get_color() in self.color_counter:
                self.color_counter[i.get_color()] += 1
            else:
                self.color_counter[i.get_color()] = 1
        return self.color_counter
