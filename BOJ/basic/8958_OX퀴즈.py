# https://www.acmicpc.net/problem/8958


def score_sum(n):
    return (n * (n + 1)) // 2


def main():
    _, *score_list = open(0).read().split()
    for score in score_list:
        print(sum([score_sum(len(i)) for i in score.split('X')]))


if __name__ == '__main__':
    main()
