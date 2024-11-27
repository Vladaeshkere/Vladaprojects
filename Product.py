class Products:
    def __init__(self):
        self.__name = input('Write the name of the product')
        __ErrorTypeNumber = True
        if __ErrorTypeNumber:
            while __ErrorTypeNumber:
                try:
                    self.__number = int(input('Write the number of the product'))
                    __ErrorTypeNumber = False
                except ValueError:
                    print('Please write a number')

        __ErrorTypePrice = True
        if __ErrorTypePrice:
            while __ErrorTypePrice:
                try:
                    self.__price = int(input('Write the price of the product'))
                    __ErrorTypePrice = False
                except ValueError:
                    print('Please write a normal price')

    def __cost(self):
        return self.__number * self.__price

    def get_cost(self):
        print(f'The cost of the {self.__name} is {self.__cost()}')


product = Products()
product.get_cost()