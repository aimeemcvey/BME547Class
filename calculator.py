# calculator.py
u = int(input('Insert first number: '))
v = int(input('Insert second number: '))
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
else:
    print('{} not recognized' .format(x))
print("Finished")