from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color, width):
        """
        initializer
        :param color, width:
        """
        super().__init__(color, width, width)

    def get_area(self):
        """
        A function that gets the area of the square
        :return: the area of the square
        """
        return self.width * self.width

    def get_perimeter(self):
        """
        A function that gets the perimeter of the square
        :return: the perimeter of the square
        """
        return 4 * self.width

    def get_width(self):
        """
        A function that gets the width of the square
        :return: the width of the square
        """
        return self.width

    def set_width(self, width):
        """
        A function that sets the width of the square
        :return:
        """
        self.width = width
