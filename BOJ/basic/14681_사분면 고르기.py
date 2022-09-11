# https://www.acmicpc.net/problem/14681


import sys


def main():
    x, y = map(int, open(0))
    sys.stdout.write(f'{"1342"[0 if x * y > 0 else 2:][0 if x > 0 else 1]}')


if __name__ == '__main__':
    main()