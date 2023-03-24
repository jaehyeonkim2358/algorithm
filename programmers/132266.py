# https://school.programmers.co.kr/learn/courses/30/lessons/132266

def solution(n, roads, sources, destination):
    from collections import defaultdict
    answer = []
    adj_roads = defaultdict(list)
    for i in range(len(roads)):
        v, u = roads[i]
        adj_roads[v].append(u)
        adj_roads[u].append(v)

    dist = bfs(n, adj_roads, destination)
    for i in range(len(sources)):
        answer.append(dist[sources[i]])
    return answer


def bfs(n, roads, destination):
    from collections import deque
    dist = [-1] * (n+1)
    dist[destination] = 0

    queue = deque()
    queue.append(destination)
    while queue:
        cur = queue.popleft()
        d = dist[cur]
        for i in roads[cur]:
            if dist[i] == -1:
                dist[i] = d + 1
                queue.append(i)
    return dist
