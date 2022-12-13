from dataclasses import dataclass
import copy

@dataclass
class Monk:
    items: None
    oper: int
    oper_add: int
    test_div: int
    monk_true: int
    monk_false: int
    inspections = 0


def monkey_business(monks, rounds: int, divider: int):
    monk_prime_master = 1
    for monk in monks:
        monk_prime_master *= monk.test_div

    round = 0
    while(round < rounds):
        for monk in monks:
            while(monk.items):
                it = monk.items.pop(0)
                monk.inspections += 1
                worry = 0
                if monk.oper:
                    worry = int(it * monk.oper / divider)
                elif monk.oper_add:
                    worry = int((it + monk.oper_add) / divider)
                else:
                    worry = int(it * it / divider)

                # Reduce
                worry = worry % monk_prime_master
                if worry % monk.test_div == 0:
                    monks[monk.monk_true].items.append(worry)
                else:
                    monks[monk.monk_false].items.append(worry)
        round += 1
    
    result = [monk.inspections for monk in monks]
    result.sort()
    return result[-1] * result[-2]

def day11():
    test_monks = [
        Monk([79,98], 19, None, 23, 2, 3),
        Monk([54,65,75,74], None, 6, 19, 2, 0),
        Monk([79,60,97], None, None, 13, 1, 3),
        Monk([74], None, 3, 17, 0, 1),
    ]
    input_monks = [
        Monk([57,58], 19, None, 7, 2, 3),
        Monk([66,52,59,79,94,73], None, 1, 19, 4, 6),
        Monk([80], None, 6, 5, 7, 5),
        Monk([82, 81, 68, 66, 71, 83, 75, 97], None, 5, 11, 5, 2),
        Monk([55, 52, 67, 70, 69, 94, 90], None, None, 17, 0, 3),
        Monk([69, 85, 89, 91], None, 7, 13, 1, 7),
        Monk([75, 53, 73, 52, 75], 7, None, 2, 0, 4),
        Monk([94, 60, 79], None, 2, 3, 1, 6),
    ]

    part_one = monkey_business(monks=copy.deepcopy(input_monks), rounds=20, divider=3)
    print("Part 1: ", part_one)
    assert part_one == 50830

    part_two = monkey_business(monks=copy.deepcopy(input_monks), rounds=10000, divider=1)
    print("Part 2: ", part_two)
    assert part_two == 14399640002


day11()
