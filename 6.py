with open("6.txt", "r") as file:
    buffer = file.read()

n = 14


for i in range(0, len(buffer)):
    marker = buffer[i:i+n]
    if len(set(marker)) == n:
        print(n+i)
        break
