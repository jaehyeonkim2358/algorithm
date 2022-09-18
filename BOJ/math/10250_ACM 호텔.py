# https://www.acmicpc.net/problem/10250


import sys


def main():
    _, *ps = open(0)
    for p in ps:
        h, w, n = map(int, p.split())
        sys.stdout.write(f'{[h, *list(range(1, h))][n % h]}{str(n // h + (n % h > 0)).zfill(2)}')


if __name__ == '__main__':
    main()
