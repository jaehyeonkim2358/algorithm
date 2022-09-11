# https://www.acmicpc.net/problem/1065

import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    sys.stdout.write(f'{sum(i < 100 or i // 100 == 2 * (i // 10 % 10) - i % 10 for i in list(range(1, n + 1)))}')


if __name__ == '__main__':
    main()
