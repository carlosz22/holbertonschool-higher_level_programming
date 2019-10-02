#!/usr/bin/python3
"""A
"""


class Square:
    """Creates a new object of class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructor for the class Square

        Args:
            size (int): Square's size

        Attributes:
            size (int): Square's size

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) is not int or type(position[1]) is not int or\
           position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    @property
    def size(self):
        """A

        """
        return self.__size

    @size.setter
    def size(self, value):
        """A

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """A
        """
        return self.__position

    @position.setter
    def position(self, value):
        """A
        """
        if type(value) is not tuple or len(value) != 2 or\
           type(value[0]) is not int or type(value[1]) is not int or\
           value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """A

        """
        return self.__size ** 2

    def my_print(self):
        """A
        """
        if self.__size == 0:
            print()
            return

        if self.__position[0] > 0 and self.__position[1] > 0:
            print("\n" * self.__position[1])

        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
