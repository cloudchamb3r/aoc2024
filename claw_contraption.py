import re 
import numpy as np 

SOLVE = True 

def get_inputs():
    if SOLVE:
        with open('input13.txt', 'r') as f: 
            d = f.read() 
            def string_to_tuple(s):
                r = r'X\+(\d+), Y\+(\d+)|X=(\d+), Y=(\d+)'
                mx, my, dx, dy = re.findall(r, s)[0]
                if mx and my:
                    return (int(mx), int(my))
                return (int(dx), int(dy))
            return [[string_to_tuple(s) for s in block.split('\n')] for block in d.split('\n\n')]
     
    return [
        [
            (94, 34), 
            (22, 67),
            (8400, 5400),
        ],
        [
            (26, 66),
            (67, 21),
            (12748, 12176),
        ],
        [
            (17, 86),
            (84, 37),
            (7870, 6450),
        ],
        [
            (69, 23), 
            (27, 71), 
            (18641, 10279),
        ],
    ]

MAX = 0xffffffffff
if __name__ == '__main__':
    ip = get_inputs()
    
    # part1 
    acc = 0
    for (ax, ay), (bx, by), (cx, cy) in ip:
        min_cost = MAX 
        for a in range(101):
            for b in range(101):
                if a * ax + b * bx == cx and \
                   a * ay + b * by == cy: 
                    min_cost = min(min_cost, 3 * a + b)
        if min_cost != MAX:
            acc += min_cost
    print(acc)

    # part 
    BASE = 10000000000000
    acc = 0
    for (ax, ay), (bx, by), (cx, cy) in ip:
        mat = np.matrix([
            [ax, bx], 
            [ay, by]
        ])
        inv_mat = np.linalg.inv(mat)
        xy = np.matrix([BASE + cx, BASE + cy]).transpose()
        ab = np.matmul(inv_mat, xy).transpose()
        a = round(ab[0, 0], 3)
        b = round(ab[0, 1], 3)
        a_is_integer = int(a) == a
        b_is_integer = int(b) == b 
        if a_is_integer and b_is_integer: 
            acc += int(3 * a + b)
    print(acc)