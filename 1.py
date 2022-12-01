with open("1.txt", "r") as file:
    lines = file.read().split("\n\n")
sums = [sum([int(i) for i in line.split()]) for line in lines]
print(sums)
print(max(sums))
print(sum(sorted(sums, reverse=True)[:3]))
