# https://school.programmers.co.kr/learn/courses/30/lessons/92343

ans = 0

def solution(info, edges):
    size = len(info)
    adj = [[] for _ in range(size)]
    visited = [False] * (1<<size)
    for i in range(len(edges)):
        v, u = edges[i]
        adj[v].append(u)
    solve(visited, 1, info, adj)
    return ans

def solve(visited, state, info, adj):
    global ans

    # 현재 상태를 이미 방문한 적이 있는 경우 종료
    if visited[state]:
        return None
    
    # 방문한 적 없는 경우 방문 체크
    visited[state] = True

    # 현재 상태의 양, 늑대 수 확인
    sheep, wolf = 0, 0
    for i in range(len(info)):
        if state & (1<<i):
            wolf += info[i]
            sheep += info[i] ^ 1
    
    # 늑대가 양보다 많거나 같으면 종료
    if sheep <= wolf:
        return None
    
    # 최대값 갱신
    ans = max(ans, sheep)

    # 현재 상태에서 방문 가능한 노드를 순회하며 재귀 호출
    for i in range(len(info)):
        if not (state & (1<<i)):
            continue
        for next in adj[i]:
            solve(visited, state | (1<<next), info, adj)