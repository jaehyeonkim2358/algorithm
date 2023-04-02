# https://www.acmicpc.net/problem/4963

import sys
sys.setrecursionlimit(10**6)

move = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

def solution(_map:list):
    answer = 0
    for i in range(len(_map)):
        for j in range(len(_map[i])):
            if _map[i][j] == 1:
                _map[i][j] += 1
                answer += 1
                dfs(_map, i, j)
    return answer

def dfs(_map, r, c):
    for dy, dx in move:
        if check(r + dy, c + dx, _map) and _map[r + dy][c + dx] == 1:
            _map[r + dy][c + dx] += 1
            dfs(_map, r + dy, c + dx)

def check(x, y, _map):
    if x < 0 or x >= len(_map): return False
    if y < 0 or y >= len(_map[0]): return False
    return True


if __name__ == "__main__":
    input = sys.stdin.readline
    print = sys.stdout.write
    ans = []
    _map = []
    while True:
        w, h = map(int, input().rstrip().split())
        if w == h == 0: break

        for _ in range(h):
            _map.append(list(map(int, input().rstrip().split())))
        ans.append(solution(_map))
        _map.clear()

    for i in range(len(ans)):
        print(str(ans[i]))
        print('\n')