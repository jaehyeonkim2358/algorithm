# https://www.acmicpc.net/problem/9498


import sys


def main():
    score = int(sys.stdin.readline())
    grade = 'F'
    if 100 >= score >= 90:
        grade = 'A'
    elif 89 >= score >= 80:
        grade = 'B'
    elif 79 >= score >= 70:
        grade = 'C'
    elif 69 >= score >= 60:
        grade = 'D'

    sys.stdout.write(grade)


if __name__ == '__main__':
    main()
