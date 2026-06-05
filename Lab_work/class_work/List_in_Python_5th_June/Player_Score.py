print("--------PLAYER--------")

player_score = []

for i in range(11):
    score = int(input("Input the score of player {}: ".format(i + 1)))
    player_score.append(score)

print("\nPlayer Scores:", player_score)

max_score = player_score[0]

for index in range(1, len(player_score)):
    if player_score[index] > max_score:
        max_score = player_score[index]

print("The Highest Score is:", max_score)
