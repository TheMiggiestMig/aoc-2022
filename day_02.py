with open('day') as f: txt = f.read()

metric = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2,
}

score_1 = 0
score_2 = 0

# For each match, determine the score.
for match in txt.splitlines():
    opponent, player = match[0], match[2]
    
    decider = metric[player]
    
    # Part 1
    score_1 +=  (metric[player] + 1) + 3 * (1 if decider == metric[opponent] else 0 if (decider + 1) % 3 == metric[opponent] else 2)
    
    # Part 2
    score_2 +=  ((metric[opponent] + metric[player] - 1) % 3 + 1) + (3 * (metric[player]))

# Part 1
print(score_1)

# Part 2
print(score_2)
