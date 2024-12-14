import re 
from PIL import Image, ImageColor

SOLVE = True 

def get_inputs():
    if SOLVE:
        with open('input14.txt', 'r') as f: 
            pattern = r'(-*\d+)' 
            return [[int(elem) for elem in re.findall(pattern, l)] for l in f.readlines()]
    return [
        [0,4,3,-3],
        [6,3,-1,-3],
        [10,3,-1,2],
        [2,0,2,-1],
        [0,0,1,3],
        [3,0,-2,-2],
        [7,6,-1,-3],
        [3,0,-1,-2],
        [9,3,2,3],
        [7,3,-1,2],
        [2,4,2,-3],
        [9,5,-3,-3], 
    ]

def get_wh(): 
    if SOLVE:
        return [101, 103]
    return [11, 7]

def get_quadrants(grid): 
    half_w = len(grid[0]) // 2
    half_h = len(grid) // 2

    q1 = [l[:half_w] for l in grid[0:half_h]]
    q2 = [l[half_w+1:] for l in grid[0:half_h]]
    q3 = [l[:half_w] for l in grid[half_h+1:]]
    q4 = [l[half_w+1:] for l in grid[half_h+1:]]

    return q1, q2, q3, q4

def get_sum(grid): 
    acc = 0
    for l in grid: 
        for e in l:
            acc += e 
    return acc 


robots = get_inputs() 
w, h = get_wh()

def after(robot, cnt): 
    px, py, vx, vy = robot 
    px += cnt * vx 
    py += cnt * vy 
    return [px % w, py % h]

def grid_after(k):
    robots_after_k = [after(robot, k) for robot in robots]
    grid = [[0 for _ in range(w)] for _ in range(h)]
    
    for r in robots_after_k: 
        x, y = r 
        grid[y][x] += 1
    return grid 

def draw_png(grid): 
    im = Image.new('1', (w + 1, h + 1))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0: 
                im.putpixel((j, i), ImageColor.getcolor('white', '1'))
    return im

if __name__ == '__main__':
    # part1
    grid = grid_after(100)
    s1,s2,s3,s4 = map(get_sum, get_quadrants(grid))
    print(s1 * s2 * s3 * s4)

    # part2
    imgs = []
    for i in range(89, 10000, 103):
        grid = grid_after(i)
        img = draw_png(grid)
        imgs.append(img)
    
    imgs[0].save('easter.gif', save_all=True, append_images=imgs[1:], duration=10, loop=1)