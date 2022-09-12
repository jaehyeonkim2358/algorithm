# https://www.acmicpc.net/problem/1316


import sys


def main():
    n = int(sys.stdin.readline())
    ans = 0
    for _ in range(n):
        s = sys.stdin.readline().rstrip()
        pre = s[0]
        used = [False for _ in range(26)]
        used[ord(pre) - ord('a')] = True
        flag = False
        is_break = False
        for i in range(1, len(s)):
            if pre == s[i]:
                flag = True
            else:
                flag = False
                pre = s[i]
            if flag is False and used[ord(s[i]) - ord('a')] is True:
                is_break = True
                break
            used[ord(s[i]) - ord('a')] = True
        ans += 1 if is_break is False else 0
    sys.stdout.write(f'{ans}')


if __name__ == '__main__':
    main()
