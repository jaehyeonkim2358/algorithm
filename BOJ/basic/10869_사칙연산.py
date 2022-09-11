# https://www.acmicpc.net/problem/10869


import sys


def main():
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{a + b}\n{a - b}\n{a * b}\n{a // b}\n{a % b}')


if __name__ == '__main__':
    main()
