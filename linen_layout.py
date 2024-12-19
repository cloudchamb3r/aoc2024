import sys 
from collections import defaultdict 
sys.setrecursionlimit(999999999)

SOLVE = True

def get_inputs(): 
    if SOLVE: 
        with open('input19.txt', 'r') as f: 
            a, b = f.read().split('\n\n')
            a = a.split(', ')
            b = b.split('\n')
            return a, b 
    a = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
    b = [
        'brwrr',
        'bggr',
        'gbbr',
        'rrbgbr',
        'ubwu',
        'bwurrg',
        'brgr',
        'bbrgwb',
    ]
    return a, b 

if __name__ == '__main__':
    a, b = get_inputs() 


    # part1
    __compose = defaultdict(lambda: None)
    def is_composable(c: str): 
        if c == '': return True
        if __compose[c] != None: 
            return __compose[c] 
        
        if c in a: 
            __compose[c] = True
            return True 
        result = False
        for i in range(1, len(c)): 
            if c[:i] in a: 
                result |= is_composable(c[i:]) 
        __compose[c] = result
        return result 
    
    acc = 0 
    for c in b: 
        if is_composable(c):   
            acc += 1 
    print(acc)


    # part2
    __compose_cnt = defaultdict(lambda: None) 
    def get_composable_count(c: str): 
        if c == '': return 1 
        if c in __compose_cnt: return __compose_cnt[c] 
        result = 0 
        for x in a: 
            if c.startswith(x):
                result += get_composable_count(c[len(x):])
        __compose_cnt[c] = result 
        return result 
    
    acc = 0
    for c in b:
        print(f'working on {c}: {get_composable_count(c)}')
        acc += get_composable_count(c)

    print(acc)