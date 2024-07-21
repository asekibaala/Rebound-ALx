#!/usr/bin/python3

class Rectangle:
    """ Class that defines a rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
       
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
    
        return self.__width

    @width.setter
    def width(self, value):
       

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
       

        return self.__height

    @height.setter
    def height(self, value):
       

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
    
        return self.width * self.height

    def perimeter(self):
        

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Method that returns the Rectangle #

        Returns:
            str of the rectangle

        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the string represantion of the instance

        Returns:
            string represenation of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance is deleted


        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
