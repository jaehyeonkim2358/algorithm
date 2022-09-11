# https://www.acmicpc.net/problem/2439


import sys


def main():
    num = int(sys.stdin.readline().rstrip())
    for i in range(num):
        sys.stdout.write(" " * (num - i - 1) + "*" * (i + 1) + "\n")


if __name__ == '__main__':
    main()
