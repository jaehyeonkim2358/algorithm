import sys
INF = sys.maxsize

def solution(arr):
    num_count = len(arr)//2 + 1
    max_dp = [[-INF] * num_count for _ in range(num_count)]
    min_dp = [[INF] * num_count for _ in range(num_count)]
    for i in range(num_count):
        max_dp[i][i] = int(arr[i*2])
        min_dp[i][i] = int(arr[i*2])
    
    for size in range(1, num_count):
        for start in range(num_count-size):
            end = start + size
            for i in range(start, end):
                op = arr[i*2+1]
                if op == '+':
                    max_dp[start][end] = max(max_dp[start][end], max_dp[start][i] + max_dp[i+1][end])
                    min_dp[start][end] = min(min_dp[start][end], min_dp[start][i] + min_dp[i+1][end])
                else:
                    max_dp[start][end] = max(max_dp[start][end], max_dp[start][i] - min_dp[i+1][end])
                    min_dp[start][end] = min(min_dp[start][end], min_dp[start][i] - max_dp[i+1][end])
                    
    
    return max_dp[0][num_count-1]