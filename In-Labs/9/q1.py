# Question 1
score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3

wins = 0
losses = 0
for _, score in score_differences.items():
    if score > 0:
        wins += 1
    elif score < 0:
        losses += 1

print(wins, "wins -", losses, "losses")
