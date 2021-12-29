def get_int(s):
    i = int(s[0])
    return i, s[1:]

def day():
    file = open('24.txt', 'r')
    input = []
    for line in file:
        row = line.strip().split(" ")
        input.append(row)

    d = {}
    monad =  "79997391969649"
    monad =  "16931171414113"
    monad_orig = monad
    d["w"] = 0
    d["x"] = 0
    d["y"] = 0
    d["z"] = 0
    count = 0
    for ins in input:
        if ins[0] == "inp":
            val, monad = get_int(monad)
            d[ins[1]] = val
            count += 1
            continue
        digge = int(ins[2]) if ins[2] not in ("wxyz") else d[ins[2]]
        if ins[0] == "add":
            d[ins[1]] += digge
            continue
        if ins[0] == "mul":
            d[ins[1]] *= digge
            continue
        if ins[0] == "div":
            if digge == 0:
                break
            d[ins[1]] = int(d[ins[1]] / digge)
            continue
        if ins[0] == "mod":
            if d[ins[1]] < 0 or digge < 0:
                break
            d[ins[1]] = d[ins[1]] % digge
            continue
        if ins[0] == "eql":
            d[ins[1]] = 1 if d[ins[1]] == digge else 0
            continue
    if d["z"] == 0:
        print("Check sum correct!!")
        print(monad_orig)
        print(d["z"])
        exit()
    print(count)
    print(monad_orig)
    print(d)
    count += 1
day()
