import sys


def main():
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write('>' if a > b else '<' if a < b else '==')


if __name__ == '__main__':
    main()
