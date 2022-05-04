"""next prime number - have the program find prime numbers until the user
chooses to stop asking for the next one.
"""


def next_prime(x):

    for i in range(x + 1, 2 * x - 1):
        k = 0
        for j in range(1, i + 1):
            if i % j == 0:
                k += 1

        if k == 2:
            return i
            break


def main():
    while True:
        entry = input('->> ')
        if entry == 'q':
            break
        if not entry.isdigit():
            print('Not a digit, try again, \'q\' to quit.')
            continue
        print(next_prime(int(entry)))


if __name__ == '__main__':
    main()
