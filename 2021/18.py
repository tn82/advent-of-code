from collections import defaultdict
from math import floor, ceil

def add_row(r1, r2):
    return "[" + r1 + "," + r2 + "]"

def get_int(s, i):
    return int(s[i]), s[:i] + s[i+1:]

def remove(s, i):
    s = s[:i] + s[i+1:]
    #print(s)
    return s

def find_left_reg(s, end):
    regs = '0123456789'
    i = -1
    for r in regs:
        idx = s.rfind(r, 0, end)
        if idx > i:
            i = idx
    return i

def find_right_reg(s, start):
    regs = '0123456789'
    i = 10000
    for r in regs:
        idx = s.find(r, start)
        if idx != -1 and idx < i:
            i = idx
    return -1 if i == 10000 else i

splits =  []
for i in range(10, 100):
    splits.append(str(i))

def find_split(s):
    i = 10000
    split = 0
    for r in splits:
        idx = s.find(r)
        if idx != -1 and idx < i:
            i = idx
            split = r
    return (-1 if i == 10000 else i), int(split)

def add_int(s, dest, src):
    #if dest == -1:
    #    s = s[:src] + str(0) + s[src + 1:]
    #else:
    if dest != -1:
        src_int = s[src]
        if s[src+1].isdigit():
            src_int += s[src+1]
        dest_int = s[dest]
        if s[dest+1].isdigit():
            dest_int += s[dest+1]
        dest_int = int(src_int) + int(dest_int)
    if dest > src:
        if dest != -1:
            offset = 1
            if s[dest+1].isdigit():
                offset = 2
            s = s[:dest] + str(dest_int) + s[dest + offset:]
        offset = 1
        if s[src+1].isdigit():
            offset = 2
        s = s[:src] + str(0) + s[src + offset:]
    else:
        offset = 1
        if s[src+1].isdigit():
            offset = 2
        s = s[:src] + str(0) + s[src + offset:]
        if dest != -1:
            offset = 1
            if s[dest+1].isdigit():
                offset = 2
            s = s[:dest] + str(dest_int) + s[dest + offset:]
    #print(s)
    return s

def exploder(s, left, right):
    s = remove(s, right)
    s = remove(s, left)
    right_reg = find_right_reg(s, right)
    offset = 2
    if s[right-3].isdigit():
        offset = 3
    s = add_int(s, right_reg, right-offset)
    left_reg = find_left_reg(s, left)
    if left_reg != -1 and s[left_reg-1].isdigit():
        left_reg -= 1
    s = add_int(s, left_reg, left)
    if right_reg != -1 or left_reg != -1:
        right_reg = find_right_reg(s, left_reg + 2)
        if s[right_reg+1].isdigit():
            s = remove(s, right_reg+1) # second in number xx
        s = remove(s, right_reg) # 
        s = remove(s, right_reg) # ","
    return s

def nested(string):
    stack = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(i)
        elif c == ']' and stack:
            start = stack.pop()
            yield (len(stack), i, string[start + 1: i])

def explode_old(s): # Not good
    left4 = s.rfind("[[[[")
    right4 = s.find("]]]]")
    if left4 != -1 and left4 < right4:
        right4 = -1

    if left4 != -1:
        left = left4 + 3
        right = s.find("]", left)
    elif right4 != -1:
        right = right4
        left = s.rfind("[", 0, right)
    did_explode = left4 != -1 or right4 != -1
    if did_explode:
        s = exploder(s, left, right)
    return did_explode, s

def explode(s):
    #print(s)
    level4 = [v for v in nested(s) if v[0] == 4]
    if level4:
        right = level4[0][1]
        left = right - 4
        if s[left].isdigit():
            left -= 1
        if s[left].isdigit():
            left -= 1
        s = exploder(s, left, right)
        return True, s
    return False, s

def split(s):
    idx, val = find_split(s)
    if idx != -1:
        s = remove(s, idx)
        s = remove(s, idx)
        le = floor(val / 2.0)
        re = ceil(val / 2.0)
        s = s[:idx] + "[" + str(le) + "," + str(re) + "]" + s[idx:]
        #print(s)
        return True, s
    return False, s

def day_18():
    file = open('18.txt', 'r')
    input = []
    for line in file:
        row = line.strip()
        input.append(row)
    s = '[[[[[9,8],1],2],3],4]' # ok
    s = '[7,[6,[5,[4,[3,2]]]]]' # ok
    s = '[[6,[5,[4,[3,2]]]],1]' # ok
    s = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
    s1 = '[[[[4,3],4],4],[7,[[8,4],9]]]'
    s2 = '[1,1]'
    s = add_row(s1, s2)
    s = input[0]
    i = 1
    for i in range(1, len(input)):
        s = add_row(s, input[i])
        while True:
            ex = True
            while ex:
                ex, s = explode(s)
            spl, s = split(s)
            if not spl and not ex:
                break
    for l in range(3,-1, -1):
        for b in [v for v in nested(s) if v[0] == l]:
            v1 = b[2][0]
            i = 1
            while True:
                if b[2][i].isdigit():
                    v1 += b[2][i]
                    i += 1
                else:
                    break
            v2 = ""
            i += 1
            while True:
                if i < len(b[2]) and b[2][i].isdigit():
                    v2 += b[2][i]
                    i += 1
                else:
                    break
            val = int(v1)*3 + int(v2)*2
            s = s.replace("["+b[2]+"]", str(val), 1)
    
    print(s)
    #for c in row:
    #    row1find
day_18()



def day_18_2():
    row1 = '[[[[0,7],4],[7,[[8,4],[6,3]]]],[1,1]]'
    #row1 = '[[[[4,9],[1,2]],[[0,0],[1,6]]],[[5,6],[[8,4],[5,7]]]]'
    s = set()
    l = [v for v in nested(row1) if v[0] == 4]
    print(l)
#day_18_2()