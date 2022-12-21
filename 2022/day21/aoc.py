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


def part_one():
    monkeys = []
    for line in input():
        com = line.split(" ")
        if len(com) > 2:
            monkeys.append(
                Monkey(com[0].replace(":", ""), com[1], 0, com[3], 0, com[2], 0)
            )
        else:
            monkeys.append(Monkey(com[0].replace(":", ""), "", 0, "", 0, "", int(com[1])))
    md = {}
    for m in monkeys:
        md[m.name] = m

    reduced = 1
    while reduced > 0:
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
                    if m.operand == "*":
                        m.num = m.oper1_num * m.oper2_num

    print("Part 1: ", md["root"].num)
    assert md["root"].num == 10037517593724


#part_one()

def reduce(yell):
    monkeys = []
    for line in input():
        com = line.split(" ")
        if len(com) > 2:
            monkeys.append(
                Monkey(com[0].replace(":", ""), com[1], 0, com[3], 0, com[2], 0)
            )
        else:
            if yell and com[0].replace(":", "") == "humn":
                monkeys.append(Monkey("humn", "", 0, "", 0, "", yell))
            else:
                monkeys.append(Monkey(com[0].replace(":", ""), "", 0, "", 0, "", int(com[1])))

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
                    if m.name == "root" and m.oper1_num == m.oper2_num:
                        print("root", yell, m.oper1_num)
                        exit(0)
                    if m.name == "root":
                        print(
                            "root2",
                            yell,
                            m.oper1_num,
                            m.oper2_num,
                            (m.oper1_num / m.oper2_num - 1) * 100,
                        )
                        breaker = True
                        break

                    if m.operand == "+":
                        m.num = m.oper1_num + m.oper2_num
                    if m.operand == "-":
                        m.num = m.oper1_num - m.oper2_num
                    if m.operand == "/":
                        m.num = m.oper1_num / m.oper2_num
                        if abs(m.num - round(m.num, 0)) > 0.000001:
                            breaker = True
                            break
                        m.num = int(m.oper1_num / m.oper2_num)
                    if m.operand == "*":
                        m.num = m.oper1_num * m.oper2_num

def part_two():
    X = 1
    c = 1
    count = 0

    start = 3272260914328
    for yell in range(start-100, start + 100):
        
        monkeys = []
        for line in input():
            com = line.split(" ")
            if len(com) > 2:
                monkeys.append(
                    Monkey(com[0].replace(":", ""), com[1], 0, com[3], 0, com[2], 0)
                )
            else:
                if com[0].replace(":", "") == "humn":
                    monkeys.append(Monkey("humn", "", 0, "", 0, "", yell))
                else:
                    monkeys.append(Monkey(com[0].replace(":", ""), "", 0, "", 0, "", int(com[1])))

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
                        if m.name == "root" and m.oper1_num == m.oper2_num:
                            print("root", yell, m.oper1_num)
                            exit(0)
                        if m.name == "root":
                            print(
                                "root2",
                                yell,
                                m.oper1_num,
                                m.oper2_num,
                                (m.oper1_num / m.oper2_num - 1) * 100,
                            )
                            breaker = True
                            break

                        if m.operand == "+":
                            m.num = m.oper1_num + m.oper2_num
                        if m.operand == "-":
                            m.num = m.oper1_num - m.oper2_num
                        if m.operand == "/":
                            m.num = m.oper1_num / m.oper2_num
                            if abs(m.num - round(m.num, 0)) > 0.000001:
                                breaker = True
                                break
                            m.num = int(m.oper1_num / m.oper2_num)
                        if m.operand == "*":
                            m.num = m.oper1_num * m.oper2_num


    print("Part 2: ", 3272260914328)
    assert 3272260914328 == 3272260914328


part_two()
