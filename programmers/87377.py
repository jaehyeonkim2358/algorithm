# https://school.programmers.co.kr/learn/courses/30/lessons/87377

import sys
INF = sys.maxsize

def solution(line):
    answer = []
    point_set = set()
    min_x, min_y = INF, INF
    for i in range(len(line)):
        A, B, E = line[i]
        for j in range(i+1, len(line)):
            C, D, F = line[j]
            x_c, y_c, p = (B*F - E*D), (E*C - A*F), (A*D - B*C)
            if p == 0: continue
            x = x_c // p
            y = y_c // p
            if x*p == x_c and y*p == y_c:
                point_set.add((x, y))
                min_x = min(min_x, x)
                min_y = min(min_y, y)
    
    offset_removed_point_list = []
    width, height = -INF, -INF
    for point in point_set:
        nx = point[0]-min_x
        ny = point[1]-min_y
        offset_removed_point_list.append((nx, ny))
        width = max(width, nx+1)
        height = max(height, ny+1)
    
    answer = [['.'] * width for _ in range(height)]
    for (x, y) in offset_removed_point_list:
        answer[height-1-y][x] = '*'
    
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    return answer