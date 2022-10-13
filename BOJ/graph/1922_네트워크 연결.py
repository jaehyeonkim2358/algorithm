import sys
from collections import defaultdict


class Edge:
    def __init__(self, start, dest, cost):
        self.start = start
        self.dest = dest
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = []
for _ in range(m):
    u, v, d = map(int, sys.stdin.readline().split())
    graph.append(Edge(u, v, d))

graph.sort()


parent = [i for i in range(n+1)]
rank = [0] * (n+1)


def union(a, b):
    a = find(a)
    b = find(b)
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
    
    if rank[a] == rank[b]:
        rank[a] += 1


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

answer = 0
for g in graph:
    if find(g.start) != find(g.dest):
        union(g.start, g.dest)
        answer += g.cost

print(answer)
