import re

def day_3():
    file = open('3.txt', 'r')
    sum_list = [0] * 12
    count = 0
    for line in file:
        count = count + 1
        line_list = [int(char) for char in line.strip()]
        sum_list = [a + b for a, b in zip(line_list, sum_list)]
        
    print(sum_list)
    print(count)
    s1 = [1 if s * 2 >= count else 0 for s in sum_list]
    s2 = [1 if s * 2 < count else 0 for s in sum_list]
    s1_str = ""
    for i in s1:
        s1_str = s1_str + str(i)
    print(s1_str)
    print(int(s1_str, 2))
    
    s2_str = ""
    for i in s2:
        s2_str = s2_str + str(i)
    print(s2_str)
    print(int(s2_str, 2))

    #011101111100 1916
    #100010000011 2179

#day_3()

def day_3_2():
    file = open('3.txt', 'r')
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)

    oxy_lines = lines
    oxy_result = 0
    for i in range(12):
        count = 0
        zero_lines = []
        one_lines = []
        for line in oxy_lines:
            if line[i] == '0':
                zero_lines.append(line)
            else:
                one_lines.append(line)
        oxy_lines = one_lines if len(one_lines) >= len(zero_lines) else zero_lines
        if len(oxy_lines) == 1:
            print("oxy_lines")
            print(oxy_lines)
            oxy_result = int(oxy_lines[0], 2)
            break

    co2_lines = lines
    co2_result = 0
    for i in range(12):
        count = 0
        zero_lines = []
        one_lines = []
        for line in co2_lines:
            count = count + int(line[i])
            if line[i] == '0':
                zero_lines.append(line)
            else:
                one_lines.append(line)
        co2_lines = one_lines if len(one_lines) < len(zero_lines) else zero_lines
        if len(co2_lines) == 1:
            print("co2_lines")
            print(co2_lines)
            co2_result = int(co2_lines[0], 2)
            break
    print(('Result: {}, {}, {}').format(oxy_result, co2_result, oxy_result*co2_result))

day_3_2()