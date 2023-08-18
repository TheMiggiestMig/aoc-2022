with open('day') as f: txt = f.read()

seg = [[0,0] for i in range(10)] # seg[0] is 'head', seg[9] (aka. seg[-1]) is 'tail'.

part_1_marks = ['0,0']
part_2_marks = ['0,0']

for move in txt.splitlines():
    direction, amount = move.split(' ')
    
    axis = 0 if direction in 'RL' else 1
    speed = 1 if direction in 'RU' else -1
    
    
    for n in range(int(amount)):
        head = 0
        seg[head][axis] += speed
        
        # Check separation from the next segment
        for i in range(1, len(seg)):
            diffx = seg[head][0] - seg[i][0]
            diffy = seg[head][1] - seg[i][1]
            dist2 = diffx**2 + diffy**2
            
            if dist2 > 2:
                seg[i][0] += diffx // abs(diffx) if diffx else 0
                seg[i][1] += diffy // abs(diffy) if diffy else 0
                
                if i == 1: part_1_marks.append(f"{seg[i][0]},{seg[i][1]}")
                if i == 9: part_2_marks.append(f"{seg[i][0]},{seg[i][1]}")
            head = i
            
# Part 1
print(len(set(part_1_marks)))

# Part 2
print(len(set(part_2_marks)))
