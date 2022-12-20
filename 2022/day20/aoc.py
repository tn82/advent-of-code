def input():
    with open("input.txt", "r") as file:
        return [line.rstrip() for line in file]


def input_test():
    with open("test.txt", "r") as file:
        return [line.rstrip() for line in file]


def decrypt(decryption_key, loops):
    encrypt = []
    index = []
    for i, line in enumerate(input()):
        encrypt.append(int(line) * decryption_key)
        index.append(i)

    size = len(index)
    for _ in range(0, loops):
        i = 0
        while i < size:
            new_i = index.index(i)
            index.pop(new_i)
            ei = encrypt.pop(new_i)
            j = (new_i + ei) % (size - 1)
            if j == 0:
                j = size - 1
            encrypt = encrypt[0:j] + [ei] + encrypt[j:]
            index = index[0:j] + [i] + index[j:]
            i += 1

    decrypted = 0
    index0 = encrypt.index(0)
    i = index0 + 1
    j = 1
    while i < index0 + 3001:
        if j in (1000, 2000, 3000):
            print(encrypt[i % size])
            decrypted += encrypt[i % size]
        i += 1
        j += 1
    return decrypted


part_one = decrypt(1, 1)
print("Part 1: ", part_one)
assert part_one == 8764

part_two = decrypt(811589153, 10)
print("Part 2: ", part_two)
assert part_two == 535648840980
