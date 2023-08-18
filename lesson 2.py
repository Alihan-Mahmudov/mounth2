class Figure:
    unit = "cm"

    def __init__(self):
        self.__perimeter = 0

    def get_perimeter(self):
        return self.__perimeter

    def set_perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        self.calculate_perimeter()

    def calculate_area(self):
        return self.__side_length ** 2

    def calculate_perimeter(self):
        self.__perimeter = 4 * self.__side_length
        return self.__perimeter

    def info(self):
        return f"Square side length: {self.__side_length}{self.unit}, " \
               f"perimeter: {self.__perimeter}{self.unit}, area: " \
               f"{self.calculate_area()}{self.unit}."

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.calculate_perimeter()

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        self.__perimeter = 2 * (self.__length + self.__width)
        return self.__perimeter

    def info(self):
        return f"Rectangle length: {self.__length}{self.unit}," \
               f" width: {self.__width}{self.unit}, " \
               f"perimeter: {self.__perimeter}{self.unit}, " \
               f"area: {self.calculate_area()}{self.unit}."


shapes = [
    Square(5),
    Square(7),
    Rectangle(5, 8),
    Rectangle(3, 10)
]


for shape in shapes:
    print(shape.info())
