# This is a sample Python script.
import base64
from functools import reduce
import threading
import string
from OOP import Octopus
from OOP import Pixel
from OOP import BigThing
from OOP import BigCat
import time
# import xyz
import functools
import winsound
from itertools import combinations

def combine_coins(coin, values):
    print(','.join([(lambda coin, num: coin + str(num))(coin, num) for num in values]))


def word_length():
    my_file = open("names.txt", "r").readlines()
    print(max(my_file))


def sum_of_length():
    my_file = open("names.txt", "r").readlines()
    print(sum([len(line) - 1 for line in my_file]) + 1)


def min_names():
    my_file = open("names.txt", "r").readlines()
    my_file.sort(key=len)
    print([line[0:len(line) - 1] for line in my_file if len(line) == len(my_file[0])])


def print_names_with_x_len():
    my_file = open("names.txt", "r").readlines()
    choosen_len = int(input('Please enter the length of the words you would like to see: '))
    print([line[0:len(line) - 1] for line in my_file if len(line) - 1 == choosen_len])


def write_lengths():
    my_file = open('names.txt', 'r').readlines()
    outfile = open('out.txt', 'w')

    # option number 1 : using map
    # outfile.writelines(map(lambda s: f"{len(s)-1}\n", my_file))

    # option number 2 : using list comprehension and lambda function
    outfile.writelines([f"{len(string) - 1}\n" for string in my_file])


def secret(a):
    return a % 3 != 0 and a % 5 != 0


def double_char(ch):
    return ch + ch


def double_string(my_str):
    return ''.join(map(double_char, my_str))


def div_by_four(num):
    return num % 4 == 0


def four_dividers(number):
    return list(filter(div_by_four, range(1, number)))


def my_sum(num1, num2):
    return num1 + num2


def sum_of_digits(number):
    return reduce(my_sum, list(map(int, str(number))))


def function(num, item):
    return num + 1


def intersection(list_1, list_2):
    return [x for x in list_1 for y in list_2 if x == y]


def is_prime(number):
    return bool(min([1 if number % num != 0 else 0 for num in range(2, number)]))


def orig_is_funny(string):
    for char in string:
        if char != 'h' and char != 'a':
            return False
    return True


def is_funny(string):
    return bool(min([1 if ch == 'a' or ch == 'h' else 0 for ch in string]))


