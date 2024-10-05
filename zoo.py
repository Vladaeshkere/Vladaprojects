import random
class Animal:
    _food_level = 0
    _name = ''
    _type = ''

    def _make_sound(self):
        self.__sound()
    def __sound(self):
        if self._type == 'пташка':
            print('цвіріньк')
        elif self._name == 'Кішка':
            print('мяу')
        elif self._name == 'Собака':
            print('гав')


    def _feed(self):
        self.__food()
    def __food(self):
        self._food_level += 10
        if self._type == 'пташка':
            print('похавав зернят')
        elif self._name == 'Кішка':
            print('Похавав рибу')
        elif self._name == 'Собака':
            print('похава корм')

        if self._food_level >= 100:
            self._food_level = 100

    def _get_info(self):
        self.__info()

    def __info(self):
        print(f'Мене звати {self._name}, я {self._type}')



class Bird(Animal):
    _type = 'пташка'

    def _do_fly(self):
        self.__fly()
    def __fly(self):
        print('Я політав')
        self._food_level -= 5
        print(f'{self._food_level}')


class Samci(Animal):
    _type = 'савець'

    def _do_pogladit(self):
        self.__pogladit()
    def __pogladit(self):
        print('Мене погладили')
        self._food_level -= 5
        print(f'Рівень ситості {self._food_level}')


class Gorobchik(Bird):
    _food_level = 100
    _name = 'Горобець'


class Sinichka(Bird):
    _food_level = 100
    _name = 'Синиця'
    def _where_is_sinicka(self):
        place = random.randint(1,2)
        if place == 1:
            print('Я в дуплі')
        else:
            print('Я на ззовні')


class Cat(Samci):
    _food_level = 100
    _name = 'Кішка'

    def _do_hunt(self):
        self.__hunt()
    def __hunt(self):
        print('Кішка полює')
        self._feed()
        print('Рівень ситості', self._food_level)

class Dog(Samci):
    _food_level = 100
    _name = 'Собака'

    def _do_play(self):
        self.__play()
    def __play(self):
        comand_choice = random.choice(['Бігти за палицею', 'Сісти', 'Лягти', 'Дати лапу', 'Голос'])
        if comand_choice == 'Голос':
            self._make_sound()
        else:
            print(comand_choice)
        self._food_level -= 5
        print(f'Рівень ситості {self._food_level}')

cat = Cat()
cat._do_hunt()
dog = Dog()
dog._do_play()