class CalculationRectangle:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __perimeter(self):
        self.__sum = self.__b + self.__a
        return self.__sum * 2

    def get_perimeter(self):
        print(f'P = {self.__perimeter()}')

    def __area(self):
        return self.__a * self.__b

    def get_area(self):
        print(f'S = {self.__area()}')


a = None
ErrorTypeA = True
if ErrorTypeA:
    while ErrorTypeA:
        try:
            a = int(input('Write the first side of the rectangle'))
            ErrorTypeA = False
        except ValueError:
            print('Please write a number')

b = None
ErrorTypeB = True
if ErrorTypeB:
    while ErrorTypeB:
        try:
            b = int(input('Write the second side of the rectangle'))
            ErrorTypeB = False
        except ValueError:
            print('Please write a number')


rectangle = CalculationRectangle(a, b)
rectangle.get_perimeter()
rectangle.get_area()