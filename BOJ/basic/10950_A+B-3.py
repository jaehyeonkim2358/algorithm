# https://www.acmicpc.net/problem/10950


import sys


def main():
    testcase_num = int(sys.stdin.readline())
    for i in range(testcase_num):
        a, b = map(int, sys.stdin.readline().split())
        sys.stdout.write("%d\n" % (a + b))


if __name__ == '__main__':
    main()
