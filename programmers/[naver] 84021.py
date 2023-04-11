# https://school.programmers.co.kr/learn/courses/30/lessons/84021

from collections import deque

def solution(game_board, table):
    game_board_key = 0
    table_key = 1
    
    # block 마지막에 [offset_y, offset_x] 저장됨
    board_list = get_list(game_board, game_board_key)
    block_list = get_list(table, table_key)
    
    # block 마지막에 [y_width, x_width, 사각형 수] 저장됨
    sub_offset(board_list)
    sub_offset(block_list)
    
    return get_count(board_list, block_list)


def bfs(start: tuple, table: list, key: int):
    not_key = ((key+1)<<3)
    move = ((1,0),(0,1),(-1,0),(0,-1))
    size = len(table)
    queue = deque([start])
    block = [[start[0], start[1]], ]
    min_x, min_y = start[1], start[0]
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny = y+dy
            nx = x+dx
            if 0<=ny<size and 0<=nx<size and table[ny][nx]==key:
                table[ny][nx] = not_key
                queue.append((ny, nx))
                block.append([ny, nx])
                min_y = min(min_y, ny)
                min_x = min(min_x, nx)
    block.append([min_y, min_x])
    return block


def get_list(_2d_array, key):
    not_key = ((key+1)<<3)
    size = len(_2d_array)
    result = []
    for i in range(size*size):
        if _2d_array[i//size][i%size] == key:
            _2d_array[i//size][i%size] = not_key
            result.append(bfs((i//size, i%size), _2d_array, key))
    return result
    

def sub_offset(_3d_array):
    for i in range(len(_3d_array)):
        off_y, off_x = _3d_array[i][-1]
        x_width, y_width = 0, 0
        for j in range(0, len(_3d_array[i])-1, 1):
            _3d_array[i][j][0] -= off_y
            _3d_array[i][j][1] -= off_x
            y_width = max(y_width, _3d_array[i][j][0])
            x_width = max(x_width, _3d_array[i][j][1])
        _3d_array[i][-1][0] = y_width + 1
        _3d_array[i][-1][1] = x_width + 1
        _3d_array[i][-1].append(len(_3d_array[i])-1)


def make_fit_board(_2d_array):
    y_size = _2d_array[-1][0]
    x_size = _2d_array[-1][1]
    result = [[0] * x_size for _ in range(y_size)]
    for i in range(0, len(_2d_array)-1, 1):
        result[_2d_array[i][0]][_2d_array[i][1]] = 1
    return result


def compare_2_board(board1, board2):
    if len(board1) != len(board2): return -1
    if len(board1[0]) != len(board2[0]): return -1
    size = len(board1)
    count = 0
    for i in range(0, size, 1):
        for j in range(0, size, 1):
            if board1[i][j] != board2[i][j]:
                return -1
            else:
                if board1[i][j] == 1: count += 1
    return count

# 정사각 배열을 회전
def rotate(_2d_array):
    y_size = len(_2d_array)
    x_size = len(_2d_array[0])
    result = [[0] * y_size for _ in range(x_size)]
    for i in range(0, x_size, 1):
        for j in range(0, y_size, 1):
            result[i][j] = _2d_array[j][x_size-1-i]
    return result


def get_count(board_list, block_list):
    used_block = [False] * len(block_list)
    count = 0
    # game_board를 먼저 순회
    for i in range(len(board_list)):
        tmp_board = make_fit_board(board_list[i])
        used_flag = False
        # table을 순회하며 block을 꺼내기
        for j in range(len(block_list)):
            # 사용된 블럭은 비교하지 않음
            if used_block[j]: continue
            
            board_long = board_list[i][-1][0] if board_list[i][-1][0] > board_list[i][-1][1] else board_list[i][-1][1]
            board_short = board_list[i][-1][0] if board_long == board_list[i][-1][1] else board_list[i][-1][1]
            board_count = board_list[i][-1][2]

            block_long = block_list[j][-1][0] if block_list[j][-1][0] > block_list[j][-1][1] else block_list[j][-1][1]
            block_short = block_list[j][-1][0] if block_long == block_list[j][-1][1] else block_list[j][-1][1]
            block_count = block_list[j][-1][2]

            # 넓이 또는 사각형 갯수가 다른 블럭은 비교하지 않음
            if board_long != block_long: continue
            if board_short != block_short: continue
            if board_count != block_count: continue
            
            # 블록을 돌려가며 비교
            tmp_block = make_fit_board(block_list[j])
            for _ in range(4):
                cnt = compare_2_board(tmp_board, tmp_block)
                if cnt >= 0:
                    used_flag = True
                    count += cnt
                    break
                tmp_block = rotate(tmp_block)
            if used_flag:
                used_block[j] = True
                break
    return count