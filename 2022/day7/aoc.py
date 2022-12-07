
def part_one1():
    file = open("input.txt", "r")
    
    current_path = ""
    files = {}
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
            path2 = current_path + file
            files[path2] = int(size)

        elif parts[0] == "dir":
            directory = parts[1]
            #if not current_path.endswith("/"):
            #    directory = "/" + directory
            path2 = current_path + directory + "/"
            directories.append(path2)

    print(directories)
    print(files)
    sizes = {}
    for directory in directories:
        #directory = directory + "/"
        size = sum(
            s for file, s in files.items() if file.startswith(directory)
        )
        print(size)
        sizes[directory] = size

    part_one = sum(size for size in sizes.values() if size <= 100000)
    print(part_one)
    assert part_one == 1232307
    print("Part 1: ", part_one)

    remove = 30000000 - 70000000 + sum(s for _, s in files.items())
    part_two = 1e14
    for directory in directories:
        directory = directory + "/"
        size = sum(
            s for file, s in files.items() if file.startswith(directory)
        )
        if size >= remove and size < part_two:
            part_two = size

    assert part_two == 7268994
    print("Part 2: ", part_two)

part_one1()

