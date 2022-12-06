with open("6.txt", "r") as file:
    buffer = file.read()

for i in range(0, len(buffer)):
    marker = buffer[i:i+4]
    if len(set(marker)) == 4:
        print(4+i)
        break
