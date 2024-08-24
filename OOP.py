class Octopus:
    count_animals = 0

    def __init__(self, age, name='Octavio'):
        self._name = name
        self._age = age
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        my_str = f'X: {self._x}, Y:{self._y}, Color: ({self._red}, {self._green}, {self._blue})'
        if self._red == 0 and self._green == 0 and self._blue > 50:
            my_str += ' Blue'
        elif self._blue == 0 and self._green == 0 and self._red > 50:
            my_str += ' Red'
        elif self._blue == 0 and self._red == 0 and self._green > 50:
            my_str += ' Green'

        print(my_str)


class BigThing:
    def __init__(self, something):
        self._something = something

    def size(self):
        if isinstance(self._something, int):
            return self._something
        elif isinstance(self._something, list) or isinstance(self._something, dict) or isinstance(self._something, str):
            return len(self._something)
        else:
            return 'Not valid'


class BigCat(BigThing):
    def __init__(self, something, weight):
        super().__init__(something)
        self._weight = weight

    def size(self):
        if self._weight > 15:
            return 'Fat'
        elif self._weight > 20:
            return 'Very Fat'
        else:
            return 'OK'


class Animal:
    zoo_name = 'Hayaton'

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger != 0

    def feed(self):
        if self._hunger > 0:
            self._hunger -= 1

    def __str__(self):
        my_type = ''
        if isinstance(self, Dog):
            my_type = 'Dog '
        elif isinstance(self, Cat):
            my_type = 'Cat '
        elif isinstance(self, Skunk):
            my_type = 'Skunk '
        elif isinstance(self, Unicorn):
            my_type = 'Unicorn '
        else:
            my_type = 'Dragon '

        return my_type + self.get_name()


class Dog(Animal):
    def talk(self):
        print('woof woof')

    def fetch_stick(self):
        print('There you go, sir!')


class Cat(Animal):
    def talk(self):
        print('meow')

    def chase_laser(self):
        print('Meeeeow')


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print('tsssss')

    def stink(self):
        print('Dear lord!')


class Unicorn(Animal):
    def talk(self):
        print('Good day, darling')

    def sing(self):
        print("i'm not your toy")


class Dragon(Animal):
    def __init__(self, name, hunger=0, color='Green'):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print('Raaaawr')

    def breath_fire(self):
        print('$@#$#@$')
