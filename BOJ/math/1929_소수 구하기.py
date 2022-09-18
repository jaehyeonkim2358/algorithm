# https://www.acmicpc.net/problem/1929


import sys


def main():
    max_num = 1000001
    pn = [True for _ in range(max_num)]
    pn[0] = False
    pn[1] = False
    for i in range(2, 1001):
        if pn[i] is False:
            continue
        for j in range(2, max_num//i+2):
            if i * j < max_num:
                pn[i * j] = False
    m, n = map(int, sys.stdin.readline().split())
    print(*[i for i in range(m, n+1) if pn[i] is True], sep="\n", end='')


if __name__ == '__main__':
    main()
