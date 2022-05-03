"""Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a
limit to how far the program will go. """
import math
import sys
from decimal import *

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)


def factorial(x):
    if not x:
        return 1
    return x * factorial(x - 1)


def get_value_of_pi(k):
    k = k + 1
    getcontext().prec = k
    s = 0

    for k in range(k):
        nom = factorial(6 * k) * (13591409 + 545140134 * k)
        denom = factorial(3 * k) * (factorial(k)) ** 3 * (640320 ** (3 * k))
        s += nom / denom

    nom2 = 426880 * math.sqrt(10005)
    pi = Decimal(nom2) / Decimal(s)

    return pi


def main():
    while True:
        entry = input("->> ")
        if entry == "q":
            break
        if not entry.isdigit():
            print("Not a digit, try again")
            continue
        print(get_value_of_pi(int(entry)))


if __name__ == '__main__':
    main()
