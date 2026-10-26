from . import rectangle

class Square(rectangle.Rectangle):
    ClassName = 'Square'

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return f'Square(side={self.width}, color={self.color.color}, area={self.get_area()})'
