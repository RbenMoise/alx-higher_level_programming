#!/usr/bin/python3

"""the thisng"""

class Square:
    def __init__(self, size=0):
        """
        Initialize a new Square instance with an optional size.

        Args:
            size (int, optional): The size (side length) of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2
