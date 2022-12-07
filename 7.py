with open("7.txt", "r") as file:
    lines = file.read().split("\n")

file_system = {
    "/": {}
}

path = []


#  Built file system
for line in lines:
    print("\nnewline:" + line)
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

file_sizes = {}

def find_size(dir: dict) -> int:
    for value in dir.values():


for key in file_system["/"]:

