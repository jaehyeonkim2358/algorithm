# https://www.acmicpc.net/problem/2480


import sys


def main():
    dice1, dice2, dice3 = map(int, sys.stdin.readline().split())
    reward = 0
    if dice1 == dice2 == dice3:
        reward = 10000 + dice1 * 1000
    elif dice1 != dice2 and dice2 != dice3 and dice1 != dice3:
        reward = max(dice1, dice2, dice3) * 100
    else:
        if dice1 == dice2:
            reward = 1000 + dice1 * 100
        else:
            reward = 1000 + dice3 * 100
    sys.stdout.write("%d" % reward)


if __name__ == '__main__':
    main()
