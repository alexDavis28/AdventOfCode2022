with open("7.txt", "r") as file:
    lines = file.read().split("\n")

file_system = {
    "/": {}
}

path = []

#  Built file system
for line in lines:
    # print("\nnewline:" + line)
    line = line.split()
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                path.pop()
            else:
                path.append(line[2])
    elif line[0] == "dir":
        if line[1] not in working_dir:
            working_dir[line[1]] = {}
    else:
        working_dir[line[1]] = int(line[0])

    working_dir = file_system
    for i in path:
        working_dir = working_dir[i]


def find_dir_size(directory: dict) -> (str, int):
    size = 0
    for value in directory.values():
        if isinstance(value, dict):
            size += find_dir_size(value)
        else:
            size += value
    return size


def precise_sizes(directory: dict) -> [int]:
    sizes = []
    for key, value in directory.items():
        if isinstance(value, dict):
            sizes.append(find_dir_size(value))
            sizes += precise_sizes(value)
    return sizes


sizes = precise_sizes(file_system)

print(sum([s for s in sizes if s <= 100000]))

unused = 70000000 - find_dir_size(file_system)
for size in sorted(sizes):
    if size+unused >= 30000000:
        print(size)
        break