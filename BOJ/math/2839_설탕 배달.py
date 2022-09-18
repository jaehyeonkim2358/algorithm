# https://www.acmicpc.net/problem/2839


import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    i = n//5
    ans = -1
    while i >= 0:
        if (n - 5 * i) % 3 == 0:
            ans = i + (n - 5 * i) // 3
            break
        i -= 1
    sys.stdout.write(f'{ans}')


if __name__ == '__main__':
    main()
