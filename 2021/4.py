import re
def day_4():
    file = open('4.txt', 'r')
    row_i = 0
    bing_nums = []
    board_rows = []
    for line in file:
        #new_board = 
        if row_i == 0:
            bing_nums = [int(l) for l in line.strip().split(",")]
        else:
            l1 = [int(l) for l in line.strip().split()]
            if l1:
                board_rows.append(l1)
        row_i = row_i + 1

    bn_rc = {}
    for b in range(100):
        break_b = False
        hits = []
        for c in range(5):
            hit_rows = []
            bn = -1
            for n in bing_nums:
                bn = bn + 1
                for r in range(5):
                    if n == board_rows[b * 5 + r][c] and n not in hits:
                        hits.append(n)
                    if n == board_rows[b * 5 + r][c] and n not in hit_rows:
                        hit_rows.append(n)
                        if len(hit_rows) == 5:
                            if b in bn_rc:
                                bn_rc[b] = min(bn_rc[b], bn)
                            else:
                                bn_rc[b] = bn
                            #if bn < breaker:
                            #print("row,{},{},{}".format(bn, hit_rows, b))
                            #print(hits)
                            #break_b = True
                            #break
                if break_b:
                    break
            if break_b:
                    break
                
    for b in range(100):
        break_b = False
        hits = []
        for r in range(5):
            hit_cols =  []
            bn = -1
            for n in bing_nums:
                bn = bn + 1
                for c in range(5):
                    if n == board_rows[b * 5 + r][c] and n not in hits:
                        hits.append(n)
                    if n == board_rows[b * 5 + r][c] and n not in hit_cols:
                        hit_cols.append(n)
                        if len(hit_cols) == 5:
                            if b in bn_rc:
                                bn_rc[b] = min(bn_rc[b], bn)
                            else:
                                bn_rc[b] = bn
                            #if bn < breaker:
                            #print("col,{},{},{}".format(bn, hit_cols,b))
                            #print(hits)
                            #break_b = True
                            #break
                if break_b:
                    break
            if break_b:
                break
    print(bn_rc)
    b = max(bn_rc, key=bn_rc.get)
    print(b)
    print(max(bn_rc.values()))

    hits = []
    bn = -1
    for n in bing_nums:
        bn = bn + 1
        for r in range(5):
            for c in range(5):
                if n == board_rows[b * 5 + r][c]:
                    tmp = board_rows[b * 5 + r]
                    hits.append(n)
                    if bn == max(bn_rc.values()):
                        sum = 0
                        for h in hits:
                            sum += h
                        print(hits)
                        print(sum)

    sum = 0
    for r in range(5):
        for c in range(5):
            sum += board_rows[b * 5 + r][c]
    print(sum)


day_4()
