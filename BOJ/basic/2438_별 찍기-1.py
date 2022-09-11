# https://www.acmicpc.net/problem/2438


import sys


def main():
    num = int(sys.stdin.readline().rstrip())
    for i in range(num):
        sys.stdout.write("*"*(i+1)+"\n")


if __name__ == '__main__':
    main()
