import time

def loop_x(target_x, target_y, y, max_y):
    good_shots = 0
    for x in range(0, 1000):
        vx = x
        vy = y
        cx = 0
        cy = 0
        max_y_x = 0
        while True:
            if cx >= target_x[0] and cx <= target_x[1] and cy >= target_y[0] and cy <= target_y[1]:
                if max_y_x > max_y:
                    max_y = max_y_x
                good_shots += 1
                break
            #if cx > target_x[1]:
                # Not possible to find a solution for any x higher then current
            #    return max_y, good_shots
            if cx > target_x[1] or cy < target_y[0]:
                break
            cx += vx
            cy += vy
            if vx > 0:
                vx += -1
            elif vx < 0:
                vx += 1
            vy += -1
            if cy > max_y_x:
                max_y_x = cy
    return max_y, good_shots

def day_17():
    #my:    target area: x=269..292, y=-68..-44
    # test: target area: x=20..30, y=-10..-5
    target_x = [269, 292]
    target_y = [-68, -44]

    max_y = -100000
    hits = 0
    for y in range(-100, 100):
        max_y_x, hits_x = loop_x(target_x, target_y, y, max_y)
        hits += hits_x
        max_y = max(max_y, max_y_x)
    print(f"Part one: {max_y}") # 2278
    print(f"Part two: {hits}") # 996

time_start = time.perf_counter()
day_17()
print(f"Time: {time.perf_counter() - time_start}") 