import copy
SOLVE = True

def get_input_list(): 
    if SOLVE: 
        with open('input6.txt', 'r') as f: 
            return [l.strip() for l in f.readlines()]
    return [
        '....#.....',
        '.........#',
        '..........',
        '..#.......',
        '.......#..',
        '..........',
        '.#..^.....',
        '........#.',
        '#.........',
        '......#...',
    ]

if __name__ == '__main__':
    l = get_input_list() 
    n, m = len(l), len(l[0])

    # reconstucturing maps    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    maps = [[0 for _ in range(m)] for _ in range(n)]
    y, x, d = -1, -1, 0

    for i in range(n):
        for j in range(m): 
            if l[i][j] == '#': maps[i][j] = 1
            if l[i][j] == '^': y, x = i, j 

    sy, sx = y, x # this will be used in part2 

    ans = 0 
    try: 
        while True:
            maps[y][x] = 2 
            ny, nx = y + dy[d], x + dx[d] 
            if maps[ny][nx] == 1: 
                ny, nx = y, x 
                d = (d + 1) % 4 
            y, x = ny, nx  
    except IndexError:
        for x in maps: ans += x.count(2)
    print(ans)

    # part2 

    ans = 0 
    for i in range(n):
        for j in range(m): 
            if maps[i][j] == 1: continue 
            if i == sy and j == sx: continue

            new_maps = copy.deepcopy(maps)
            new_maps[i][j] = 1
            
            y, x, d = sy, sx, 0
            visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
            while True:
                if visited[y][x][d]:
                    ans += 1
                    break
                visited[y][x][d] = True
                ny, nx = y + dy[d], x + dx[d]
                if not (0 <= ny < n) or not (0 <= nx < m): break 
                if new_maps[ny][nx] == 1:
                    ny, nx = y, x
                    d = (d + 1) % 4 
                y, x = ny, nx    

    print(ans)