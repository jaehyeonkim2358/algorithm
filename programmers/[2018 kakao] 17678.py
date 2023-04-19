# https://school.programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    answer = ''
    start_time = time_to_int('09:00')
    tt_size = len(timetable)
    timetable = list(map(time_to_int, timetable))
    timetable.sort()
    
    conns_time = 0
    passenger_index = 0
    for i in range(n):
        shuttle_time = start_time + t*i
        p_cnt = 0
        max_p_time = 0
        while passenger_index < tt_size and p_cnt < m:
            if timetable[passenger_index] <= shuttle_time:
                p_cnt += 1
                max_p_time = max(max_p_time, timetable[passenger_index])
            else:
                break
            passenger_index += 1
        if p_cnt == m:
            conns_time = max_p_time-1
        else:
            conns_time = shuttle_time
    answer = int_to_time(conns_time)
    return answer

def time_to_int(time:str) -> int:
    h, m = map(int, time.split(':'))
    return h*60 + m

def int_to_time(i_time:int) -> str:
    return f'{i_time//60:02d}:{i_time%60:02d}'