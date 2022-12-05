import re

with open("5.txt", "r") as file:
    data = file.read().split("\n\n")
print(data[0])
inital = data[0].split("\n")
stack_names = inital[-1].split()
instructions = data[1].split("\n")

cleaned_initial = [i.count(" ") for i in inital]

stacks = [[] for i in stack_names]

for line in inital[:-1]:
    # print(len(line))
    # print(line[1::4])
    # position = line.index("J") // 4
    for i, char in enumerate(line[1::4]):
        # print(i, char)
        if char != " ":
            stacks[i].append(char)

for stack in stacks:
    stack.reverse()
print(stacks)
for instruction in instructions:
    temp = []
    moves, a, b = [int(i) for i in re.findall(r"(\d+)", instruction)]
    for i in range(moves):
        temp.append(stacks[a-1].pop())
    temp.reverse()
    for i in temp:
        stacks[b-1].append(i)

print("".join([s.pop() for s in stacks]))