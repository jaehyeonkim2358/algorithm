# https://www.acmicpc.net/problem/1157


import sys


def main():
    s = sys.stdin.readline().rstrip().upper()
    al = [0 for i in range(26)]
    for c in {*s}:
        al[ord(c) - ord('A')] = s.count(c)
    print('?' if al.count(max(al)) > 1 else chr(al.index(max(al)) + ord('A')))


if __name__ == '__main__':
    main()
