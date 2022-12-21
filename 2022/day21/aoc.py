from dataclasses import dataclass


def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]


def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]


@dataclass
class Monkey:
    name: str
    oper1: str
    oper1_num: int
    oper2: str
    oper2_num: int
    operand: str
    num: int


def reduce(replace_yell):
    monkeys = []
    for line in input():
        com = line.split(" ")
        if len(com) > 2:
            monkeys.append(
                Monkey(com[0].replace(":", ""), com[1], 0, com[3], 0, com[2], 0)
            )
        else:
            if replace_yell and com[0].replace(":", "") == "humn":
                monkeys.append(Monkey("humn", "", 0, "", 0, "", replace_yell))
            else:
                monkeys.append(
                    Monkey(com[0].replace(":", ""), "", 0, "", 0, "", int(com[1]))
                )

    md = {}
    for m in monkeys:
        md[m.name] = m

    reduced = 1
    breaker = False

    while not breaker and reduced > 0:
        reduced = 0
        for m in monkeys:
            if m.num == 0:
                if not m.oper1_num and md[m.oper1].num:
                    m.oper1_num = md[m.oper1].num
                    reduced += 1
                if not m.oper2_num and md[m.oper2].num:
                    m.oper2_num = md[m.oper2].num
                    reduced += 1
                if m.oper1_num and m.oper2_num:
                    if m.operand == "+":
                        m.num = m.oper1_num + m.oper2_num
                    if m.operand == "-":
                        m.num = m.oper1_num - m.oper2_num
                    if m.operand == "/":
                        m.num = m.oper1_num / m.oper2_num
                        # Only valid if int but we can get direction of solution from the invalid solution
                        m.num = int(m.oper1_num / m.oper2_num)
                    if m.operand == "*":
                        m.num = m.oper1_num * m.oper2_num
                    if replace_yell and m.name == "root" and m.oper1_num == m.oper2_num:
                        return m.num, 0
                    if m.name == "root":
                        return m.num, (m.oper1_num / m.oper2_num - 1) * 100
    return 0, -1


def part_two():
    part_one, direction = reduce(0)
    print("Part 1: ", part_one)
    assert part_one == 10037517593724

    part_two = 0
    yell_low_bound = 1
    yell_high_bound = part_one # Use part1 as upperbound, why not
    yell = 1
    while True:
        # Pattern in m.oper1_num / m.oper2_num
        # Interval half seach for this pattern
        num, direction = reduce(yell)
        if direction == -1:
            yell += 1
        elif direction > 0.0:
            yell_low_bound = yell
            yell = int((yell_high_bound + yell_low_bound) / 2)
        elif direction < 0.0:
            yell_high_bound = yell
            yell = int((yell_high_bound + yell_low_bound) / 2)
        elif not direction:
            part_two = yell
            break

    print("Part 2: ", part_two)
    assert 3272260914328 == part_two


part_two()
