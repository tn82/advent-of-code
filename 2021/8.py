import re
import random
def day_8():
    file = open('8_test.txt', 'r')
    input0 = []
    input = []
    for line in file:
        line_str = re.split(r"\|", line.strip())
        input0.append(list(filter(None, re.split(r"\s", line_str[0]))))
        input.append(list(filter(None, re.split(r"\s", line_str[1]))))
    #1, 4, 7, and 8
    easy_len = [2, 4, 3, 7]
    easy_count = 0
    for i in input:
        for j in i:
            if len(j) in easy_len:
                easy_count = easy_count + 1
    print(input)
    print(easy_count)

#day_8()

def common_chars(str1, str2):
    result = ''
    for char in str1:
        if char in str2 and not char in result:
            result += char
    return result

def day_8_2():
    file = open('8.txt', 'r')
    input0 = []
    input = []
    for line in file:
        line_str = re.split(r"\|", line.strip())
        input0.append(list(filter(None, re.split(r"\s", line_str[0]))))
        input.append(list(filter(None, re.split(r"\s", line_str[1]))))
    sum = 0
    for row, res in zip(input0, input):
        mapper = {}
        mapper2 = {}
        for i in row:
            if len(i) == 2:
                mapper[i] = 1
                mapper2[1] = i
            if len(i) == 4:
                mapper[i] = 4
                mapper2[4] = i
            if len(i) == 3:
                mapper[i] = 7
                mapper2[7] = i
            if len(i) == 7:
                mapper[i] = 8
                mapper2[8] = i
        for i in row:
            if len(i) == 6 and len(common_chars(i, mapper2[8])) == 6 and len(common_chars(i, mapper2[4])) == 3 and len(common_chars(i, mapper2[7])) == 3:
                mapper[i] = 0
                mapper2[0] = i
            if len(i) == 6 and len(common_chars(i, mapper2[8])) == 6 and len(common_chars(i, mapper2[4])) == 4 and len(common_chars(i, mapper2[7])) == 3:
                mapper[i] = 9
                mapper2[9] = i
            if len(i) == 6 and len(common_chars(i, mapper2[8])) == 6 and len(common_chars(i, mapper2[4])) == 3 and len(common_chars(i, mapper2[7])) == 2:
                mapper[i] = 6
                mapper2[6] = i
            if len(i) == 5 and len(common_chars(i, mapper2[4])) == 3 and len(common_chars(i, mapper2[7])) == 2:
                mapper[i] = 5
                mapper2[5] = i
            if len(i) == 5 and len(common_chars(i, mapper2[4])) == 2 and len(common_chars(i, mapper2[7])) == 2:
                mapper[i] = 2
                mapper2[2] = i
            if len(i) == 5 and len(common_chars(i, mapper2[4])) == 3 and len(common_chars(i, mapper2[7])) == 3:
                mapper[i] = 3
                mapper2[3] = i
        val = 0
        multi = 1000
        for j in res:
            for k in range(10):
                cl = len(common_chars(j, mapper2[k]))
                if cl == len(j) and cl == len(mapper2[k]):
                    val += mapper[mapper2[k]] * multi
                    multi = multi / 10
                    break
        sum += val
    print(sum)

day_8_2()
