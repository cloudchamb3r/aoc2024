SOLVE = True 

def get_input_list():
    if SOLVE:
        with open('input4.txt', 'r') as f: 
            return list(map(lambda x: x.strip(), f.readlines()))
    return [
        'MMMSXXMASM',
        'MSAMXMSMSA',
        'AMXSXMAAMM',
        'MSAMASMSMX',
        'XMASAMXAMM',
        'XXAMMXXAMA',
        'SMSMSASXSS',
        'SAXAMASAAA',
        'MAMMMXMMMM',
        'MXMXAXMASX',
    ]

if __name__ == '__main__':
    # part1
    l = get_input_list() 
    n, m = (len(l), len(l[0]))

    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [-1, 0, 1, 1, -1, -1, 0, 1] 

    def go(i: int, j: int, d: int, step: int): 
        if step == 4: return 1 
        y = i + dy[d] * step 
        x = j + dx[d] * step 
        if not 0 <= y < n: return 0 
        if not 0 <= x < m: return 0 
        if l[y][x] != 'XMAS'[step]: return 0
        return go(i, j, d, step + 1)

    ans = 0 
    for i in range(n):
        for j in range(m):
            for d in range(8):
                ans += go(i, j, d, 0)
    print(ans)

    # part2
    ans = 0 
    for i in range(1, n-1):
        for j in range(1, m-1): 
            if l[i][j] != 'A': continue
            diag1 = (l[i-1][j-1] == 'M' and l[i+1][j+1] == 'S') or \
                    (l[i-1][j-1] == 'S' and l[i+1][j+1] == 'M')
            diag2 = (l[i-1][j+1] == 'M' and l[i+1][j-1] == 'S') or \
                    (l[i-1][j+1] == 'S' and l[i+1][j-1] == 'M')
            if diag1 and diag2: ans += 1 
    print(ans) 