# https://school.programmers.co.kr/learn/courses/30/lessons/60062

flag = False

def solution(n, weak, dist):
    weaks = []
    answer = -1
    for i in range(len(weak)):
        weaks.append(weak[i:]+list(map(lambda x: x+n, weak[:i])))

    for i in range(1, len(dist)+1):
        for j in range(len(weaks)):
            used = [False] * len(dist)
            dfs(0, i, dist, [], weaks[j], used)
            if flag:
                return i
    return answer

def dfs(depth, N, dist, result, weak, used):
    global flag
    if flag: return
    if depth == N:
        if calc(result, weak, N):
            flag = True
        return

    for i in range(len(dist)):
        if not used[i]:
            used[i] = True
            result.append(dist[i])
            dfs(depth+1, N, dist, result, weak, used)
            result.pop()
            used[i] = False

def calc(dist, weak, N):
    idx = 1
    cur = 0
    recent = 0
    while idx < len(weak) and cur < N:
        if dist[cur] >= weak[idx]-weak[idx-1] + recent:
            recent += weak[idx]-weak[idx-1]
        else:
            cur += 1
            recent = 0
        idx += 1

    return cur < N
