runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")

for player, score in runs.items():
    if score > 500:
        print(player)

# 2. Find the Orange Cap winner
orange_cap = max(runs, key=runs.get)

print("\nOrange Cap Winner:", orange_cap, "(", runs[orange_cap], ")", sep="")

# 3. Find the lowest scorer
lowest_scorer = min(runs, key=runs.get)

print("Lowest Scorer:", lowest_scorer, "(", runs[lowest_scorer], ")", sep="")

# 4. Calculate total runs scored
total_runs = sum(runs.values())

print("Total Tournament Runs:", total_runs)

# 5. Create a list of players scoring below 400
below_400 = []

for player, score in runs.items():
    if score < 400:
        below_400.append(player)

print("Players Scoring Below 400:", below_400)

# 6. Count players scoring between 400 and 600 runs
count = 0

for score in runs.values():
    if 400 <= score <= 600:
        count += 1

print("Players Between 400 and 600 Runs:", count)
