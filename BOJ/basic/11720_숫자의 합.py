# https://www.acmicpc.net/problem/11720


import sys


def main():
    sys.stdout.write(f'{sum(map(int, [*open(0)][1:][0].rstrip()))}')


if __name__ == '__main__':
    main()
