# https://www.acmicpc.net/problem/5622


import sys


def main():
    s = sys.stdin.readline().rstrip()
    ans = 0
    for c in s:
        ans += 1 + int("22233344455566677778889999"[ord(c)-ord("A")])
    sys.stdout.write(f'{ans}')


if __name__ == '__main__':
    main()
