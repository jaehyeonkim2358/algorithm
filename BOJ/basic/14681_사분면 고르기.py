import sys


def main():
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())
    sys.stdout.write("%d" % (1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 3 if x < 0 and y < 0 else 4))


if __name__ == '__main__':
    main()
