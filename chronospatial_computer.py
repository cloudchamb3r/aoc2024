from enum import Enum
import sys 

sys.setrecursionlimit(10000000)
SOLVE = True

REG_A = 0 
REG_B = 1 
REG_C = 2 

class Opcode(Enum):
    ADV = 0 
    BXL = 1 
    BST = 2 
    JNZ = 3 
    BXC = 4 
    OUT = 5 
    BDV = 6
    CDV = 7

def get_inputs():
    if SOLVE:
        with open('input17.txt', 'r') as f: 
            register, program = f.read().split('\n\n')
            register = register.split('\n')
            register = [int(l.split(': ')[-1].strip()) for l in register]

            program = program.split(': ')[-1].split(',')
            program = [int(p) for p in program]
            return register, program
        
    # register = [729, 0, 0]
    # program = [0,1,5,4,3,0]
    register = [2024, 0, 0]
    program = [0,3,5,4,3,0]
    return register, program

def exec(register: list[int], program: list[int]):
    pc = 0 
    output: list[int] = []

    def combo(operand: int): 
        nonlocal register
        if operand == 4: 
            return register[REG_A]
        if operand == 5: 
            return register[REG_B]
        if operand == 6: 
            return register[REG_C]
        if operand == 7: 
            raise ValueError("7 is reserved value")
        return operand

    def read() -> tuple[int, int]:
        nonlocal pc
        if pc >= len(program): return -1, -1 
        opcode, operand = program[pc], program[pc + 1]
        pc += 2
        return Opcode(opcode), operand

    def run() -> tuple[bool, list[int] | None]:
        nonlocal register
        nonlocal output
        nonlocal pc 

        opcode, operand = read()
        match opcode:
            case Opcode.ADV: 
                register[REG_A] = register[REG_A] >> combo(operand)
            case Opcode.BXL: 
                register[REG_B] ^= operand
            case Opcode.BST: 
                register[REG_B] = combo(operand) % 8
            case Opcode.JNZ: 
                if register[REG_A] != 0: 
                    pc = operand
            case Opcode.BXC: 
                register[REG_B] ^= register[REG_C]
            case Opcode.OUT: 
                output.append(combo(operand) % 8)
            case Opcode.BDV: 
                register[REG_B] = register[REG_A] >> combo(operand)
            case Opcode.CDV: 
                register[REG_C] = register[REG_A] >> combo(operand)
            case _:
                return False, output
        return True, output
    return run

if __name__ == '__main__':
    r, p = get_inputs()
    print('r', r)
    print('p', p)
    # part1
    program = exec(r, p)
    while True:
        cnt, output = program()
        if not cnt: 
            print('part1: ', ','.join(map(str, output)))
            break

    
    # part2
    def digits_to_num(l): 
        acc = 0 
        inv_l = l[::-1]
        for i in range(len(l)): 
            acc += inv_l[i] * (8 ** i)
        return acc 

    def get_expected(): 
        return ''.join(map(str, p))
    
    def get_test(x):   
        r[0] = x
        program = exec(r, p)
        while True:
            cnt, output = program()
            if not cnt: 
                return ''.join(map(str, output))

    expected  = get_expected()
    digits = [0 for _ in range(len(expected))] 

    ans = 0xfffffffffffffffffff
    def dfs(pos): 
        global ans 
        global digits
        if pos == len(expected):
            if get_test(digits_to_num(digits)) == expected: 
                ans = min(ans, digits_to_num(digits))
            return 
        
        start = 0
        if pos == 0: start = 1 
        for i in range(start, 8):
            digits[pos] = i
            test = get_test(digits_to_num(digits))
            if test[-(pos + 1)] == expected[-(pos + 1)]: 
                dfs(pos + 1)
    dfs(0)
    print(f'answer: {ans}')