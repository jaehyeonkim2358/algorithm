count = 0

def solution(tree, root, D):
    if -1 not in tree:      return 0
    if len(tree[-1]) == 0:  return 0
    if len(tree[root]) == 0:return 1
    
    dfs(tree, root, D)
    return count

def dfs(tree, root, D):
    global count
    if root not in tree or len(tree[root]) == 0:
        count += 1
        return
    for next in tree[root]:
        dfs(tree, next, D)

if __name__ == '__main__':
    import sys
    # 입력
    N = int(sys.stdin.readline().rstrip())
    T = list(map(int, sys.stdin.readline().split()))
    D = int(sys.stdin.readline().rstrip())

    # tree 초기화
    DP = -1
    root = -1
    tree = {}
    for i in range(len(T)):
        if T[i] not in tree:
            tree[T[i]] = set()
        tree[T[i]].add(i)
        if T[i] == -1:
            root = i
        if i == D:
            DP = T[i]
    tree[D] = []        # D의 자식 노드 삭제
    tree[DP].remove(D)  # D의 부모노드에서 D삭제

    answer = solution(tree, root, D)
    sys.stdout.write(f'{answer}')