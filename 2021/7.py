
def day_7():
    file = open('20211207.txt', 'r')
    positions = []
    for line in file:
        positions = [int(l) for l in line.strip().split(",")]

    #states = [16,1,2,0,4,2,7,1,2,14]
    min_pos = min(positions)
    max_pos = max(positions)
    min_fuel = 1e10
    for pos_i in range(min_pos, max_pos + 1):
        positions_i = [pos_i] * len(positions)
        steps = [abs(i - j) for (i, j) in zip(positions, positions_i)]
        fuels = [c*(c+1)/2 for c in steps]
        fuel = sum(fuels)
        if fuel < min_fuel:
            print(pos_i)
            print(fuel)
            min_fuel = fuel
            # 355592 correct
day_7()
