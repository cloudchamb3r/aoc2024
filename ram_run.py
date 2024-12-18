SOLVE = True 

def get_input():
    if SOLVE: 
        with open('input18.txt', 'r') as f: 
            return [list(map(int, l.split(','))) for l in f.readlines()]
    return [
        [5,4],
        [4,2],
        [4,5],
        [3,0],
        [2,1],
        [6,3],
        [2,4],
        [1,5],
        [0,6],
        [3,3],
        [2,6],
        [5,1],
        [1,2],
        [5,5],
        [2,5],
        [6,5],
        [1,4],
        [0,4],
        [6,4],
        [1,1],
        [6,1],
        [1,0],
        [0,5],
        [1,6],
        [2,0],
    ]

def get_wh(): 
    if SOLVE:
        return 71, 71
    return 7, 7 

def get_memory_after():
    if SOLVE: return 1024 
    return 12

PSEUDO_MAX = 0xfffffffffff

if __name__ == '__main__':
    w, h = get_wh() 
    memory = [[0 for _ in range(w)] for _ in range(h)]
    obs = get_input() 
    memory_after = get_memory_after()
    for x, y in obs[:memory_after]:
        memory[y][x] = 1 

    def bfs(): 
        valid = lambda y, x: 0<= y < h and 0 <= x < w 
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]
        visited = [[PSEUDO_MAX for _ in range(w)] for _ in range(h)]
        q = [(0, 0)]
        visited[0][0] = 0
        while len(q): 
            y, x = q.pop(0)
            for d in range(4): 
                ny = y + dy[d]
                nx = x + dx[d] 
                if not valid(ny, nx): continue 
                if memory[ny][nx] == 1: continue 
                if visited[ny][nx] <= visited[y][x] + 1: continue 
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1 
        return visited[h-1][w-1]
    
    # part1
    ans = bfs()
    print('min count:', ans)

    # part2 
    day = memory_after 
    while day < len(obs): 
        x, y = obs[day]
        memory[y][x] = 1 
        ans = bfs()
        if ans == PSEUDO_MAX: 
            print(f"cannot go on {x},{y}")
            break
        day+=1