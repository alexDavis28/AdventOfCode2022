with open("4.txt", "r") as file:
    pairs = [i.split(",") for i in file.read().splitlines()]
    print(pairs)

print(pairs)
range_values = [(i[0].split("-"), i[1].split("-")) for i in pairs]
ranges = [
    (
        set([a for a in (range(int(i[0][0]), int(i[0][1]) + 1))]),
        set([b for b in (range(int(i[1][0]), int(i[1][1]) + 1))])
     )
    for i in range_values]
print(ranges)

c = 0
for r in ranges:
    overlap = False
    for i in r[0]:
        if i in r[1]:
            overlap = True
    if overlap:
        c += 1
print(c)