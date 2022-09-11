# https://www.acmicpc.net/problem/2753


import sys


def main():
    year = int(sys.stdin.readline())
    leap_year = 1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0
    sys.stdout.write("%d" % leap_year)


if __name__ == '__main__':
    main()
