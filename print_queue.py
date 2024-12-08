SOLVE = True

def get_inputs():
    if SOLVE:
        with open('input5.txt', 'r') as f: 
            fs, ss = f.read().split('\n\n')
            ordering_rule = [list(map(int, entry.split('|'))) for entry in fs.split()]
            update = [list(map(int, entry.split(','))) for entry in ss.split()]
        return ordering_rule, update
    
    ordering_rule = [
        [47, 53],
        [97, 13],
        [97, 61],
        [97, 47],
        [75, 29],
        [61, 13],
        [75, 53],
        [29, 13],
        [97, 29],
        [53, 29],
        [61, 53],
        [97, 53],
        [61, 29],
        [47, 13],
        [75, 47],
        [97, 75],
        [47, 61],
        [75, 61],
        [47, 29],
        [75, 13],
        [53, 13],
    ]
    update = [
        [75,47,61,53,29],
        [97,61,53,29,13],
        [75,29,13],
        [75,97,47,61,53],
        [61,13,29],
        [97,13,75,29,47],
    ]
    return ordering_rule, update 

if __name__ == '__main__':
    # part1
    ordering_rule, update = get_inputs()
    
    def is_right_order(u: list[int]):
        lu = len(u)
        for i in range(lu): 
            for j in range(i + 1, lu):
                if [u[j], u[i]] in ordering_rule: 
                    return False
        return True
    
    ans = 0 
    for u in update:
        if is_right_order(u):
            ans += u[len(u) // 2]
    print(ans)
    
    # part2
    def correct_order(u: list[int]):
        lu = len(u)
        for i in range(lu): 
            for j in range(i + 1, lu): 
                if [u[j], u[i]] in ordering_rule:
                    u[j], u[i] = u[i], u[j]
        return u
    
    ans = 0 
    for u in update:
        if not is_right_order(u):
            co = correct_order(u)
            ans += co[len(co) // 2]
    print(ans)