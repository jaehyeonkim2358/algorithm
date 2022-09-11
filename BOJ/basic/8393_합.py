import sys


def main():
    n = int(sys.stdin.readline())
    sys.stdout.write("%d" % (n*(n+1)//2))


if __name__ == '__main__':
    main()
