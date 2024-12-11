from collections import defaultdict 
SOLVE = True

def get_inputs():
    if SOLVE:
        with open('input11.txt', 'r') as f: 
            return list(map(int, f.readline().split()))
    return [125, 17]

def blink(l: list[int]) -> list[int]: 
    ret = [] 
    for i in l: 
        s = str(i)
        sn = len(s)
        if i == 0: 
            ret.append(1) 
        elif sn % 2 == 0: 
            first = int(s[:sn//2])
            second = int(s[sn//2:])
            ret.append(first)
            ret.append(second)
        else: 
            ret.append(i * 2024)
    return ret 


__blink_count = defaultdict(lambda: defaultdict(int))
def blink_count(n: int, k: int): 
    
    if __blink_count[n][k] != 0:
        return __blink_count[n][k]
    
    if k == 0:
        __blink_count[n][k] = 1 
        return __blink_count[n][k]
    
    s = str(n)
    sn = len(s)
    if n == 0: 
        __blink_count[n][k] = blink_count(1, k - 1)
    elif sn % 2 == 0: 
        first = int(s[:sn//2])
        second = int(s[sn//2:])
        __blink_count[n][k] = blink_count(first, k -1) + blink_count(second, k - 1)
    else: 
        __blink_count[n][k] = blink_count(n * 2024, k - 1)
    return __blink_count[n][k]

if __name__ == '__main__':
    ip = get_inputs() 
    for i in range(25): 
        ip = blink(ip)
    print(len(ip))

    # part2
    ip = get_inputs()
    cnt = 0 
    for i in ip: 
        cnt += blink_count(i, 75)
    print(cnt)
