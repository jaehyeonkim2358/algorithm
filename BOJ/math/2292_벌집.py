# https://www.acmicpc.net/problem/2292


import sys


def main():
    # 1, 6, 12, 18, 24
    # 1, 7, 19, 37, 61
    x = int(sys.stdin.readline().rstrip())
    idx = 0
    while x > 1:
        idx += 1
        x -= idx * 6
    sys.stdout.write(f'{idx + 1}')


if __name__ == '__main__':
    main()
