import re 

SOLVE = True 

def get_input():
    if SOLVE:
        with open('input3.txt', 'r') as f: 
            return f.read()
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


if __name__ == '__main__':
    # part1
    mul_re = r'mul\((\d+),(\d+)\)'
    tps = re.findall(mul_re, get_input())
    ans = 0 
    for tp in tps: 
        l, r = map(int, tp)
        ans += l * r
    print(ans)

    # part2
    pt2_mul_re = r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))"
    tps = re.findall(pt2_mul_re, get_input())
    
    do = True 
    ans = 0 

    for tp in tps: 
        l, r, n, y = tp 
        if y != '': do = True
        if n != '': do = False
        if do and l != '' and r != '':
            ans += int(l) * int(r)
    print(ans)