# https://www.acmicpc.net/problem/10809


import sys


def main():
    s = sys.stdin.readline().rstrip()
    print(*map(s.find, map(chr, range(ord('a'), ord('z')+1))))


if __name__ == '__main__':
    main()
