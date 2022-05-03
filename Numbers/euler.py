"""Find e to the Nth Digit - Just like the previous problem, but with e instead of PI. Enter a number and have the
program generate e up to that many decimal places. Keep a limit to how far the program will go. """
import sys
from decimal import *

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)


def factorial(n):
    if not n:
        return 1
    return n * factorial(n - 1)


def euler(n):
    k = 1000
    s = 0
    getcontext().prec = n + 1
    for k in range(k):
        s += Decimal(1) / Decimal(factorial(k))
    print(f"Euler's number: {Decimal(s)}")


def main():
    while True:
        entry = input('->> ')
        if entry == 'q':
            break
        if not entry.isdigit():
            print('Not a digit, try again')
            continue
        euler(int(entry))


if __name__ == '__main__':
    main()


