
def part_one():
    file = open("input.txt", "r")

    current_path = ""
    files = []
    directories = []

    breaker = 0
    for line in file:
        breaker += 1
        if breaker > 100*100:
            break
        parts = line.strip().split()

        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "/":
                    current_path = "/"
                elif parts[2] == "..":
                    current_path = current_path.rstrip("/")
                    current_path, _ = current_path.rsplit("/", 1)
                    current_path += "/"
                else:
                    if not current_path.endswith("/"):
                        current_path += "/"
                    current_path += parts[2] + "/"


        elif parts[0].isdigit():
            size, file = parts
            file_path = current_path + file
            files.append([file_path, int(size)])

        elif parts[0] == "dir":
            directory = parts[1]
            directory_path = current_path + directory + "/"
            directories.append(directory_path)


    dir_sizes = {}
    for dir in directories:
        dir_size = 0
        for file_name, file_size in files:
            if file_name.startswith(dir):
                dir_size += file_size
        dir_sizes[dir] = dir_size

    part_one = sum(size for size in dir_sizes.values() if size <= 100000)
    assert part_one == 1232307
    print("Part 1: ", part_one)

    remove = 30000000 - 70000000 + sum(file_size for _, file_size in files)
    part_two = 1e14
    for dir in directories:
        dir_size = 0
        for file_name, file_size in files:
            if file_name.startswith(dir):
                dir_size += file_size
        if dir_size >= remove and dir_size < part_two:
            part_two = dir_size

    assert part_two == 7268994
    print("Part 2: ", part_two)

part_one()

