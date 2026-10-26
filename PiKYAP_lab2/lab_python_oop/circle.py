import math

from . import geometric_figure, figure_color

class Circle(geometric_figure.GeometricFigure):
    ClassName = 'Circle'

    def __init__(self, radius, color):
        self.radius = radius
        self.color = figure_color.FigureColor(color)

    def __repr__(self):
        return f'Circle(radius={self.radius}, color={self.color.color}, area={self.get_area()})'

    def get_area(self):
        return math.pi * self.radius ** 2
