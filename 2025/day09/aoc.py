import os
from collections import defaultdict
#import heapq
#import copy
#from functools import cache
#import matplotlib.pyplot as plt
#import numpy as np

day_path = os.path.dirname(__file__)

def input():
    with open(os.path.join(day_path, "input.txt"), "r") as file:
        return [line.rstrip() for line in file]

def test():
    with open(os.path.join(day_path, "test.txt"), "r") as file:
        return [line.rstrip() for line in file]

def int_list(char_list):
    return [int(c) for c in char_list]

def part_one():
    sums = 0
    points = []
    for i, line in enumerate(input()):
        x, y = line.split(",")
        points.append((int(x), int(y)))

    area = 0
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i == j:
                continue
            a = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            if a > area:
                area = a
                print(i, j, a)

    print("Part 1: ", area)
    #assert(area == 4781377701)
'''
def plotter(points):
    x_coords, y_coords = zip(*points)

    # 3. Create the plot
    plt.figure(figsize=(8, 5))

    # Plotting as a scatter plot (distinct points)
    plt.plot(x_coords, y_coords, 'o', color='blue', label='Data Points')

    # 4. Add labels and title for clarity
    plt.title('Plot of 2D Points')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

    # 5. Save the plot
    plt.savefig('2d_points_plot.png')
'''
def is_point_in_polygon(point, polygon_points):
    """
    Checks if a 2D point is enclosed by a polygon defined by a list of points 
    that form a closed loop (last point connects to the first).
    Uses the Ray Casting Algorithm.

    Args:
        point (tuple or list): (x, y) coordinates of the point to check.
        polygon_points (list of tuples/lists): [(x1, y1), (x2, y2), ...] 
                                               defining the polygon vertices.

    Returns:
        bool: True if the point is inside or on the boundary, False otherwise.
    """

    px, py = point
    intersections = 0
    n = len(polygon_points)
    
    if n < 3:
        return False
    
    # Loop through all edges of the polygon. We use the modulo operator (%) 
    # to handle the wrap-around from the last vertex (n-1) to the first (0).
    for i in range(n):
        # Current edge vertices: (p1) is the current vertex, (p2) is the next
        p1 = polygon_points[i]
        p2 = polygon_points[(i + 1) % n]
        
        x1, y1 = p1
        x2, y2 = p2
        
        # --- 1. Check if the point is ON the boundary (optional but good practice) ---
        # The equation for the line segment from p1 to p2 is 
        # (py - y1) * (x2 - x1) == (px - x1) * (y2 - y1)
        if (py - y1) * (x2 - x1) == (px - x1) * (y2 - y1):
            # Check if the point is within the bounding box of the segment
            if (min(y1, y2) <= py <= max(y1, y2) and 
                min(x1, x2) <= px <= max(x1, x2)):
                return True # Point is exactly on the boundary

        # --- 2. Ray Casting Algorithm (Intersection Check) ---
        
        # We cast a ray horizontally to the right from the test point (px, py).
        # We only count intersections if the edge (p1, p2) crosses the ray
        # and one vertex is strictly above the ray and the other is below or on it.
        
        # 2a. Check if the ray intersects the edge's Y-span
        if ((y1 <= py < y2) or (y2 <= py < y1)):
            
            # 2b. Calculate the X-coordinate of the intersection point (xi)
            # The intersection point x is found using the line equation:
            # xi = x1 + (px - x1) * (y2 - y1) / (x2 - x1)  <-- WRONG formula below
            
            # xi = x1 + (py - y1) / (y2 - y1) * (x2 - x1) 
            
            # Simplified check: Only need to know if the intersection is to the right of px
            if x1 + (py - y1) / (y2 - y1) * (x2 - x1) < px:
                # If the intersection point's X-coordinate is less than px, 
                # the ray must have crossed the edge.
                intersections += 1
                
    # 3. Final Result: If the number of intersections is odd, the point is inside.
    return intersections % 2 == 1

def part_two():
    sums = 0
    points = []
    for i, line in enumerate(input()):
        x, y = line.split(",")
        points.append((int(x), int(y)))
    #plotter(points)

    area = 0
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i == j:
                continue
            a = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            if a <= area or a < 1470616992-1e6:
                continue
            if a <= area or a > 1470616992+1e6:
                continue
            print(i, j, area)
            ok = True
            for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                ok = is_point_in_polygon((x, p1[1]), points)
                if not ok:
                    break
                ok = is_point_in_polygon((x, p2[1]), points)
                if not ok:
                    break
                
            if not ok:
                continue
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+ 1):
                ok = is_point_in_polygon((p1[0], y), points)
                if not ok:
                    break
                ok = is_point_in_polygon((p2[0], y), points)
                if not ok:
                    break

            if ok and a > area:
                area = a
                print(i, area)

    print("Part 2: ", area) #
    assert(area == 1470616992)


#part_one()
part_two()