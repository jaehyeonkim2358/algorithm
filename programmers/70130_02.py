# https://school.programmers.co.kr/learn/courses/30/lessons/70130

def solution(a):
    answer = 0
    num_count = dict()
    for i in range(len(a)):
        if a[i] not in num_count:
            num_count[a[i]] = 0
        num_count[a[i]] += 1
        
    for (num, val) in num_count.items():
        if answer >= val*2: continue
        length = 0
        i = 1
        while i < len(a):
            if a[i] == a[i-1] or \
                (a[i] != num and a[i-1] != num):
                i += 1
                continue
            i += 2
            length += 2
        answer = max(answer, length)
    return answer
