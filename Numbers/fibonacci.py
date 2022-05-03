"""Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the
Nth number. """
import sys

sys.setrecursionlimit(100000)


def print_sequence(x):
    print(*x, sep=', ')


def fibonacci(n):
    x = []
    for n in range(n):
        if n == 0 or n == 1:
            x.append(1)
        else:
            x.append(x[n - 1] + x[n - 2])
    print_sequence(x)


def main():
    while True:
        entry = input('->> ')
        if entry == 'q':
            break
        if not entry.isdigit():
            print('Not a digit, try again, \'q\' to exit')
            continue
        fibonacci(int(entry))


if __name__ == '__main__':
    main()
