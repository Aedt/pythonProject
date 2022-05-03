"""Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.

"""
import math


def prime_factors(x):
    while x % 2 == 0:
        print(2, end=', ')
        x = x / 2

    for i in range(3, int(math.sqrt(x)) + 1, 2):

        while x % i == 0:
            print(int(i), end=', ')
            x = x / i

    if x > 2:
        print(int(x))


def main():
    while True:
        entry = input('->> ')
        if entry == 'q':
            break
        if not entry.isdigit():
            print('Not a digit, try again, \'q\' to quit')
            continue
        prime_factors(int(entry))


if __name__ == '__main__':
    main()