def password(string):
    return ''.join([' ' if ch == ' ' else ':' if ch == ':' else chr(ord(ch) + 2) for ch in string])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # map, filter and reduce

    # result = filter(secret, list(range(1, 31)))
    # print(list(result))

    # print(double_string('Hello Udi'))
    # print(four_dividers(50))
    # print(sum_of_digits(104))

    # lambda functions

    '''
    password = input("Enter Your password (integers only): ")
    lst = list(map(int, password))
    magic = functools.reduce(function, lst)
    result = (lambda x: x % 4 == 0)(magic)
    if result:
        print("Correct password!")
    else:
        print("Wrong password.")
    '''

    # list comprehension

    # print(intersection(set([1, 2, 3, 4, 4]), set([3, 4, 5, 6])))
    # print(is_prime(100))
    # print(is_funny("hahahaha"))
    # print(password('sljkai ugrf rfc akbc: lglc dksp klc ruk'))

    # summery

    # combine_coins('$', [1,2,3,4])
    # word_length()
    # sum_of_length()
    # min_names()
    # write_lengths()
    # print_names_with_x_len()

    # OOP

    '''
    oct1 = Octopus(4, 'Shmulikipod')
    oct2 = Octopus(7)
    oct1.birthday()
    print(f'Oct1 name is: {oct1.get_name()}')
    print(f'Oct2 name is: {oct2.get_name()}')
    print(f'The number of octopuses is: {Octopus.count_animals} ')
    '''

    '''
    p1 = Pixel(5, 6, 250)
    p1.print_pixel_info()
    p1.set_grayscale()
    p1.print_pixel_info()
    '''

    '''
    b = BigThing('aaa')
    print(b.size())

    c = BigCat("Mitzi", 17)
    print(c.size())
    '''

    '''
    zoo_lst = [OOP.Dog("Brownie", 10), OOP.Cat("Zelda", 3), OOP.Skunk("Stinky", 0), OOP.Unicorn("Keith", 7),
               OOP.Dragon("Brownie", 1450)]


    zoo_lst.append(OOP.Dog('Doggo', 80))
    zoo_lst.append(OOP.Cat('Kitty', 80))
    zoo_lst.append(OOP.Skunk('Stinky Jr.', 80))
    zoo_lst.append(OOP.Unicorn('Clair', 80))
    zoo_lst.append(OOP.Dragon('McFly', 80))

    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal)
        while animal.is_hungry():
            animal.feed()

    print('all animal supposed to be full by now')

    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal)

    for animal in zoo_lst:
        animal.talk()
        if isinstance(animal, OOP.Dog):
            animal.fetch_stick()
        elif isinstance(animal, OOP.Cat):
            animal.chase_laser()
        elif isinstance(animal, OOP.Skunk):
            animal.stink()
        elif isinstance(animal, OOP.Unicorn):
            animal.sing()
        else:
            animal.breath_fire()

    print(f'Zoo name: {animal.zoo_name}')
    '''

    # StopIteration
    # mylist = iter(["apple"])
    # x = next(mylist)
    # print(x)
    # x = next(mylist)

    # ZeroDivisionError: division by zero
    # y = 5 / 0

    # AssertionError: Invalid Operation
    # x = 1
    # y = 0
    # assert y != 0, "Invalid Operation"  # denominator can't be 0
    # print(x / y)

    # ModuleNotFoundError: No module named 'xyz'
    # see above import (import xyz)

    # KeyError: 'Michael'
    # ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
    # ages['Michael']

    # SyntaxError: invalid syntax. Perhaps you forgot a comma?
    # ages = {
    #    'pam': 24,
    #    'jim': 24
    #    'michael': 43
    # }

    # IndentationError: expected an indented block after 'for' statement on line 242
    # for i in range(10):
    # print(i)

    # TypeError: can only concatenate str (not "int") to str
    # geek = "Geeks"
    # num = 4
    # print(geek + num + geek)

'''
def read_file(file_name):
    f = None
    try:
        f = open(file_name)
    except UnboundLocalError:
        print('__CONTENT_START__')
        print('__NO_SUCH_FILE__')
        print('__CONTENT_END__')
    else:
        print('__CONTENT_START__')
        print(f.readline())
        print('__CONTENT_END__')
    finally:
        f.close()

read_file('names.txt')
'''

'''
class UnderAge(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return "Sorry, you can't participate my party since you are ony %d years old." % self._age

    def get_arg(self):
        return self._age


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


send_invitation('Udi', 20)
send_invitation('Gal', 17)
'''

