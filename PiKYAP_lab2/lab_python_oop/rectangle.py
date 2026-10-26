from . import geometric_figure, figure_color

class Rectangle(geometric_figure.GeometricFigure):
    ClassName = 'Rectangle'

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = figure_color.FigureColor(color)
        self.__secret = 0


    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height}, color={self.color.color}, area={self.get_area()})'

    def get_area(self):
        return self.width * self.height
