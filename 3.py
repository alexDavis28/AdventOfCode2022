items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("3.txt", "r") as file:
    rucksacks = [[i[:len(i)//2], i[len(i)//2:]] for i in file.read().splitlines()]


common_items = []
for compartments in rucksacks:
    for item in compartments[0]:
        if item in compartments[1]:
            common_items.append(item)
            break

priorities = [items.index(i)+1 for i in common_items]
print(sum(priorities))