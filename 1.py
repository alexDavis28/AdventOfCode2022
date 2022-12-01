with open("1.txt", "r") as file:
    lines = file.read().split("\n\n")
sums = [sum([int(i) for i in line.split()]) for line in lines]
print(sums)
print(max(sums))
print(sum(sorted(sums, reverse=True)[:3]))

# part 1 one-liner - ignore that it doesn't close the file, it's fine
print(max([sum([int(i) for i in line.split()]) for line in open("1.txt", "r").read().split("\n\n")]))

# part 2 one-liner
print(sum(sorted([sum([int(i) for i in line.split()]) for line in open("1.txt", "r").read().split("\n\n")], reverse=True)[:3]))