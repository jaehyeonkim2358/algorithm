from heapq import heappop, heappush
from collections import defaultdict

def solution(operations):
    max_heap = []
    min_heap = []
    counter = defaultdict(int)
    heap_size = 0
    for i in range(len(operations)):
        cmd, num = operations[i].split()
        if cmd == 'I':
            num = int(num)
            heappush(min_heap, num)
            heappush(max_heap, -num)
            counter[num] += 1
            heap_size += 1
        else:
            if heap_size > 0:
                target_heap = max_heap if operations[i][2:] == '1' else min_heap
                sign = -1 if target_heap == max_heap else 1
                number = erase_used_number(target_heap, counter, sign)
                counter[number] -= 1
                heap_size -= 1
            else:
                heap_size = 0
                max_heap = []
                min_heap = []
                    
    if heap_size > 0:
        max_num = erase_used_number(max_heap, counter, -1)
        min_num = erase_used_number(min_heap, counter, 1)
        print(max_num, min_num)
    else:
        print('EMPTY')
    
def erase_used_number(heap, counter, sign):
    if len(heap) > 0:
        result = heappop(heap)
        while counter[result*sign] == 0:
            result = heappop(heap)
        return result*sign

# if __name__ == '__main__':
#     import sys
#     T = int(sys.stdin.readline().rstrip())
#     while T > 0:
#         T -= 1
#         N = int(sys.stdin.readline().rstrip())
#         operations = []
#         for _ in range(N):
#             operations.append(sys.stdin.readline().rstrip())
#         solution(operations)