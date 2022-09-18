# https://www.acmicpc.net/problem/2775


import sys
import math


def main():
    tc = int(sys.stdin.readline())
    for _ in range(tc):
        k, n = int(sys.stdin.readline()), int(sys.stdin.readline())
        sys.stdout.write(f'{math.comb(k+n, k+1)}\n')


if __name__ == '__main__':
    main()
