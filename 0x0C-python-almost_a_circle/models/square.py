#!/usr/bin/python3
'''Module class of square'''
from models.rectangle import Rectangle

class Square(Rectangle):
    ''' a square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ This is the new __str__ function """
        sq_str = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return f"{sq_str}"
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)

    def update(self, *args, **kwargs):
        """ This is the update function """
        attr = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key in list(kwargs.keys()):
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ This is the to_dictionary function """
        return vars(self)