# Custom Exceptions
'''
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Username is missing one or more required character: %s" % self._arg

    def get_arg(self):
        return self._arg


class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Username Too Short: length = %d" % self._arg

    def get_arg(self):
        return self._arg


class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Username Too Long: length = %d" % self._arg

    def get_arg(self):
        return self._arg


class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password is missing one or more required character: %s" % self._arg

    def get_arg(self):
        return self._arg


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password Too Short: length = %d" % self._arg

    def get_arg(self):
        return self._arg


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password Too Long: length = %d" % self._arg

    def get_arg(self):
        return self._arg


def check_username(username):
    letter = digit = underscore = True
    try:
        letter = any([char.isalpha() for char in username])
        digit = any([char.isdigit() for char in username])
        underscore = any([char == '_' for char in username])
        if len(username) < 3:
            raise UsernameTooShort(len(username))
        if len(username) > 16:
            raise UsernameTooLong(len(username))
        if not letter or not digit or not underscore:
            raise UsernameContainsIllegalCharacter(username)

    except UsernameContainsIllegalCharacter as e:
        print(e)
    except UsernameTooShort as e:
        print(e)
    except UsernameTooLong as e:
        print(e)

    return letter and digit and underscore and 2 < len(username) < 17


def check_password(password):
    upper = lower = digit = punctuation = True
    try:
        upper = any([char.isupper() for char in password])
        lower = any([char.islower() for char in password])
        digit = any([char.isdigit() for char in password])
        punctuation = any([char in string.punctuation for char in password])
        if len(password) < 8:
            raise PasswordTooShort(len(password))
        if len(password) > 40:
            raise PasswordTooLong(len(password))
        if not upper or not lower or not digit or not punctuation:
            raise PasswordMissingCharacter(password)
    except PasswordMissingCharacter as e:
        print(e)
    except PasswordTooShort as e:
        print(e)
    except PasswordTooLong as e:
        print(e)
    return upper and lower and digit and punctuation and 7 < len(password) < 41


def check_input(username, password):
    userOK = check_username(username)
    passwordOK = check_password(password)
    if userOK and passwordOK:
        print('OK')
    else:
        print('Failed')


check_input("1", "2")
check_input("0123456789ABCDEFG", "2")
check_input("Aa1.", "12345678")
check_input("A_1", "2")
check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
check_input("A_1", "abcdefghijklmnop")
check_input("A_1", "ABCDEFGHIJLKMNOP")
check_input("A_1", "ABCDEFGhijklmnop")
check_input("A_1", "4BCD3F6h1jk1mn0p")
check_input("A_1", "4BCD3F6.1jk1mn0p")
'''
# Generators
'''
def is_primee(number):
    return bool(min([1 if number % num != 0 else 0 for num in range(2, number)]))

prime_generator = (n for n in range(3,1000) if is_primee(n))
for prime_number in prime_generator:
    print(prime_number)
'''

'''
def translate(sentence):
    ret_str = ''
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}

    g = (words[word] for word in sentence.split())
    for word in g:
        ret_str += word
        ret_str += ' '
    return  ret_str


print(translate("el gato esta en la casa"))
'''

'''
def is_primee(number):
    return bool(min([1 if number % num != 0 else 0 for num in range(2, number)]))


def first_prime_over(num):
    prime_generator = (n for n in range(num, num + 1000) if is_primee(n))
    return next(prime_generator)


print(first_prime_over(1000000))
'''

'''
def parse_ranges(ranges_string):
    my_list = ranges_string.split(',')
    gen = (sub_str.split('-') for sub_str in my_list)
    for start, stop in gen:
        for num in range(int(start), int(stop) + 1):
            yield num


#parse_ranges("1-2,4-4,8-10")
print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))
'''

'''
def get_fibo():
    prev = 0
    cur = 1
    yield prev
    yield cur
    while True:
        next = prev +cur
        prev = cur
        cur = next
        yield  next


fibo_gen = get_fibo()

for num in range(10):
    print(next(fibo_gen))
'''

'''
def gen_secs():
    sec = 0
    while True:
        sec += 1
        if sec == 60:
            sec = 0
        yield sec


def gen_minutes():
    min = 0
    while True:
        min += 1
        if min == 60:
            min = 0
        yield min


def gen_hours():
    hour = 0
    while True:
        hour += 1
        if hour == 24:
            hour = 0
        yield hour


def gen_time():
    second = 0
    minute = 0
    hour = 0
    secs = gen_secs()
    minutes = gen_minutes()
    hours = gen_hours()
    while True:
        for second in secs:
            if second == 0:
                minute = next(minutes)
                if minute == 0:
                    hour = next(hours)
            #yield f'{hour:02d}:{minute:02d}:{second:02d}'
            yield hour, minute, second


def gen_years(start=2019):
    current_year = start
    while True:
        current_year += 1
        yield current_year


def gen_months():
    month = 0
    while month != 12:
        month += 1
        yield month


def gen_days(month, leap_year=True):
    while True:
        match month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                yield 31
            case 4 | 6 | 9 | 11:
                yield 30
            case 2:
                if leap_year:
                    yield 29
                else:
                    yield 28

def gen_date():
    day = 1
    month = 1
    year = 2024
    time = gen_time()
    months = gen_months()
    years = gen_years()
    days = gen_days(1)

    while True:
        for hour, minute, second in time:
            if hour == 0 and minute == 0 and second == 0:
                day += 1
                if day > next(days(month, leap_year(year))):
                    day = 1
                    prev_month = month
                    month = next(months)
                    if month != prev_month and month == 1:
                        year = next(years)
        yield f'{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}'




def leap_year(year):
    # Python program to check if year is a leap year or not

    # To get year (integer input) from the user
    # year = int(input("Enter a year: "))

    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return False



gen = gen_date()
count = 0
for date in gen:
    if count % 100000 == True:
        print(date)
'''

