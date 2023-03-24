# https://school.programmers.co.kr/learn/courses/30/lessons/92343

import sys
sys.setrecursionlimit(10**6)

ans = 0

def solution(info, edges):
    # 인접 리스트 생성
    adj = [[] for _ in range(len(info))]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
    
    # 방문 가능한 노드들을 담을 리스트 생성
    nodes = []

    solve(0, nodes, adj, 0, 0, info)
    return ans

def solve(current:int, nodes:list, adj:list, sheep:int, wolf:int, info:list):
    global ans
    
    # 현재 방문한 노드에 따라 양 또는 늑대 수 증가
    sheep += info[current] ^ 1
    wolf += info[current]

    # 현재 양의 수가 최대값보다 크다면 갱신
    ans = max(ans, sheep)

    # 만약 늑대의 수가 양의 수보다 같거나 크면 종료
    if sheep <= wolf:   return
    
    # 현재 노드의 자식노드는 
    # 앞으로 현재 노드의 모든 subtree의 자식 노드들이 방문 가능한 노드임
    for i in adj[current]:
        nodes.append(i)

    # 방문 가능한 노드를 순회하며 재귀호출
    # 이때, 방문 대상인 노드는 방문 가능한 노드 목록(nodes)에서 제외해야함.
    # 또한, nodes는 함수가 호출될 때 마다 독립적으로 존재해야함(deep copy)
    for i in range(len(nodes)):
        next = nodes[i]
        solve(next, nodes[:i]+nodes[i+1:], adj, sheep, wolf, info)