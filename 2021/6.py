
def day_6():
    file = open('6.txt', 'r')
    states = []
    for line in file:
        states = [int(l) for l in line.strip().split(",")]

    states = [3,4,3,1,2]
    states_c = [6] * len(states)
    dead_states = [0] * 9
    for s in states:
        dead_states[s] += 1
    for day in range(256):
        day_states = []
        day_states_c = []
        day_states1 = []
        day_states_c1 = []
        for s, c in zip(states, states_c):
            if s > 0:
                s -= 1
                day_states.append(s)
                day_states_c.append(c)
            else:
                day_states.append(6)
                day_states_c.append(6)
                day_states1.append(8)
                day_states_c1.append(8)
        states = day_states
        states += day_states1
        states_c = day_states_c
        states_c += day_states_c1
        print("{},{}".format(day, len(states)))

    print(len(states)) # 350917 correct

def day_6_2():
    file = open('6.txt', 'r')
    states = []
    for line in file:
        states = [int(l) for l in line.strip().split(",")]

    #states = [3,4,3,1,2]
    dead_states = [0] * 9
    for s in states:
        dead_states[s] += 1
    for day in range(256):
        print(dead_states)
        print(sum(dead_states)) # 350917 correct
        d0 = dead_states[0]
        dead_states[0] = dead_states[1]
        dead_states[1] = dead_states[2]
        dead_states[2] = dead_states[3]
        dead_states[3] = dead_states[4]
        dead_states[4] = dead_states[5]
        dead_states[5] = dead_states[6]
        dead_states[6] = dead_states[7]
        dead_states[7] = dead_states[8]
        dead_states[8] = d0
        dead_states[6] += d0


    print(dead_states)
    print(sum(dead_states)) # 350917 correct

day_6_2()
