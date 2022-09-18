# https://www.acmicpc.net/problem/9020


import sys


def main():
    pn = [True] * 10001
    pn[0] = pn[1] = False
    for i in range(2, 10001):
        if pn[i] is True:
            for j in range(2*i, 10001, i):
                pn[j] = False
    _, *ns = open(0).read().split()
    for n in map(int, ns):
        for p in range(n//2, 1, -1):
            if pn[p] is True and pn[n-p] is True:
                sys.stdout.write("%d %d\n" % (p, n-p))
                break


if __name__ == '__main__':
    main()
