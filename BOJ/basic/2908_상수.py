# https://www.acmicpc.net/problem/2908


import sys


def main():
    sys.stdout.write(f'{max(map(int, sys.stdin.readline().rstrip()[::-1].split()))}')


if __name__ == '__main__':
    main()
