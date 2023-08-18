with open('day') as f: txt = f.read()

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

score_1 = 0
score_2 = 0

rugsacks = txt.splitlines()

for elf in range(0, len(rugsacks), 3):
    # Part 1
    for sack in rugsacks[elf:elf+3]:
        for item in sack[:len(sack) // 2]:
            if item in sack[len(sack) // 2:]:
                score_1 += priority.index(item) + 1
                break
    
    for item in rugsacks[elf]:
        if item in rugsacks[elf + 1] and item in rugsacks[elf + 2]:
            score_2 += priority.index(item) + 1
            break

# Part 1
print(score_1)

# Part 2
print(score_2)
