# https://www.acmicpc.net/problem/2533

import sys
sys.setrecursionlimit(10**6)


def solution(tree):
    answer = 0
    root = 1
    # tree_dp[node][0]: node가 얼리어답터인 경우 node를 포함한 서브트리의 얼리어답터 수
    # tree_dp[node][1]: node가 일반인인 경우 node를 포함한 서브트리의 얼리어답터 수
    tree_dp = dict()
    dfs(root, tree_dp, tree)
    answer = min(tree_dp[root][0], tree_dp[root][1])
    return answer


def dfs(current, tree_dp, tree):
    # 현재 노드가 얼리어답터 인 경우의 수를 갱신해준다.
    if current not in tree_dp:
        tree_dp[current] = [0, 0]
    tree_dp[current][0] = 1

    for adjacent_node in tree[current]:
        # adjacent_node가 current의 부모노드 인 경우도 존재함
        # 따라서 방문하지 않은 노드를 확인하기 위해 tree_dp의 key로 존재하는지를 확인
        if adjacent_node not in tree_dp:
            dfs(adjacent_node, tree_dp, tree)

            # 현재 노드가 얼리어답터 인 경우, 자식 노드가 얼리어답터, 일반인 중 어떤 경우일 때 최적해가 나오는지 알 수 없다.
            tree_dp[current][0] += min(tree_dp[adjacent_node][0], tree_dp[adjacent_node][1])

            # 현재 노드가 일반인인 경우, 자식 노드는 항상 얼리어답터이어야 한다.
            tree_dp[current][1] += tree_dp[adjacent_node][0]


if __name__ == '__main__':
    import sys
    N = int(sys.stdin.readline().rstrip())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        tree[u].append(v)
        tree[v].append(u)
    answer = solution(tree)
    sys.stdout.write(f'{answer}')