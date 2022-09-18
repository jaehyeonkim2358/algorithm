# https://www.acmicpc.net/problem/1193


import sys


def main():
    x = int(sys.stdin.readline().rstrip())
    for i in range(1, x+1):
        if (i + 1) * i // 2 >= x:
            dist = ((i + 1) * i // 2) - x
            break
    sys.stdout.write('%d/%d' % ((dist + 1, i - dist)[::(i % 2 * 2 - 1)]))


if __name__ == '__main__':
    main()
