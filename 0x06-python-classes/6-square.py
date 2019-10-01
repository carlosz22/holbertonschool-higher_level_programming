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
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """A

        """
        return self.__size

    @size.setter
    def size(self, size):
        """A

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def position(self):
        """A
        """
        return self.__position

    @position.setter
    def position(self, position):
        """A
        """
        if type(self.__position) is not tuple and len(self.__position) != 2 and
        self.__position[0] >= 0 and self.__position[1] >= 0:
            raise TypeError('position must be a tuple of 2 positive integers')

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
            print()

        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
