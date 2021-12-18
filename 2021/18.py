from collections import defaultdict

def add_row(r1, r2):
    return r1 + "," + r2

def get_int(s, i):
    return int(s[i]), s[:i] + s[i+1:]

def remove(s, i):
    return s[:i] + s[i+1:]

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
    if dest == -1:
        return s[:src] + str(0) + s[src + 1:]
    else:
        dest_int = int(s[src]) + int(s[dest])
        return s[:dest] + str(dest_int) + s[dest + 1:]

def day_18():
    file = open('18.txt', 'r')

    input = []
    first = True
    for line in file:
            row = line.strip()
            input.append(row)
    regs = '0123456789'
    row1 = '[[[[[9,8],1],2],3],4]'
    left = row1.rfind("[[[[")
    if left != -1:
        left += 3
        right = row1.find("]", left)
        row1 = remove(row1, right)
        row1 = remove(row1, left)
        right_reg = find_right_reg(row1, right)
        row1 = add_int(row1, right_reg, right-2)
        row1 = remove(row1, right-1) # ","
        row1 = remove(row1, right-2) # 
        
        left_reg = find_left_reg(row1, left)
        row1 = add_int(row1, left_reg, left)


    four_r = row1.find("]]]]")
    if four_r != -1:
        print(1)
    #for c in row:
    #    row1find
day_18()