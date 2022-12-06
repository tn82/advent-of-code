def position_unique(message: str, number_unique: int):
    l1 = []
    s1 = set()
    pos = 0
    for c in message:
        pos += 1
        if len(l1) == number_unique:
            pop_tmp = l1.pop(0)
            s1.remove(pop_tmp)
        l1.append(c)
        for c_tmp in l1:
            s1.add(c_tmp)
        if len(s1) == number_unique:
            break
    return pos


def part_one():
    with open("input.txt", "r") as file:
        line = file.readline().strip()
        part_one = position_unique(line.strip(), 4)
        assert part_one == 1723
        print("Part 1: ", part_one)

        part_two = position_unique(line.strip(), 14)
        assert part_two == 3708
        print("Part 2: ", part_two)


part_one()
