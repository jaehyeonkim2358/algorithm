import sys


def main():
    a, b = map(float, input().split())
    sys.stdout.write("%d\n" % (a + b))
    sys.stdout.write("%d\n" % (a - b))
    sys.stdout.write("%d\n" % (a * b))
    sys.stdout.write("%d\n" % (a // b))
    sys.stdout.write("%d" % (a % b))


if __name__ == '__main__':
    main()
