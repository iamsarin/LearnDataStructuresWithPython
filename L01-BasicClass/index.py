import math


class Shape(object):
    def __init__(self, color: str = 'red', filled: bool = True):
        self.__color = color
        self.__filled = filled

    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str):
        self.__color = color

    def is_filled(self) -> bool:
        return self.__filled

    def get_area(self) -> float:
        raise NotImplementedError('subclasses must override foo()!')

    def get_perimeter(self) -> float:
        raise NotImplementedError('subclasses must override foo()!')

    def to_string(self) -> str:
        raise NotImplementedError('subclasses must override foo()!')

    def get_xx(self):
        return self.__color


class Circle(Shape):
    def __init__(self, radius: float, color: str = None, filled: bool = None):
        super().__init__(color, filled)
        self.__radius = radius

    def get_radius(self) -> float:
        print(self.get_xx())
        return self.__radius

    def set_radius(self, radius: float):
        self.__radius = radius

    def get_area(self) -> float:
        return math.pi * (self.__radius * self.__radius)

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def to_string(self) -> str:
        return 'Circle \n\tradius: ' + str(self.__radius)


class Rectangle(Shape):
    def __init__(self, width: float = 1.0, length: float = 1.0, color: str = None, filled: bool = None):
        super().__init__(color, filled)
        self.__width = width
        self.__length = length

    def get_width(self) -> float:
        return self.__width

    def set_width(self, width: float):
        self.__width = width

    def get_length(self) -> float:
        return self.__length

    def set_length(self, length: float):
        self.__length = length

    def get_area(self) -> float:
        return self.__width * self.__length

    def get_perimeter(self) -> float:
        return (self.__width + self.__length) * 2

    def to_string(self) -> str:
        return 'Rectangle \n\twidth: ' + str(self.__width) + '\n\tlength:' + str(self.__length)

    def _get_x(self):
        return 'x'


class Square(Rectangle):
    def __init__(self, side: float = 1.0, color: str = None, filled: bool = None):
        super().__init__(side, side, color, filled)
        print(self._get_x())

    def get_side(self) -> float:
        return self.__width

    def set_side(self, side: float):
        self.__width = side
        self.__length = side

    def set_width(self, side: float):
        self.__width = side
        self.__length = side

    def set_length(self, side: float):
        self.__width = side
        self.__length = side

    def to_string(self) -> str:
        return 'Square \n\tSide: ' + str(self.__width)


print('Create circle has radius 3 Unit')
circle = Circle(3)
print(circle.get_radius())
print('Area: ', "{0:.2f}".format(circle.get_area()))
print('Perimeter: ', "{0:.2f}".format(circle.get_perimeter()))
print('\n')

print('Create circle has radius 5 Unit that green and filled')
circle = Circle(3, 'green', True)
print('Area: ', "{0:.2f}".format(circle.get_area()))
print('Perimeter: ', "{0:.2f}".format(circle.get_perimeter()))
print('Color: ', circle.get_color())
print('isFilled: ', 'Yes' if circle.is_filled() else 'No')
print('\n')

print('Create rectangle width=3 length=8')
rectangle = Rectangle(3, 8)
print('Area: ', "{0:.2f}".format(rectangle.get_area()))
print('Perimeter: ', "{0:.2f}".format(rectangle.get_perimeter()))
print('\n')

print('Create square 3 Unit')
square = Square(3)
print('Area: ', "{0:.2f}".format(square.get_area()))
print('Perimeter: ', "{0:.2f}".format(square.get_perimeter()))
print('\n')
print(square._get_x())
print(square._t)
