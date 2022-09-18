# https://www.acmicpc.net/problem/2869


import sys


def main():
    a, b, v = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{(v - a) // (a - b) + 1 + ((v - a) % (a - b) != 0)}')


if __name__ == '__main__':
    main()
