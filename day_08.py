with open("day") as f: txt = f.read()

# Build the forest
forest = txt.splitlines()
hidden = 0
score_1 = 0
score_2 = 0

# Scan the trees (excluding the trees at the edge)
# Part 1
for y in range(1, len(forest)-1):
    for x in range(1, len(forest[y])-1):
        height = forest[y][x]
        if max([tree[x] for tree in forest[:y]]) < height or max([tree[x] for tree in forest[y + 1:]]) < height: continue
        if max([tree for tree in forest[y][:x]]) < height or max([tree for tree in forest[y][x + 1:]]) < height: continue
        
        hidden += 1
score_1 = (len(forest) * len(forest[0])) - hidden

# Part 2
# Check how many trees along a line of trees can be seen from a given height
def view(height, line):
    score = 0
    
    for tree in line:
        score += 1
        if int(tree) >= int(height): return score
    
    return score
    
for y in range(1, len(forest) - 1):
    for x in range(1, len(forest[y]) - 1):
        height = forest[y][x]
        score = 1
        
        score *= view(height, forest[y][:x][::-1])
        score *= view(height, forest[y][x + 1:])
        score *= view(height, ''.join([row[x] for row in forest[:y]])[::-1])
        score *= view(height, ''.join([row[x] for row in forest[y + 1:]]))
        
        score_2 = max(score_2, score)

# Part 1
print(score_1)

# Part 2
print(score_2)
