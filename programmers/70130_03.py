# https://school.programmers.co.kr/learn/courses/30/lessons/70130

def solution(a):
    answer = 0
    dic = {}
    check = {}
    for i in range(len(a)):
        dic[i] = 0
        check[i] = -2
    
    for i in range(len(a) - 1):
        if a[i] != a[i+1]:
            if check[a[i]] != i-1:
                dic[a[i]] += 1
                check[a[i]] = i
            if check[a[i+1]] != i-1:
                dic[a[i+1]] += 1
                check[a[i+1]] = i
            answer = max(answer, dic[a[i]], dic[a[i+1]])

    return answer * 2