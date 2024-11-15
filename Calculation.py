class CalculationRectangle:

    def __init__(self):
        self.__a = None
        __ErrorTypeA = True
        if __ErrorTypeA:
            while __ErrorTypeA:
                try:
                    self.__a = int(input('Write the first side of the rectangle'))
                    __ErrorTypeA = False
                except ValueError:
                    print('Please write a number')
        self.__b = None
        __ErrorTypeB = True
        if __ErrorTypeB:
            while __ErrorTypeB:
                try:
                    self.__b = int(input('Write the second side of the rectangle'))
                    __ErrorTypeB = False
                except ValueError:
                    print('Please write a number')

    def __perimeter(self):
        self.__sum = self.__b + self.__a
        return self.__sum * 2

    def get_perimeter(self):
        print(f'P = {self.__perimeter()}')

    def __area(self):
        return self.__a * self.__b

    def get_area(self):
        print(f'S = {self.__area()}')


rectangle = CalculationRectangle()
rectangle.get_perimeter()
rectangle.get_area()

rectangle2 = CalculationRectangle()
rectangle2.get_perimeter()
rectangle2.get_area()
