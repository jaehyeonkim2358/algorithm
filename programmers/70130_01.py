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
        idx, count, length, pre = 0, 0, 0, -1
        while idx < len(a):
            if count % 2 == 0:
                count += 1
                pre = a[idx]
            else:
                if check(a[idx], pre, num):
                    count += 1
                    length += 2
            idx += 1
        answer = max(answer, length)
    return answer

def check(current, previous, common):
    return (current == common or previous == common) and current != previous    