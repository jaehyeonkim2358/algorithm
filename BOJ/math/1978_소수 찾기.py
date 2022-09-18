# https://www.acmicpc.net/problem/1978


import sys


def main():
    ans = sum(all(n % j for j in range(2, int(n ** (1 / 2)) + 1)) * n > 1 for n in
              map(int, open(0).read().split('\n')[1].split()))
    sys.stdout.write(f'{ans}')


if __name__ == '__main__':
    main()
