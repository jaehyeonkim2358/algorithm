import sys


def main():
    num = int(sys.stdin.readline())
    for i in range(1, 10):
        sys.stdout.write("%d * %d = %d\n" % (num, i, num*i))


if __name__ == '__main__':
    main()
