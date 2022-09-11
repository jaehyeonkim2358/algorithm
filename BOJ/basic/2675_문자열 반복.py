# https://www.acmicpc.net/problem/2675


def main():
    for r, _, *s, _ in [*open(0)][1:]:
        print(''.join(c * int(r) for c in s))


if __name__ == '__main__':
    main()
