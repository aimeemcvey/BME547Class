def add_two_numbers(a,b):
    sum = a + b
    print(sum)
    if type(a) == 'str' or type(b) == 'str':
        raise TypeError("Change variables to ints")
    if a < 0 or b < 0:
        raise ValueError("Change variables to pos")

def main():
    x = input("a: ")
    y = input("b: ")
    x = int(x)
    y = int(y)
    add_two_numbers(x,y)


if __name__ == '__main__':
    main()