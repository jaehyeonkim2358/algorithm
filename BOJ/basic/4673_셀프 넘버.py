# https://www.acmicpc.net/problem/4673


import sys


def main():
    self_number = [True for row in range(10001)]
    for i in range(1, len(self_number)):
        result = tmp = i
        while tmp > 0:
            result += tmp % 10
            tmp //= 10
        if result < len(self_number):
            self_number[result] = False

    for i in range(1, len(self_number)):
        if self_number[i]:
            sys.stdout.write(f'{i}\n')


if __name__ == '__main__':
    main()
