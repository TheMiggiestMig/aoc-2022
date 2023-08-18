with open('day') as f: txt = f.read()

cycle = 0
signal = 1

crt = { 'width': 40, 'height': 6, 'screen': ["" for i in range(6)] }

checks = []

# Read each operation
for opline in txt.splitlines():
    tick = 0
    gain = 0
    
    # Split into opcodes
    op = opline.split(" ")
    
    if len(op) - 1:
        gain = int(op[1])
        tick = 2
    else:
        tick = 1
    
    # Delay based on tick requirement and check for key cycles
    while tick:
        tick -= 1
        cycle += 1
        
        # Part 1
        if not (cycle - 20) % 40:
            checks.append(signal * cycle)
        
        # Part 2 - Drawing
        row_num = (cycle - 1) // 40
        row = crt['screen'][row_num]
        
        x = (cycle - 1) % 40
        sprite = signal
        crt['screen'][row_num] = row[:x] + ('#' if x >= sprite - 1 and x <= sprite + 1 else '.') + row[x + 1:]
        

    signal += gain

# Part 1
print(sum(checks))

# Part 2
[print(row) for row in crt['screen']]
