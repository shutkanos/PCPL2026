from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    ClassName = 'Geometric Figure'

    @abstractmethod
    def get_area(self):
        pass

    def get_class_name(self):
        return self.ClassName