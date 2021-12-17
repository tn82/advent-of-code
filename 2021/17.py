
def day_17():
    #my:    target area: x=269..292, y=-68..-44
    # test: target area: x=20..30, y=-10..-5
    target_x = [20, 30]
    target_y = [-10, -5]
    target_x = [269, 292]
    target_y = [-68, -44]

    high_yg = -100000
    good_shots = 0
    for y in range(-100,100):
        print(y, good_shots)
        for x in range(-1000,1000):
            vx = x
            vy = y
            cx = 0
            cy = 0
            high_y = 0
            while True:
                if cx >= target_x[0] and cx <= target_x[1] and cy >= target_y[0] and cy <= target_y[1]:
                    if high_y > high_yg:
                        high_yg = high_y
                        #print(x, y, high_y)
                    good_shots += 1
                    break
                if cx > target_x[1] or cy < target_y[0]:
                    break
                cx += vx
                cy += vy
                if vx > 0:
                    vx += -1
                elif vx < 0:
                    vx += 1
                vy += -1
                if cy > high_y:
                    high_y = cy
    print(good_shots)
day_17() #p1 2278 correct
