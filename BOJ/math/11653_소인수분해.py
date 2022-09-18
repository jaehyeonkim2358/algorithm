# https://www.acmicpc.net/problem/11653


import sys
import math


def main():
    n = int(sys.stdin.readline().rstrip())
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            sys.stdout.write(f'{i}\n')
            n //= i
    if n != 1:
        sys.stdout.write(f'{n}')


if __name__ == '__main__':
    main()
