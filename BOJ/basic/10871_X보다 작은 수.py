# https://www.acmicpc.net/problem/10871


import sys


def main():
    n, x = map(int, sys.stdin.readline().split())
    print(*list(filter(lambda i: i < x, list(map(int, sys.stdin.readline().split())))))


if __name__ == '__main__':
    main()
