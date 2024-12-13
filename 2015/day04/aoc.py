import hashlib

def part_one():
    key = "ckczppom"
    i5 = 0
    i6 = 0
    for i in range(1000000000):
        md5_hash = hashlib.md5((key + str(i)).encode('utf-8')).hexdigest()
        if md5_hash[:6] == "000000":
            i6 = i
            break
        if i5 == 0 and md5_hash[:5] == "00000":
            i5 = i

    print("Part 1: ", i5)
    assert(i5 == 117946)

    print("Part 2: ", i6)
    assert(i6 == 3938038)



part_one()