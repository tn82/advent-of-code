import os
from collections import defaultdict
import copy
day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def block_in_grid(block, grid, dz):
    if block[0][2] + dz == 0 or block[1][2] + dz == 0:
        return True # Floor
    for x in range(block[0][0], block[1][0] + 1):
        for y in range(block[0][1], block[1][1] + 1):
            for z in range(block[0][2], block[1][2] + 1):
                if (x, y, z + dz) in grid:
                    return True
    return False

def add_to_grid(block, grid):
    for x in range(block[0][0], block[1][0] + 1):
        for y in range(block[0][1], block[1][1] + 1):
            for z in range(block[0][2], block[1][2] + 1):
                grid[(x, y, z)] = 1

def del_from_grid(block, grid):
    for x in range(block[0][0], block[1][0] + 1):
        for y in range(block[0][1], block[1][1] + 1):
            for z in range(block[0][2], block[1][2] + 1):
                del grid[(x, y, z)]

def freeze_blocks(blocks, grid_stop):
    bc = 1
    while True:
        if not bc:
            break
        bc = 0
        grid_stop_n = copy.copy(grid_stop)
        for b in blocks:
            if block_in_grid(b, grid_stop, 0):
                continue # Already in grid
            if block_in_grid(b, grid_stop, -1):
                add_to_grid(b, grid_stop_n)
                bc += 1
        grid_stop = grid_stop_n
    return grid_stop

def move_to_stop(blocks, early_return):
    grid_stop = {}
    any_block_move = False
    blocks_moved = 1
    while True:
        if not blocks_moved:
            break
        grid_stop = freeze_blocks(blocks, grid_stop)
        blocks_moved = 0
        for b in blocks:
            if block_in_grid(b, grid_stop, 0):
                continue # Already in grid
            b[0][2] -= 1
            b[1][2] -= 1
            blocks_moved += 1
            any_block_move = True
            if early_return:
                return any_block_move
    return any_block_move

def part_one():
    sums = 0
    blocks = []
    for i, line in enumerate(test()):
        coo0, coo1 = line.split("~")
        coo0 = [int(c) for c in coo0.split(",")]
        coo1 = [int(c) for c in coo1.split(",")]
        blocks.append((coo0, coo1))

    any_block_move = move_to_stop(blocks, False)

    for i, b in enumerate(blocks):
        blocks_b = copy.copy(blocks)
        blocks_b.remove(b)
        any_block_move = move_to_stop(blocks_b, False)
        if not any_block_move:
            sums += 1
        if i % 100 == 0:
            print("Iteration:", i, sums)

    print("Part 1: ", sums) # too high 522
    #assert(sums == 0)


def part_two():
    sums = 0
    for i, line in enumerate(test()):
        sums += int(line)

    print("Part 2: ", sums)
    #assert(sums == 0)


part_one()
#part_two()



'''
    final_blocks = []
    orig_blocks = copy.copy(blocks)
    block_count = len(blocks)
    while blocks:
        if len(final_blocks) == block_count:
            break
        b = blocks.pop(0)
        if block_in_grid(b, grid_stop, -1):
            add_to_grid(b, grid_stop)
        else:
            blocks.append(block_down(b))
            final_blocks.append(b)
            '''