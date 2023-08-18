with open('day') as f: txt = f.read()

# Split the input into distinct elves.
elves = txt.split('\n\n')[:-1]

# For each of the elves, split the food they are carrying and add them together.
elves = [sum([int(food_calories) for food_calories in elf.splitlines()]) for elf in elves]

# Part 1
print(sorted(elves, reverse=True)[0])

# Part 2
print(sum(sorted(elves, reverse=True)[0:3]))
