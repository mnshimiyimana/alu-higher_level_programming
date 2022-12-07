#!/usr/bin/python3

"""Dictionary representation of the class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class"""
        if len(args) !=0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

            elif len(kwargs) != 0:
            if 'id' in kwargs:
                    self.id = kwargs['id']
            else:
                        self.id = self.id
            if 'size' in kwargs:
                    self.size = kwargs['size']
            else:
                        self.size = self.size
            if 'x' in kwargs:
                    self.x = kwargs['x']
            else:
                        self.x = self.x
            if 'y' in kwargs:

                    self.y = kwargs['y']
            else:
                        self.y = self.y

    def to_dictionary(self):
        """Dictionary representation of the class"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
