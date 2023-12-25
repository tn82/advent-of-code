import os
from collections import defaultdict

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def int_list(char_list):
    return [int(c.strip()) for c in char_list.split(",")]

from decimal import *

def line_conv(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return Decimal(A), Decimal(B), Decimal(-C)

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False, False
    
def part_one():
    sums = 0
    pos_vel = []
    getcontext().prec = 24
    for i, line in enumerate(input()):
        pos, vel = line.split("@")
        pos = int_list(pos)
        vel = int_list(vel)
        pos_vel.append([pos, vel])

    lb = Decimal(200000000000000.0)
    ub = Decimal(400000000000000.0)
    #lb = Decimal(7.0)
    #ub = Decimal(17.0)
    for a in range(len(pos_vel)):
        for b in range(a + 1, len(pos_vel)):
            ax, ay, az = pos_vel[a][0]
            avx, avy, avz = pos_vel[a][1]

            bx, by, bz = pos_vel[b][0]
            bvx, bvy, bvz = pos_vel[b][1]

            delta = 1
            line1 = line_conv((ax, ay), (ax + avx * delta, ay + avy * delta))
            line2 = line_conv((bx, by), (bx + bvx * delta, by + bvy * delta))
            ix, iy = intersection(line1, line2)
            if not ix or not iy:
                continue
            if avx > 0 and ix < ax:
                continue
            if avx < 0 and ix > ax:
                continue
            if avy > 0 and iy < ay:
                continue
            if avy < 0 and iy > ay:
                continue
            if bvx > 0 and ix < bx:
                continue
            if bvx < 0 and ix > bx:
                continue
            if bvy > 0 and iy < by:
                continue
            if bvy < 0 and iy > by:
                continue
            if lb <= ix <= ub and lb <= iy <= ub:
                sums += 1
            else:
                continue


    print("Part 1: ", sums)
    assert(sums == 18184)


from skspatial.objects import Line
import numpy as np

# Line(point=[24, 13, 10], direction=[-3, 1, 2]), 5, 3, 4
def solve_point(vars):
    x, y, z, xv, yv, zv, t1, t2, t3 = vars
    #f = np.empty((9))
    f = [0] * 9
    f[0] = 19 - 2*t1 - x - xv*t1
    f[1] = 18 - 1*t2 - x - xv*t2
    f[2] = 20 - 2*t3 - x - xv*t3

    f[3] = 13 + 1*t1 - y - yv*t1
    f[4] = 19 - 1*t2 - y - yv*t2
    f[5] = 25 - 2*t3 - y - yv*t3

    f[6] = 30 - 2*t1 - z - zv*t1
    f[7] = 22 - 2*t2 - z - zv*t2
    f[8] = 34 - 4*t3 - z - zv*t3
    return f

def solve_point2(vars):
    x, y, z, xv, yv, zv, t1, t2, t3 = vars
    global pos_vel
    f = [0] * 9

    px, py, pz = pos_vel[0][0]
    pxv, pyv, pzv = pos_vel[0][1]
    f[0] = px + pxv*t1 - x - xv*t1
    f[1] = py + pyv*t1 - y - yv*t1
    f[2] = pz + pzv*t1 - z - zv*t1
    
    px, py, pz = pos_vel[1][0]
    pxv, pyv, pzv = pos_vel[1][1]
    f[3] = px + pxv*t2 - x - xv*t2
    f[4] = py + pyv*t2 - y - yv*t2
    f[5] = pz + pzv*t2 - z - zv*t2

    px, py, pz = pos_vel[2][0]
    pxv, pyv, pzv = pos_vel[2][1]
    f[6] = px + pxv*t3 - x - xv*t3
    f[7] = py + pyv*t3 - y - yv*t3
    f[8] = pz + pzv*t3 - z - zv*t3

    return f


def solve_point3(vars):
    x, y, z, xv, yv, zv, _, __, ___ = vars
    global pos_vel
    f = [0] * 9

    px, py, pz = pos_vel[0][0]
    pxv, pyv, pzv = pos_vel[0][1]
    a1 = (x - px)
    a2 = (y - py)
    a3 = (z - pz)
    b1 = (xv - pxv)
    b2 = (yv - pyv)
    b3 = (zv - pzv)
    
    f[0] = a2 * b3 - a3 * b2
    f[1] = -(a1 * b3 - a3 * b1)
    f[2] = a1 * b2 - a2 * b1
    
    px, py, pz = pos_vel[1][0]
    pxv, pyv, pzv = pos_vel[1][1]
    a1 = (x - px)
    a2 = (y - py)
    a3 = (z - pz)
    b1 = (xv - pxv)
    b2 = (yv - pyv)
    b3 = (zv - pzv)
    f[3] = a2 * b3 - a3 * b2
    f[4] = -(a1 * b3 - a3 * b1)
    f[5] = a1 * b2 - a2 * b1

    px, py, pz = pos_vel[2][0]
    pxv, pyv, pzv = pos_vel[2][1]
    a1 = (x - px)
    a2 = (y - py)
    a3 = (z - pz)
    b1 = (xv - pxv)
    b2 = (yv - pyv)
    b3 = (zv - pzv)
    f[6] = a2 * b3 - a3 * b2
    f[7] = -(a1 * b3 - a3 * b1)
    f[8] = a1 * b2 - a2 * b1
    return f

pos_vel = []
from scipy.optimize import fsolve
def part_two():
    sums = 0
    global pos_vel
    getcontext().prec = 24
    for i, line in enumerate(input()):
        pos, vel = line.split("@")
        pos = int_list(pos)
        vel = int_list(vel)
        pos_vel.append([pos, vel])

    xmin = 1e17
    xmax = -1e17
    ymin = 1e17
    ymax = -1e17
    zmin = 1e17
    zmax = -1e17
    for a in range(len(pos_vel)):
        ax, ay, az = pos_vel[a][0]
        avx, avy, avz = pos_vel[a][1]
        if avx > 0 and ax < xmin:
            xmin = ax
        if avx < 0 and ax > xmax:
            xmax = ax
        if avy > 0 and ay < ymin:
            ymin = ay
        if avy < 0 and ay > ymax:
            ymax = ay
        if avz > 0 and az < zmin:
            zmin = az
        if avz < 0 and az > zmax:
            zmax = az

    start_guess = [24, 13, 10, -3, 1, 2]
    start_guess = [24, 13, 10, 0, 0, 0]
    start_guess = [xmin, ymin, zmin, 0, 0, 0, 0, 0, 0]
    ans = fsolve(solve_point3, start_guess, xtol = 1e-14)
    print(ans)
    f = solve_point3(ans)
    x, y, z, xv, yv, zv, _, __, ___ = ans
    sums = round(x, 0) + round(y, 0) + round(z, 0)
    print(sums)
    
    print("Part 1: ", sums)
    assert(sums == 557789988450159)


#part_one()
part_two()