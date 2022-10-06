class Shape:
    def __init__(self, color):
        """
        initializer
        :param color:
        """
        self.color = color

    def set_color(self, color):
        """
        A function that sets the color of the shape
        :param color:
        :return:
        """
        print("setter method called")
        self.color = color

    def get_color(self):
        """
        A function that gets the color of the shape
        :return: the color of the shape
        """
        return self.color

    def get_area(self):
        """
        A function that gets the area of the shape
        :return:
        """
        pass

    def get_perimeter(self):
        """
        A function that gets the perimeter of the shape
        :return:
        """
        pass
