with open('day') as f: txt = f.read()

matches = txt.splitlines()

# The metric to score against.
# A, B, and C always represent the opponent's hand.
# X, Y, and Z represent either the player's hand, or the player's match outcome.
metric = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2,
}

# Scores all of the matches based on the strategy provided.
# Opponent's hand is A for Rock, B for Paper or C for scissors.
# The metric for X, Y and Z depends on the strategy.
#
# Rock scores 1, Paper scores 2, Scissors scores 3.
# The player also gains 0 points for losing, 3 points for a draw, and 6 points for winning.
def score(matches, strategy):
    score = 0
    for match in matches:
        opponent, player = metric[match[0]], metric[match[2]]
        score += strategy(opponent, player)
    
    return score


# The metric represents the player's hand: X is for Rock, Y for Paper, and Z for Scissors.
def strategy_a(opponent, player_hand):
    
    # Add the value of the player's hand
    score = player_hand + 1    # Plus 1 since the metric is zero indexed
    
    # Add the value of the outcome.
    # 0 if the player's hand type is the one after the opponents in the metric list,
    # 3 if it is the same, or 6 otherwise (if it's a win).
    score += 3 * (0 if (player_hand + 1) % 3 == opponent else 1 if player_hand == opponent else 2)
    
    return score


# The metric represents the match outcome for the player: X is for loss, Y for draw, and Z for win.
def strategy_b(opponent, player_outcome):
    
    # Add the value of the outcome
    score = 3 * player_outcome
    
    # Add the value of the player's hand.
    # The player's hand will either be the hand before, on, or after the opponents,
    # depending on the outcome.
    score += (opponent + player_outcome - 1) % 3 + 1
    
    return score


# Part 1
print(score(matches, strategy_a))

# Part 2
print(score(matches, strategy_b))
