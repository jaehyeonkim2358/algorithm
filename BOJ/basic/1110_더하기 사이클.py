# https://www.acmicpc.net/problem/1110


def main():
    n = int(input())
    tmp = (n % 10) * 10 + (n // 10 + n % 10) % 10
    cnt = 1
    while tmp != n:
        tmp = (tmp % 10) * 10 + (tmp // 10 + tmp % 10) % 10
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
