# calculator.py
import math
#u = 47
#v = 7
def add(x, y):
    z = x + y
    symbol = '+'
    return z, symbol


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z

def square_root(x):
    z = math.sqrt(x)
    return z


if __name__ == "__main__":
    u = float(input('Insert first number: '))
    v = float(input('Insert second number: '))
    x = input('Enter a letter: ')
    print('You entered {}' .format(x))
    if x == 'a':
        d, f = add(u, v)
        print('{} {} {} = {}' .format(u, f, v, d))
        if d > 100:
            print('This number is too high.')
    elif x == 's':
        d = subtract(u, v)
        print('{} - {} = {}' .format(u, v, d))
    elif x == 'm':
        d = multiply(u, v)
        print('{} * {} = {}' .format(u, v, d))
    elif x == 'd':
        d = divide(u, v)
        print('{} / {} = {}' .format(u, v, d))
    elif x == 'r':
        d = square_root(u)
        print('sqrt({}) = {}' .format(u, d))
    else:
        print('{} not recognized' .format(x))
    print("Finished")