SOLVE = False 

def get_inputs(): 
    if SOLVE: 
        with open('input16.txt', 'r') as f: 
            return [l.strip() for l in f.readlines()]
    return [
        "###############",
        "#.......#....E#",
        "#.#.###.#.###.#",
        "#.....#.#...#.#",
        "#.###.#####.#.#",
        "#.#.#.......#.#",
        "#.#.#####.###.#",
        "#...........#.#",
        "###.#.#####.#.#",
        "#...#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.....#...#.#.#",
        "#.###.#.#.#.#.#",
        "#S..#.....#...#",
        "###############",
    ]

if __name__ == '__main__':
    grid = get_inputs() 
    n, m = len(grid), len(grid[0])
    scores = [[[10000 * n * m for _ in range(4)] for _ in range(m)] for _ in range(n)]

    sy, sx, sy, sx = -1, -1, -1, -1 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'E': 
                ey, ex = i, j
            elif grid[i][j] == 'S':
                sy, sx = i, j

    def valid(y, x): 
        return 0 <= y < n and 0 <= x < m and grid[y][x] != '#'
    
    # +1 if turn clockwise
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    scores[sy][sx][0] = 0 
    q = [(sy, sx, 0)]
    while len(q): 
        y, x, d = q.pop(0)
        if y == ey and x == ex: 
            continue
            
        # go straight 
        nd = d
        ny, nx = y + dy[nd], x + dx[nd]
        if valid(ny, nx) and scores[ny][nx][nd] > scores[y][x][d] + 1: 
            scores[ny][nx][nd] = scores[y][x][d] + 1 
            q.append((ny, nx, nd))
        # turn cw 
        nd = (d + 1) % 4
        ny, nx = y + dy[nd], x + dx[nd]
        if valid(ny, nx) and scores[ny][nx][nd] > scores[y][x][d] + 1001: 
            scores[ny][nx][nd] = scores[y][x][d] + 1001
            q.append((ny, nx, nd))
        # turn ccw
        nd = (d + 3) % 4 
        ny, nx = y + dy[nd], x + dx[nd]
        if valid(ny, nx) and scores[ny][nx][nd] > scores[y][x][d] + 1001: 
            scores[ny][nx][nd] = scores[y][x][d] + 1001 
            q.append((ny, nx, nd))

    print(min(scores[ey][ex]))

    def backtrack():
        new_grid = [[grid[i][j] for j in range(m)] for i in range(n)]
        q = [(ey, ex, -1)]
        while len(q): 
            def find_min_dirs(l, last_d):
                score = 0xffffff
                ds = []
                for d in range(4): 
                    current_score = l[d] 
                    if d == -1: pass
                    elif d == last_d: current_score += 1 
                    elif d != last_d: current_score += 1001

                    if current_score < score:
                        score = current_score
                        ds = [d]
                    elif current_score == score:
                        ds.append(d) 
                return ds
            
            y, x, d = q.pop(0)
            ds = find_min_dirs(scores[y][x], d)
            if len(ds) > 1: 
                print('multiple in ', y, x)
            new_grid[y][x] = 'O'
            if y == sy and x == sx: continue 
            for d in ds: 
                q.append((y - dy[d], x - dx[d], d)) 
        return new_grid
    
    bt = backtrack()
    acc = 0 
    for i in range(n):
        for j in range(m):
            if bt[i][j] == 'O':
                acc += 1
    for i in range(n):
        for j in range(m):
            print(bt[i][j], end='')
        print() 
    
    print(acc)
    # backtrack()