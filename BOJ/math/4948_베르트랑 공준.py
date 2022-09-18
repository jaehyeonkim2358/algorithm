# https://www.acmicpc.net/problem/4948


import sys


def main():
    n = 123456 * 2
    pn = [True] * (n + 1)
    pn[0] = pn[1] = False
    for i in range(2, int(n ** (1 / 2)) + 2):
        if pn[i] is True:
            for j in range(2 * i, n + 1, i):
                pn[j] = False
    for num in map(int, open(0).read().split()):
        sys.stdout.write(f'{sum(pn[i] for i in range(num + 1, num * 2 + 1))}\n' if num != 0 else '')


if __name__ == '__main__':
    main()
