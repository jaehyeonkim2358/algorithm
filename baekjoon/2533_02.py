def solution(edge, n):
    early_adopter = set()
    stack = []

    # 연결된 edge가 하나인 노드를 stack에 담기
    for i in range(1, n+1):
        if len(edge[i]) == 1:
            stack.append(i)
    
    # stack에는 항상 간선이 1개 이하인 노드만 존재함
    while stack:
        cur = stack.pop()
        if not edge[cur]: continue
        
        sVertex = edge[cur][0]
        early_adopter.add(sVertex)
        
        for v in edge[sVertex]:
            edge[v].remove(sVertex)

            if len(edge[v]) == 1:
                stack.append(v)
        edge[sVertex] = ()
        
    return len(early_adopter)


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    edge = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    ans = solution(edge, n)
    sys.stdout.write(f'{ans}')