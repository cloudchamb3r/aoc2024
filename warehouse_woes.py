import os 
from copy import deepcopy

SOLVE = True
WALL = 2 
BOX = 1
BOX_OPEN = 3 
BOX_CLOSE = 5
EMPTY = 0

def get_inputs(): 
    if SOLVE: 
        with open('input15.txt', 'r') as f: 
            a, b = f.read().split('\n\n')
            return a.split('\n'), ''.join(b.split('\n'))
    maps = [
        "##########",
        "#..O..O.O#",
        "#......O.#",
        "#.OO..O.O#",
        "#..O@..O.#",
        "#O#..O...#",
        "#O..O..O.#",
        "#.OO.O.OO#",
        "#....O...#",
        "##########",
    ]
    moves = [
        "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^",
        "vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v",
        "><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<",
        "<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^",
        "^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><",
        "^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^",
        ">^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^",
        "<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>",
        "^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>",
        "v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^",
    ]
    return maps, ''.join(moves)

sy, sx = -1, -1 
if __name__ == '__main__':
    char_maps, moves = get_inputs() 

    n = len(char_maps)
    m = len(char_maps[0])
    
    maps = [[0 for _ in range(m)] for _ in range(n)]

    # create maps from char maps 
    for i in range(n):
        for j in range(m):
            if char_maps[i][j] == '#': 
                maps[i][j] = WALL
            elif char_maps[i][j] == 'O':
                maps[i][j] = BOX
            elif char_maps[i][j] == '@':
                sy, sx = i, j 

    def is_valid_pos(y, x): 
        return (0 <= y < n) and (0 <= x < m)

    def add_force(y, x, dy, dx):
        if not is_valid_pos(y, x): return
        if maps[y][x] in [EMPTY, WALL]: return 
        
        ny, nx = y + dy, x + dx 
        
        if not is_valid_pos(ny, nx): return 
        if maps[ny][nx] == WALL: return 
        if maps[ny][nx] == BOX: add_force(ny, nx, dy, dx)
        maps[y][x], maps[ny][nx] = maps[ny][nx], maps[y][x]

    def can_move(y, x) -> bool: 
        if not is_valid_pos(y, x): return False
        return maps[y][x] == EMPTY
    
    def move(d): 
        if d == '^': 
            add_force(sy - 1, sx, -1, 0)
            if can_move(sy - 1, sx): 
                return sy - 1, sx 
        elif d == 'v':
            add_force(sy + 1, sx, 1, 0)
            if can_move(sy + 1, sx):
                return sy + 1, sx 
        elif d == '<':
            add_force(sy, sx - 1, 0, -1)
            if can_move(sy, sx - 1): 
                return sy, sx - 1
        elif d == '>':
            add_force(sy, sx + 1, 0, 1)
            if can_move(sy, sx + 1): 
                return sy, sx + 1
        return sy, sx
    
    def print_maps(): 
        if SOLVE: return 
        for i in range(n):
            for j in range(m):
                if i == sy and j == sx: print('@', end='')
                elif maps[i][j] == WALL: print('#', end='')
                elif maps[i][j] == BOX: print('O', end='')
                elif maps[i][j] == BOX_OPEN: print('[', end='')
                elif maps[i][j] == BOX_CLOSE: print(']', end='')
                else: print('.', end='')
            print()

    for d in moves: 
        sy, sx = move(d)

    def calc_gps():
        acc = 0 
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] in [BOX, BOX_OPEN]:
                    acc += 100 * i + j 
        return acc 
    
    print('part1', calc_gps())

    # part2
    maps = [] 

    for l in char_maps:
        acc = [] 
        for e in l:
            if e == '#': 
                acc.append(WALL)
                acc.append(WALL)
            elif e == 'O':
                acc.append(BOX_OPEN)
                acc.append(BOX_CLOSE)
            elif e == '@':
                sx = len(acc)
                sy = len(maps)
                acc.append(EMPTY)
                acc.append(EMPTY)
            else:
                acc.append(EMPTY)
                acc.append(EMPTY) 
        maps.append(acc)
    n, m = len(maps), len(maps[0])

    def add_force2(y, x, dy, dx) -> bool:
        if not is_valid_pos(y, x): return False
        if maps[y][x] in [EMPTY, WALL]: return maps[y][x] == EMPTY
        
        if dy == 0: 
            ny, nx = y + dy, x + dx 
            if add_force2(ny, nx, dy, dx) and can_move(ny, nx): 
                maps[y][x], maps[ny][nx] = maps[ny][nx], maps[y][x]
                return True
        else: # if dy != 0  
            ny, nx = y + dy , x + dx 
            ny2, nx2 = [(ny, nx + 1) if maps[y][x] == BOX_OPEN else (ny, nx - 1)][0]
            y2, x2 = [(y, x + 1) if maps[y][x] == BOX_OPEN else (y, x - 1)][0]

            if add_force2(ny, nx, dy, dx) and add_force2(ny2, nx2, dy, dx) and can_move(ny, nx) and can_move(ny2, nx2): 
                maps[y][x], maps[ny][nx] = maps[ny][nx], maps[y][x]
                maps[y2][x2], maps[ny2][nx2] = maps[ny2][nx2], maps[y2][x2]
                return True
        return False

    def move2(d):
        global maps
        snapshot = deepcopy(maps)
        if d == '^': 
            if not add_force2(sy - 1, sx, -1, 0):
                maps = snapshot
            if can_move(sy - 1, sx): 
                return sy - 1, sx 
        elif d == 'v':
            if not add_force2(sy + 1, sx, 1, 0):
                maps = snapshot
            if can_move(sy + 1, sx):
                return sy + 1, sx 
        elif d == '<':
            if not add_force2(sy, sx - 1, 0, -1):
                maps = snapshot
            if can_move(sy, sx - 1): 
                return sy, sx - 1
        elif d == '>':
            if not add_force2(sy, sx + 1, 0, 1):
                maps = snapshot
            if can_move(sy, sx + 1): 
                return sy, sx + 1
        return sy, sx


    for d in moves: 
        sy, sx = move2(d)
    print('part2', calc_gps()) 
