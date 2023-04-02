# https://www.acmicpc.net/problem/2468

import sys
from collections import deque
sys.setrecursionlimit(10**6)

def solution(_map, _min, _max):
    answer = 1
    for h in range(_min, _max+1):
        answer = max(answer, solve(_map, h))
    return answer

def solve(_map, h):
    size = len(_map)
    mmap = [[False] * size for _ in range(size)]
    move = ((1,0), (0,1), (-1,0), (0,-1))

    def check(x, y):
        if x < 0 or x >= size: return False
        if y < 0 or y >= size: return False
        return True

    def _bfs(mmap, r, c):
        q = deque([(r, c)])
        mmap[r][c] = True
        while q:
            y, x = q.popleft()
            for dy, dx in move:
                if check(y+dy, x+dx) and not mmap[y+dy][x+dx] and _map[y+dy][x+dx] > h:
                    mmap[y+dy][x+dx] = True
                    q.append((y+dy, x+dx))

    count = 0
    for i in range(size):
        for j in range(size):
            if not mmap[i][j] and _map[i][j] > h:
                _bfs(mmap, i, j)
                count += 1
    return count

if __name__ == "__main__":
    input = sys.stdin.readline
    print = sys.stdout.write
    n = int(input().rstrip())
    _map = []
    _min = sys.maxsize
    _max = -1
    for _ in range(n):
        tmp = list(map(int, input().rstrip().split()))
        _map.append(tmp)
        _min = min(_min, min(tmp))
        _max = max(_max, max(tmp))

    print(str(solution(_map, _min, _max)))
