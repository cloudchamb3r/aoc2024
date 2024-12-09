
SOLVE = True

def get_inputs() -> list[int]: 
    if SOLVE: 
        with open('input9.txt', 'r') as f: 
            return list(map(int, list(f.read())))
    return list(map(int, list('2333133121414131402')))

def create_block_map(l: list[int]) -> list[int]:
    ret = [] 
    free = False 
    bid = 0
    for e in l: 
        if free: ret.extend([-1] * e) 
        else: 
            ret.extend([bid] * e)
            bid+=1 
        free = not free
    return ret 

def rearrange_block_map(bm: list[int]) -> list[int]: 
    sp, ep = 0, len(bm)-1
    while sp < ep: 
        if bm[sp] != -1:
            sp+=1 
            continue
        while sp < ep and bm[ep] == -1: 
            ep-=1
        bm[sp], bm[ep] = bm[ep], bm[sp]
    return bm

def rearrange_block_map2(bm: list[int]) -> list[int]:
    ep, eplen = len(bm) - 1, 0

    while ep >= 0:
        # get ep, eplen
        eplen = 0 
        while bm[ep] == -1: ep-=1
        while bm[ep-eplen] == bm[ep]: eplen+=1 

        # get available free spaces
        sp, splen = 0, 0
        found = False 
        while sp <= ep - eplen: 
            # get sp start pos 
            splen = 0 
            while bm[sp]!=-1 and sp<=ep-eplen: sp+=1 

            while bm[sp+splen]==-1: splen+=1 
            if splen >= eplen: 
                found = True 
                break 
            else: 
                sp += splen
        if not found: 
            ep -= eplen
        else: 
            # swap 
            bm[sp:sp+eplen], bm[ep-eplen+1:ep+1] = bm[ep-eplen+1:ep+1], bm[sp:sp+eplen]
            pass 
    return bm

def calc_checksum(bm: list[int]) -> int: 
    acc = 0 
    for i, e in enumerate(bm):
        if e == -1: continue 
        acc += i * e
    return acc 

if __name__ == '__main__':
    # part1
    ip = get_inputs() 
    bm = create_block_map(ip)
    bm = rearrange_block_map(bm)
    print(calc_checksum(bm))

    # part2 
    bm = create_block_map(ip)
    bm = rearrange_block_map2(bm)
    print(calc_checksum(bm))