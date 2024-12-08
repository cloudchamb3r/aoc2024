import numpy as np 

SOLVE = True

def get_input_list():
    if SOLVE:
        with open('input1.txt', 'r') as f: 
            return [
                list(map(int, s.split()))
                for s in f.readlines()
            ]
    else:
        return [
            [3, 4], 
            [4, 3], 
            [2, 5], 
            [1, 3], 
            [3, 9], 
            [3, 3],
        ]

if __name__ == '__main__':
    # get as np array
    il = np.array(get_input_list() )
    # transpose
    til = np.transpose(il)

    # make sort
    lhs = sorted(til[0])
    rhs = sorted(til[1])
    assert(len(lhs) == len(rhs))

    # get distance
    acc = 0 
    for i in range(len(lhs)):
        acc += abs(lhs[i] - rhs[i])
    print(acc)