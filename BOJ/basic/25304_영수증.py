import sys


def main():
    total_price = int(sys.stdin.readline())
    num = int(sys.stdin.readline())
    price_sum = 0
    for i in range(num):
        p, c = map(int, sys.stdin.readline().split())
        price_sum += p * c
    sys.stdout.write(["No", "Yes"][total_price == price_sum])


if __name__ == '__main__':
    main()
