def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]

def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]

def part_one():
    count = 0
    sum = 0
    conv = {}
    conv["="] = -2
    conv["-"] = -1
    conv["0"] = 0
    conv["1"] = 1
    conv["2"] = 2
    for line in input():
        l_sum = 0
        while line:
            l = len(line)
            n = conv[line[0]]
            line = line[1:]
            l_sum += 5**(l-1) * n
        sum += l_sum
    print(sum)

    for digits in range(0, 30):
        d = digits
        max_s = 0
        while True:
            max_s += 2*5**(d - 1)
            d -= 1
            if d <= 0:
                break
        if max_s > sum:
            break

    SNAFU = "2" * digits
    for i, _ in enumerate(SNAFU):
        for o in ("2", "1", "0", "-", "="):
            SNAFU_tmp = SNAFU[0:i] + o + SNAFU[i+1:]
            l_sum = 0
            while SNAFU_tmp:
                l = len(SNAFU_tmp)
                n = conv[SNAFU_tmp[0]]
                SNAFU_tmp = SNAFU_tmp[1:]
                l_sum += 5**(l-1) * n
            if l_sum >= sum:
                SNAFU = SNAFU[0:i] + o + SNAFU[i+1:]
                if l_sum == sum:
                    #print("ans", SNAFU[0:i] + o + SNAFU[i+1:])
                    break
            else:
                break

    print("Part 1: ", SNAFU)
    assert count == 0

part_one()
