with open('day') as f: txt = f.read()

def solve(size):
    for i in range(len(txt)):
    	if len(set(txt[i:i + size])) == size:
    		return (i + size)

# Part 1
print(solve(4))

# Part 2
print(solve(14))
