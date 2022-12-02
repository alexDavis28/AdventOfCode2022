shape_scores = {
    "A": 1,
    "B": 2,
    "C": 3
}
shape_translation = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}
winning_move = {
    "A": "B",
    "B": "C",
    "C": "A"
}

p2 = {
    "X": 2,
    "Y": 0,
    "Z": 1
}

plays = ["A", "B", "C"]

with open("2.txt", "r") as file:
    rounds = [i.split() for i in file.read().split("\n")]

score = 0
for round in rounds:
    opponent = round[0]
    player = plays[(plays.index(opponent) + p2[round[1]]) % 3]

    score += shape_scores[player]
    if player == winning_move[opponent]:
        score += 6
    elif player == opponent:
        score += 3
print(score)
