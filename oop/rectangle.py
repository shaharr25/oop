from shape import Shape


class Rectangle(Shape):
    def __init__(self, color, width, length):
        """
        initializer
        :param color, width, length
        """
        super().__init__(color)
        self.width = width
        self.length = length

    def get_area(self):
        """
        A function that gets the area of the rectangle
        :return: the area of the rectangle
        """
        return self.width*self.length

    def get_perimeter(self):
        """
        A function that gets the perimeter of the rectangle
        :return: the perimeter of the rectangle
        """
        return 2*self.width+2*self.length

    def get_width(self):
        """
        A function that gets the width of the rectangle
        :return: the width of the rectangle
        """
        return self.width

    def get_length(self):
        """
        A function that gets the length of the rectangle
        :return: the length of the rectangle
        """
        return self.length

    def set_width(self, width):
        """
        A function that sets the width of the rectangle
        :return:
        """
        self.width = width

    def set_length(self, length):
        """
        A function that sets the length of the rectangle
        :return:
        """
        self.length = length

    def add(self, rect):
        """
        a function that adds two shapes (rectangle / square)
        :param rect:
        :return:the nea connected shape
        """
        if isinstance(rect, Rectangle):
            if self.width == rect.width or self.width == rect.length:
                r = Rectangle(rect.get_color(), self.width, 2 * self.length)
                return r
            if self.length == rect.width or self.length == rect.length:
                r = Rectangle(rect.get_color(), 2 * self.width, self.length)
                return r
        raise TypeError("not rectangle")
