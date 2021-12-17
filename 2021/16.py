import math

def get_int(b, n):
    return int(b[:n], 2), b[n:]

def split(b, n):
    return b[:n], b[n:]

def calc_pack(b):
    version, b = get_int(b, 3)
    type_id, b = get_int(b, 3)

    if type_id == 4: # literal
        sub_b_tot = ""
        while True:
            prefix_bit, b = get_int(b, 1)
            sub_b, b = split(b, 4)
            sub_b_tot += sub_b
            if prefix_bit == 0:
                break
        return version, int(sub_b_tot, 2), b

    else: # operator
        length_type, b = get_int(b, 1)
        values = []
        if length_type == 0:
            sub_length, b = get_int(b, 15)
            sub_b, b = split(b, sub_length)

            while len(sub_b) and '1' in sub_b:
                sub_version, sub_value, sub_b = calc_pack(sub_b)
                version += sub_version
                values.append(sub_value)

        elif length_type == 1:
            sub_count, b = get_int(b, 11)
            for i in range(sub_count):
                sub_version, sub_value, b = calc_pack(b)
                version += sub_version
                values.append(sub_value)
        value = 0
        if type_id == 0:
            value = sum(values)
        if type_id == 1:
            value = math.prod(values)
        if type_id == 2:
            value = min(values)
        if type_id == 3:
            value = max(values)
        if type_id == 5:
            value = 1 if values[0] > values[1] else 0
        if type_id == 6:
            value = 1 if values[0] < values[1] else 0
        if type_id == 7:
            value = 1 if values[0] == values[1] else 0
        return version, value, b

def day_16():
    file = open('16.txt', 'r')
    input = []
    for line in file:
        input.append(line.strip())
        break

    binary = ""
    for c in input[0]:
        # Remove first 2 chars from bin "0b". Fill up to 4 bits as described in the problem.
        binary += bin(int(c, 16))[2:].zfill(4)

    version_sum, value, _ = calc_pack(binary)
    print("Part 1:", version_sum)
    print("Part 2:", value)
day_16()