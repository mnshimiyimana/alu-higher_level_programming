#!/usr/bin/python3

"""class that inherits from another"""


from models.base import Base

class Rectangle(Base):
        '''class Rectangle that inherits from Base'''


        def __init__(self, width, height, x=0, y=0, id=None):
                '''initializes the rectangle'''
                self.width = width
                self.height = height
                self.x = x
                self.y = y
                super().__init__(id)

        @property
        def width(self):
                '''getter for width'''
                return self.__width

        @width.setter
        def width(self, value):
                '''setter for width'''
                if type(value) is not int:
                        raise TypeError('width must be an integer')
                if value <= 0:
                        raise ValueError('width must be > 0')
                self.__width = value

        @property
        def height(self):
                '''getter for height'''
                return self.__height

        @height.setter
        def height(self, value):
                '''setter for height'''
                if type(value) is not int:
                        raise TypeError('height must be an integer')
                if value <= 0:
                        raise ValueError('height must be > 0')
                self.__height = value

        @property
        def x(self):

                '''getter for x'''
                return self.__x

        @x.setter
        def x(self, value):
                '''setter for x'''
                if type(value) is not int:
                        raise TypeError('x must be an integer')
                if value < 0:
                        raise ValueError('x must be >= 0')
                self.__x = value

        @property
        def y(self):
                '''getter for y'''
                return self.__y

        @y.setter
        def y(self, value):
                '''setter for y'''
                if type(value) is not int:
                        raise TypeError('y must be an integer')
                if value < 0:
                        raise ValueError('y must be >= 0')
                self.__y = value

        def area(self):
                '''returns the area of the rectangle'''
                return self.__width * self.__height

        def display(self):
                '''prints the rectangle'''
                for i in range(self.__y):
                        print()
                for i in range(self.__height):
                        for j in range(self.__x):
                                print(' ', end='')
                        for j in range(self.__width):
                                print('#', end='')
                        print()

        def __str__(self):
                '''returns the string representation of the rectangle'''
                return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                        self.id, self.__x, self.__y, self.__width, self.__height)

        def update(self, *args, **kwargs):
                '''assigns an argument to each attribute'''
                if args:
                        for i, arg in enumerate(args):
                                if i == 0:
                                        self.id = arg
                                elif i == 1:
                                        self.width = arg
                                elif i == 2:
                                        self.height = arg
                                elif i == 3:
                                        self.x = arg
                                elif i == 4:
                                        self.y = arg
                else:
                        for key, value in kwargs.items():
                                if key == 'id':
                                        self.id = value
                                elif key == 'width':
                                        self.width = value
                                elif key == 'height':
                                        self.height = value
                                elif key == 'x':
                                        self.x = value
                                elif key == 'y':
                                        self.y = value

        def to_dictionary(self):
                '''returns the dictionary representation of a Rectangle'''
                return {'id': self.id, 'width': self.width, 'height': self.height,
                        'x': self.x, 'y': self.y}

