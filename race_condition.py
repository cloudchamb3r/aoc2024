from collections import defaultdict 
SOLVE = True

def get_inputs():
    if SOLVE:
        with open('input20.txt', 'r') as f: 
            return [list(l.strip()) for l in f.readlines()]
    return [
        list("###############"),
        list("#...#...#.....#"),
        list("#.#.#.#.#.###.#"),
        list("#S#...#.#.#...#"),
        list("#######.#.#.###"),
        list("#######.#.#...#"),
        list("#######.#.###.#"),
        list("###..E#...#...#"),
        list("###.#######.###"),
        list("#...###...#...#"),
        list("#.#####.#.###.#"),
        list("#.#...#.#.#...#"),
        list("#.#.#.#.#.#.###"),
        list("#...#...#...###"),
        list("###############"),
    ]

if __name__ == '__main__': 
    grid = get_inputs() 
    n, m = len(grid), len(grid[0])

    print(f'n: {n}, m: {m}')
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                sy, sx = i, j 
            elif grid[i][j] == 'E':
                ey, ex = i, j 

    PSEUDO_MAX = 0xffffffffffffff
    valid = lambda y, x : 0<= y < n and 0 <= x < m 
    dy = [0, 1, 0, -1] 
    dx = [1, 0, -1, 0]

    def bfs(): 
        time = [[PSEUDO_MAX for _ in range(m)] for _ in range(n)] 
        time[sy][sx] = 0 
        q = [(sy, sx)]
        while len(q): 
            y, x = q.pop(0)
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d] 
                if not valid(ny, nx): continue 
                if grid[ny][nx] == '#': continue 
                if time[ny][nx] <= time[y][x] + 1: continue 
                q.append((ny, nx)) 
                time[ny][nx] = time[y][x] + 1 
        return time

    time = bfs()
    
    def cheat(l: int): 
        result = defaultdict(lambda: 0)

        for i in range(n):
            for j in range(m):
                if time[i][j] == PSEUDO_MAX: continue 
                for dy in range(-l, l + 1): 
                    for dx in range(-l, l + 1):
                        movelen = abs(dx) + abs(dy)
                        if movelen > l: continue 
                        ny, nx = i + dx, j + dy 
                        if not valid(ny, nx): continue
                        if time[ny][nx] == PSEUDO_MAX: continue 
                        if time[ny][nx] - time[i][j] <= movelen: continue
                        save_time = time[ny][nx] - time[i][j] - movelen
                        result[save_time] += 1
        return result

    def cheat_count(cheat: defaultdict, save: int):
        acc = 0 
        for c in cheat:
            if c >= save: 
                acc += cheat[c] 
        return acc 

    # part1
    c2 = cheat(2)
    for key in sorted(c2.keys()): 
        print(f'- There are {c2[key]} that save {key} picoseconds.')
    print(cheat_count(c2, 100))

    # part2
    c20 = cheat(20)
    for key in sorted(c20.keys()): 
        if key >= 50: 
            print(f'- There are {c20[key]} that save {key} picoseconds.')

    print(cheat_count(c20, 100))