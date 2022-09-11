# https://www.acmicpc.net/problem/9498


import sys


def main():
    score = int(sys.stdin.readline()) - 60
    sys.stdout.write(f'{"FDCBA"[0 if score < 0 else 4 if score == 40 else score // 10 + 1]}')


if __name__ == '__main__':
    main()
