SOLVE = True

def get_input(): 
    if SOLVE:
        with open('input10.txt', 'r') as f:
            return [
                list(map(int, list(l.strip())))
                for l in f.readlines()
            ]
    return [
        [8,9,0,1,0,1,2,3],
        [7,8,1,2,1,8,7,4],
        [8,7,4,3,0,9,6,5],
        [9,6,5,4,9,8,7,4],
        [4,5,6,7,8,9,0,3],
        [3,2,0,1,9,0,1,2],
        [0,1,3,2,9,8,0,1],
        [1,0,4,5,6,7,3,2],
    ]

if __name__ == '__main__':
    maps = get_input()
    n, m = len(maps), len(maps[0])
    trailheads = [] 
    
    # get trailheads
    for i in range(n):
        for j in range(m): 
            if maps[i][j] == 0: 
                trailheads.append((i, j))

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0] 
    ans = 0

    for y, x in trailheads: 
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[y][x] = True
        q = [(y, x)]
        while len(q): 
            cy, cx = q.pop(0)
            cur = maps[cy][cx] 
            if cur == 9:
                ans += 1 
                continue
            for d in range(4): 
                ny = cy + dy[d]
                nx = cx + dx[d] 
                if not (0 <= ny < n) or not (0 <= nx < m):
                    continue
                if visited[ny][nx] or maps[ny][nx] != cur + 1: 
                    continue 
                visited[ny][nx] = True 
                q.append((ny, nx)) 
    print(ans)

    # part2
    trailheads = [] 
    
    # get trailheads
    for i in range(n):
        for j in range(m): 
            if maps[i][j] == 0: 
                trailheads.append((i, j))

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0] 
    ans = 0

    for y, x in trailheads: 
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[y][x] = True
        q = [(y, x)]
        while len(q): 
            cy, cx = q.pop(0)
            cur = maps[cy][cx] 
            if cur == 9:
                ans += 1 
                continue
            for d in range(4): 
                ny = cy + dy[d]
                nx = cx + dx[d] 
                if not (0 <= ny < n) or not (0 <= nx < m):
                    continue
                if maps[ny][nx] != cur + 1: 
                    continue 
                visited[ny][nx] = True 
                q.append((ny, nx)) 
    print(ans)

