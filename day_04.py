with open('day') as f: txt = f.read()

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

score_1 = 0
score_2 = 0

for pair in txt.splitlines():
    left, right = pair.split(',')
    left = left.split('-')
    right = right.split('-')

    # Part 1
    if int(left[0]) <= int(right[0]) and int(left[1]) >= int(right[1]): score_1 += 1
    elif int(left[0]) >= int(right[0]) and int(left[1]) <= int(right[1]): score_1 += 1
    
    # Part 2
    if int(right[0]) <= int(left[1]) and int(right[1]) >= int(left[1]): score_2 += 1
    elif int(left[0]) <= int(right[1]) and int(left[1]) >= int(right[1]): score_2 += 1


# Part 1
print(score_1)

# Part 2
print(score_2)
