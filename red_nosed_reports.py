from enum import Enum
SOLVE = True 

def get_input_list(): 
    if SOLVE:
        with open('input2.txt', 'r') as f: 
            return [
                list(map(int, s.split()))
                for s in f.readlines()
            ]
    else: 
        return [
            [7, 6, 4, 2, 1], 
            [1, 2, 7, 8, 9], 
            [9, 7, 6, 2, 1], 
            [1, 3, 2, 4, 5], 
            [8, 6, 4, 4, 1], 
            [1, 3, 6, 7, 9],
        ]

IncrType = Enum('IncrType', [
    ('INCREMENT', 1), 
    ('DECREMENT', 2), 
    ('MIXED', 3),
])

def list_incr_type(l: list[int]):
    smaller, bigger = (0, 0)
    n = len(l)
    for i in range(1, n):
        if l[i-1] < l[i]: bigger += 1 
        if l[i-1] > l[i]: smaller += 1 
    if n-1 == bigger: return IncrType.INCREMENT
    if n-1 == smaller: return IncrType.DECREMENT
    return IncrType.MIXED

def get_gap_range(l: list[int]):
    init_gap = abs(l[1] - l[0])
    min_gap, max_gap = (init_gap, init_gap)
    for i in range(2, len(l)):
        min_gap = min(min_gap, abs(l[i] - l[i-1]))
        max_gap = max(max_gap, abs(l[i] - l[i-1]))
    return range(min_gap, max_gap + 1)

def is_subset(needle: range, hay: range): 
    return hay.start <= needle.start and needle.stop <= hay.stop
    
def is_safe(l: list[int]):
    return list_incr_type(l) != IncrType.MIXED \
        and is_subset(get_gap_range(l), range(1, 4))

def generous_lists(l: list[int]):
    ret = [] 
    ret.append(l)
    for i in range(len(l)):
        cl = l.copy() 
        cl.pop(i) 
        ret.append(cl)
    return ret  

if __name__ == '__main__':
    # part1 
    il = get_input_list()
    safe_cnt = 0
    for l in il:
        if is_safe(l): safe_cnt +=1 
    print(safe_cnt)

    # part2
    generous_safe_cnt = 0 
    for l in il:
        for gl in generous_lists(l): 
            if is_safe(gl):
                generous_safe_cnt += 1
                break 
    print(generous_safe_cnt)