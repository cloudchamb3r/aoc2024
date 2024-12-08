from itertools import combinations
import numpy as np 

SOLVE = True

def get_inputs():
    if SOLVE:
        with open('input8.txt', 'r') as f: 
            return [l.strip() for l in f.readlines()]
    return [
        '............',
        '........0...',
        '.....0......',
        '.......0....',
        '....0.......',
        '......A.....',
        '............',
        '............',
        '........A...',
        '.........A..',
        '............',
        '............',
    ]

if __name__ == '__main__':
    maps = [list(l) for l in get_inputs()] 
    aposes = {}
    anties = {}

    n = len(maps) 
    m = len(maps[0])

    for i in range(n):
        for j in range(m): 
            if maps[i][j] != '.': 
                antenna = maps[i][j]
                if antenna not in aposes: 
                    aposes[antenna] = [] 
                aposes[antenna].append((i, j))
                if antenna not in anties:
                    anties[antenna] = set()

    for a in aposes:
        poses = np.array(aposes[a])
        combs = list(combinations(poses, 2))
        for c in combs:
            d = c[1] - c[0]
           
            ay, ax = c[1] + d 
            if (0 <= ay < n) and (0 <= ax < m):
                anties[a].add((ay, ax))

            by, bx = c[0] - d 
            if (0 <= by < n) and (0 <= bx < m):
                anties[a].add((by, bx))

    acc = set() 
    for a in anties:
        acc = acc.union(anties[a])
    print(len(acc))

    # part2 
    anties.clear()
    for a in aposes: 
        anties[a] = set()
        poses = np.array(aposes[a])
        combs = list(combinations(poses, 2))
        for c in combs: 
            d = c[1] - c[0]
            
            for i in range(n + m + 1): 
                y, x = c[0] + d * i 
                if (0 <= y < n) and (0 <= x  < m): 
                    anties[a].add((y, x))
                else: break 

            for i in range(n + m + 1): 
                y, x = c[0] - d * i 
                if (0 <= y < n) and (0 <= x  < m): 
                    anties[a].add((y, x))
                else: break 
    acc = set() 
    for a in anties: 
        acc = acc.union(anties[a]) 
    print(len(acc))