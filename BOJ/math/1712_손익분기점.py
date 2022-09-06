def main():
    a, b, c = map(int, input().split())
    ans = -1
    if b < c or (a == 0 and b <= c):
        ans = a//(c-b) + 1
    print(ans)


if __name__ == '__main__':
    main()
