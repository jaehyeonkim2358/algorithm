# https://www.acmicpc.net/problem/2581


def main():
    m, n = int(input()), int(input())
    m = 2 if m == 1 else m
    sum_p = 0
    min_p = n
    for k in range(m, n + 1):
        flag = True
        for i in range(2, int(k ** (1 / 2)) + 1):
            if k % i == 0:
                flag = False
                break
        if flag:
            sum_p += k
            min_p = min(min_p, k)
    print(sum_p and f'{sum_p}\n{min_p}' or -1)


if __name__ == '__main__':
    main()
