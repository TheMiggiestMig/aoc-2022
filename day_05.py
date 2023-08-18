with open('day') as f: txt = f.read()

txt = txt.splitlines()

# Work out the number of towers. Each tower is 3 characters wide with a space in between.
towers = []
for i in range((len(txt[0]) // 4)+1): towers.append('')

instructions = []

# Construct the towers
for i, line in enumerate(txt):

	# If the line is empty, the instructions will be following.
	if line == "":
		instructions = txt[i+1:]
		break

	# We only care about the lines with the format '[?]', since the numbers on their own are just the tower labels.
	if '[' in line:
	    for t in range(0, len(line), 4):
	        towers[t // 4] += line[t+1] if line[t+1] != " " else ''

# Flip the towers
for i, tower in enumerate(towers): towers[i] = tower[::-1]

solve_1 = towers.copy()
solve_2 = towers.copy()

# Follow the instructions
# Part 1
for line in instructions:
	line = line.split(" ")

	for i in range(int(line[1])):
		solve_1[int(line[5])-1] += solve_1[int(line[3])-1][-1]
		solve_1[int(line[3])-1] = solve_1[int(line[3])-1][:-1]

# Part 2
for line in instructions:
	line = line.split(" ")
	solve_2[int(line[5])-1] += solve_2[int(line[3])-1][int(line[1]) * -1:]
	solve_2[int(line[3])-1] = solve_2[int(line[3])-1][:int(line[1]) * -1]

# Part 1
print(''.join([tower[-1] for tower in solve_1]))

# Part 2
print(''.join([tower[-1] for tower in solve_2]))
