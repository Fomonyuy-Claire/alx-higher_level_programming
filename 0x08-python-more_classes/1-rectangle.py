#!/usr/bin/python3
"""Defining a rectangle"""

class Rectangle:

    def _init_(self,width=0,height=0):

        self.height = height
        self.width = width

        @property
        def height(self):
            """get height of rectangle"""
            return self._height

        @height.setter
    def height(self, value):
        """
            Checking for TypeError and ValueError
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
            Checking for TypeError and ValueError
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
