# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    seq_sum = [0] * (len(sequence) + 1)
    for i in range(len(sequence)):
        seq_sum[i+1] = seq_sum[i] + sequence[i]
    answer = find(seq_sum, k)
    return answer

def find(seq_sum, k):
    left = 0
    right = 1
    s = 0
    e = 0
    min_length = len(seq_sum) + 1
    
    while left < len(seq_sum) and right < len(seq_sum):
        if seq_sum[right]-seq_sum[left] != k:
            if right == len(seq_sum)-1 or seq_sum[right]-seq_sum[left] > k:
                left += 1
            else: # seq_sum[right]-seq_sum[left] < k
                right += 1
        else:
            if min_length > right - left:
                min_length = right - left
                s = left
                e = right-1
            left += 1
            right += 1
    return [s, e]