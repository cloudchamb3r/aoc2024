SOLVE = True

def get_inputs(): 
    if SOLVE: 
        with open('input12.txt', 'r') as f:
            return [ l.strip() for l in f.readlines()]
    return [
        'RRRRIICCFF',
        'RRRRIICCCF',
        'VVRRRCCFFF',
        'VVRCCCJFFF',
        'VVVVCJJCFE',
        'VVIVCCJJEE',
        'VVIIICJJEE',
        'MIIIIIJJEE',
        'MIIISIJEEE',
        'MMMISSJEEE',
    ]


if __name__ == '__main__': 
    grid = get_inputs() 
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    dy = [0, 0, 1, -1] 
    dx = [1, -1, 0, 0]

    def invalid(i, j): 
        return i < 0  or j < 0 or i >= n or j >= m 
    
    def around_not_eq_cnt(i, j) -> int:
        ret = 0
        for d in range(4): 
            y = i + dy[d]
            x = j + dx[d]
            if invalid(y, x) or grid[i][j] != grid[y][x]: 
                ret += 1
        return ret 

    # part1
    def go(i, j) ->tuple[int, int]:     
        q = [(i, j)]
        visited[i][j] = True 
        memo = [(i, j)] 
        while len(q):
            y, x = q.pop(0)
            for d in range(4):
                ny = y + dy[d] 
                nx = x + dx[d] 
                if invalid(ny, nx): continue
                if grid[y][x] != grid[ny][nx]: continue 
                if visited[ny][nx]: continue

                visited[ny][nx] = True 
                q.append((ny, nx))
                memo.append((ny, nx))
        area = len(memo)
        perimeter = 0 
        for y, x in memo: 
            perimeter += around_not_eq_cnt(y, x)
        return area, perimeter

    acc = 0 
    for i in range(n):
        for j in range(m):
            if not visited[i][j]: 
                a, p = go(i, j) 
                acc += a*p
    print(acc)

    
    # part2 

    def go2(i, j) ->tuple[int, int]:     
        q = [(i, j)]
        visited[i][j] = True 
        memo = [(i, j)] 
        while len(q):
            y, x = q.pop(0)
            for d in range(4):
                ny = y + dy[d] 
                nx = x + dx[d] 
                if invalid(ny, nx): continue
                if grid[y][x] != grid[ny][nx]: continue 
                if visited[ny][nx]: continue

                visited[ny][nx] = True 
                q.append((ny, nx))
                memo.append((ny, nx))
        area = len(memo)
        side = 0 
        top, left, right, bottom = [], [], [], [] 

        for y, x in memo: 
            # top 
            ty, tx = y - 1, x 
            if invalid(ty, tx) or grid[y][x] != grid[ty][tx]: 
                top.append((y, x))
            # left 
            ly, lx = y, x - 1 
            if invalid(ly, lx) or grid[y][x] != grid[ly][lx]:
                left.append((y, x))
            # right 
            ry, rx = y,  x + 1
            if invalid(ry, rx) or grid[y][x] != grid[ry][rx]:
                right.append((y, x))
            # bottom 
            by, bx = y + 1, x 
            if invalid(by, bx) or grid[y][x] != grid[by][bx]: 
                bottom.append((y, x))


        top.sort(key= lambda x: (x[0], x[1]))
        left.sort(key=lambda x: (x[1], x[0]))
        right.sort(key = lambda x: (x[1], x[0]))
        bottom.sort(key = lambda x: (x[0], x[1]))

        tc = 1
        ty, tx = top[0]
        for i in range(1, len(top)):
            y, x = top[i]
            if ty == y and x - tx == 1: 
                tx = x
            else: 
                tc += 1 
                ty = y 
                tx = x 

        # print(left)
        lc = 1 
        ly, lx = left[0]
        for i in range(1, len(left)): 
            y, x = left[i] 
            if lx == x and y - ly == 1: 
                ly = y
            else:
                lc += 1 
                ly = y 
                lx = x 
        # print(right)
        rc = 1 
        ry, rx = right[0]
        for i in range(1, len(right)): 
            y, x = right[i] 
            if rx == x and y - ry == 1: 
                ry = y
            else:
                rc += 1 
                ry = y 
                rx = x 

        # print(bottom)
        bc = 1 
        by, bx = bottom[0]  
        for i in range(1, len(bottom)):
            y, x = bottom[i]
            if by == y and x - bx == 1: 
                bx = x 
            else:
                bc += 1 
                by = y 
                bx = x 
        side = tc + bc + lc + rc
        return area, side
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    acc = 0 
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                a, s = go2(i, j)
                acc += a * s
    print(acc)