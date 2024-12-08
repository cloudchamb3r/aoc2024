from itertools import product

SOLVE = True

def get_inputs():
    if SOLVE:
        with open('input7.txt', 'r') as f: 
            return [
                list(map(int, l.replace(':', ' ').split()))
                for l in f.readlines()
            ]
    return [
        [190, 10, 19],
        [3267, 81, 40, 27],
        [83, 17, 5],
        [156, 15, 6],
        [7290, 6, 8, 6, 15],
        [161011, 16, 10, 13],
        [192, 17, 8, 14],
        [21037, 9, 7, 18, 13],
        [292, 11, 6, 16, 20],
    ]

if __name__ == '__main__':
    l = get_inputs()

    # part1
    ans = 0 
    for x in get_inputs():
        res = x[0]
        nums = x[1:]
        opss = list(product(['+', '*'], repeat=len(nums) - 1))
        
        for ops in opss: 
            i = 0 
            cur = nums[0]
            for op in ops: 
                if op == '+': cur += nums[i + 1]
                if op == '*': cur *= nums[i + 1]
                i+=1
            if cur == res:
                ans += res 
                break
    print(ans)

    # part2
    ans = 0 
    for x in get_inputs():
        res = x[0]
        nums = x[1:]
        opss = list(product(['+', '*', '||'], repeat=len(nums) - 1))
        
        for ops in opss: 
            i = 0 
            cur = nums[0]
            for op in ops: 
                if op == '+': cur += nums[i + 1]
                if op == '*': cur *= nums[i + 1]
                if op == '||': cur = int(f'{cur}{nums[i+1]}')
                i+=1
            if cur == res:
                ans += res 
                break
    print(ans)