# calculator.py
def add(x, y):
    z = x + y
    print('{} + {} = {}' .format(x, y, z))
    return z


def subtract(x, y):
    z = x - y
    print('{} - {} = {}' .format(x, y, z))
    return z


def multiply(x, y):
    z = x * y
    print('{} * {} = {}' .format(x, y, z))
    return z


x = input('Enter a letter: ')
print('You entered {}' .format(x))
if x == 'a':
    d = add(100, 2)
    if d > 100:
        print('This number is too high.')
elif x == 's':
    d = subtract(6, 1)
elif x == 'm':
    d = multiply(7, 9)
else:
    print('{} not recognized' .format(x))
print("Finished")