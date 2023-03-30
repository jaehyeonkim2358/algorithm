# https://school.programmers.co.kr/learn/courses/30/lessons/77886

T = ['1', '1', '0']

def solution(s):
    answer = []
    for i in range(len(s)):
        stack = []
        idx = 0
        count = 0
        while idx < len(s[i]):
            stack.append(s[i][idx])
            while len(stack) >= 3 and stack[-3:] == T:
                count += 1
                for _ in range(3):
                    stack.pop()
            idx += 1
        insert = -1
        for j in range(len(stack)-1, -1, -1):
            if stack[j] == "0":
                insert = j
                break
        answer.append(''.join(stack[:insert+1]+T*count+stack[insert+1:]))
    return answer