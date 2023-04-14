# https://school.programmers.co.kr/learn/courses/30/lessons/150367

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(is_binary_tree(num_to_bin(n)))
    return answer
    

# 10진수 정수 NUM을 2진수 문자열로 바꾼 뒤, 2의 승수 -1 길이로 만들어서 반환
# 만들어진 이진수의 길이를 그 길이 이상의 가장 가까운 '2의 승수-1'와 비교해서
# 작다면 작은만큼 왼쪽에 0을 붙여줌
def num_to_bin(num:int) -> str:
    ori_bin = str(bin(num))[2:]
    i, size = 0, 0
    while len(ori_bin) > size + (1<<i):
        size += (1<<i)
        i += 1
    zero_bits = size + (1<<i) - len(ori_bin)
    return ('0' * zero_bits) + ori_bin
    

# 문제 조건에 맞는 이진트리로 변환 가능한지 여부를 반환
# 가능   -> 1
# 불가능 -> 0
def is_binary_tree(bin_num:str) -> int:
    RET_VAL = (0, 1)        # 0 or 1 반환
    flag = [True]
    
    find(0, len(bin_num)-1, bin_num, flag)
    
    return RET_VAL[flag[0]]
    

# 더미를 루트로 하는 서브트리의 자식 중 더미가 아닌 노드가 있다면
# 표현 불가능한 수로 판단 해서 flag[0] = False,
def find(s, e, arr, flag) -> str:
    if s>=e or not flag[0]: return arr[s]
    
    m = (s+e)//2
    left  = find(s, m-1, arr, flag)
    right = find(m+1, e, arr, flag)
    
    if arr[m] == '0' and (left == '1' or right == '1'):
        flag[0] = False
    return arr[m]