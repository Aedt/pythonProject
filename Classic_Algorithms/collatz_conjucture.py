"""Collatz Conjecture - Start with a number n > 1. Find the number of steps
it takes to reach one using the following process: If n is even, divide it
by 2. If n is odd, multiply it by 3 and add 1. """


def collatz(c):
    steps = 0
    while c > 1:
        if c % 2 == 0:
            c = c / 2
            steps += 1
            print(int(c), end=', ')
        else:
            c = 3 * c + 1
            steps += 1
            print(int(c), end=', ')
    print()
    print(f'Steps: {steps}')


def menu():
    while True:
        entry = input('->> ')
        if entry == 'q':
            break
        if not entry.isdigit():
            print('Not a digit, try again, \'q\' to quit')
            continue
        collatz(int(entry))


def main():
    menu()


if __name__ == '__main__':
    main()