# iterators

'''
freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

list_of_notes = notes.split('-')
final_list_of_notes = [ note.split(',') for note in list_of_notes]

# _ = (winsound.Beep(freqs[val[0]], int(val[1])) for val in final_list_of_notes)

for val in final_list_of_notes:
    winsound.Beep(freqs[val[0]], int(val[1]))

'''

'''
numbers = iter(list(range(1, 101)))
for i in numbers:
    try:
        next(numbers)
        next(numbers)
        print(i)
    except StopIteration:
        break

'''
'''
def standard_tuple_of_combinataion(combination):
    return tuple(sorted(list(combination)))

def combinations_to_target_of_length_n(arr, target, n):
    #take all combinations of length n, if their sum is equal to target, they are relevant
    #take all relevant combinations, and create a standart format for them as a tuple, by putting the tuples in a set, the repeated answers get ignored
    ret = set((standard_tuple_of_combinataion(combination) for combination in combinations(arr, n) if sum(combination) == target))
    return list(ret)

def combinations_to_target(arr, target):
    #go over all possible lengths of the answer, then add all of those combinations together
    #note we do not need to check for repetitions between runs of combinations_to_target_of_length_n, as they have different lengths
    ret = []
    for i in range(len(arr) + 1):
        ret += combinations_to_target_of_length_n(arr, target, i)
    return ret

print(combinations_to_target([20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1,1,1,1],100))
'''

# Iterators

'''
class MusicNotes():
    def __init__(self):
        self.freqs = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.octav_index=0
        self.index=0

    def __str__(self):
        return self.freqs[self.index] * pow(2,self.octav_index)

    def __iter__(self):
        return self

    def __next__(self):
        if self.octav_index == 5 and self.index == 0:
            raise StopIteration()
        retval = self.freqs[self.index] * pow(2,self.octav_index)
        self.index += 1
        if self.index == len(self.freqs):
            self.index = 0
            self.octav_index += 1
        return retval


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)

'''



#print(check_id_valid(123456780))
#print(check_id_valid(123456782))

class IDIterator:
    def __init__(self, valid_id):
        self.id = valid_id

    def __str__(self):
        return self.id

    def __iter__(self):
        return self

    def __next__(self):
        if self.id == 999999999:
            raise StopIteration()
        while not self.check_id_valid():
            pass
        return self.id-1

    def check_id_valid(self):
        id_list = [int(x) for x in str(self.id)]
        list2 = [(digit * 2 if i % 2 else digit) for i, digit in enumerate(id_list)]
        list3 = [sum(divmod(val, 10)) if val > 9 else val for val in list2]
        self.id += 1
        return sum(list3) % 10 == 0

        '''
        list3 = []
        for val in list2:
            if val > 9:
                x, y = [int(x) for x in str(val)] # I know that val contains 2 digits
                list3.append(x+y)
            else:
                list3.append(val)
        '''

'''
def gen_id_valid(valid_id):
    while True:
        valid_id += 1
        id_list = [int(x) for x in str(valid_id)]
        list2 = [(digit * 2 if i % 2 else digit) for i, digit in enumerate(id_list)]
        list3 = [sum(divmod(val, 10)) if val > 9 else val for val in list2]
        if sum(list3) % 10 == 0:
            yield valid_id


gen = gen_id_valid(123456780)
print(next(gen))
print(next(gen))
print(next(gen))
'''


#num = int(input('Please inset a valid id: '))
#valid_Id = IDIterator(num)
#for num in range(10):
#    print(next(valid_Id))


text = "CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo="

decoded_str = base64.b64decode(text).decode('utf-8')

print(decoded_str)