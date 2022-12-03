items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("3.txt", "r") as file:
    lines = file.read().splitlines()
    groups = [[lines[i], lines[i+1], lines[i+2]] for i in [j for j in range(len(lines))][::3]]
common_items = []
for group in groups:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            common_items.append(item)
            break

priorities = [items.index(i)+1 for i in common_items]
print(sum(priorities))
