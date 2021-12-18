from collections import defaultdict

def add_row(r1, r2):
    return r1 + "," + r2

def get_int(s, i):
    return int(s[i]), s[:i] + s[i+1:]

def remove(s, i):
    print(s)
    s = s[:i] + s[i+1:]
    print(s)
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

def add_int(s, dest, src):
    print(s)
    if dest == -1:
        s = s[:src] + str(0) + s[src + 1:]
    else:
        dest_int = int(s[src]) + int(s[dest])
        s = s[:dest] + str(dest_int) + s[dest + 1:]
    print(s)
    return s

def exploder(s, left, right):
    s = remove(s, right)
    s = remove(s, left)
    right_reg = find_right_reg(s, right)
    s = add_int(s, right_reg, right-2)
    if right_reg != -1:
        s = remove(s, right_reg-1) # ","
        s = remove(s, right_reg-2) # 
    
    left_reg = find_left_reg(s, left)
    s = add_int(s, left_reg, left)
    if left_reg != -1:
        s = remove(s, left_reg+1) # ","
        s = remove(s, left_reg+2) #
    return s

def explode(s):
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
        
    s = exploder(s, left, right)
    return s

def day_18():
    file = open('18.txt', 'r')

    input = []
    first = True
    for line in file:
            row = line.strip()
            input.append(row)
    regs = '0123456789'
    s = '[[[[[9,8],1],2],3],4]'
    s = '[7,[6,[5,[4,[3,2]]]]]'
    s = '[[6,[5,[4,[3,2]]]],1]'
    s = explode(s)

    print(s)
    #for c in row:
    #    row1find
day_18()

def parenthetic_contents(string):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(i)
        elif c == ']' and stack:
            start = stack.pop()
            yield (len(stack), string[start + 1: i])

def day_18_2():
    row1 = '[[[[[9,8],1],2],3],4]'
    #row1 = '[[[[4,9],[1,2]],[[0,0],[1,6]]],[[5,6],[[8,4],[5,7]]]]'
    l = list(parenthetic_contents(row1))
    print(l)
#day_18_2()