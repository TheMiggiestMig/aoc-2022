with open('day') as f: txt = f.read()

lower_limit = -1
drop_x = 500

lines = []

# Find the lower limit
for line in txt.splitlines():
    coords = [tuple([int(pt) for pt in coord.split(',')]) for coord in line.split(' -> ')]
    lines.append(coords)
    
    for coord in coords:
        if coord[1] > lower_limit:
            lower_limit = coord[1]
            
lower_limit += 2        # Account for the gap as per Part 2


# Map the surface blocks
def generate_surfaces():
    surface_map = [{} for y in range(lower_limit)]
    
    for line in lines:
        current_coord = line[0]
        
        for next_coord in line[1:]:
            # Check if the coordinates indicate a change in y value
            if current_coord[0] == next_coord[0]:
                x = current_coord[0]
                start_y = min(current_coord[1], next_coord[1])
                end_y = max(current_coord[1], next_coord[1])
                
                for y in range(start_y, end_y):
                    surface_map[y][x] = "#"
            
            else:
                y = current_coord[1]
                start_x = min(current_coord[0], next_coord[0])
                end_x = max(current_coord[0], next_coord[0])
                
                for x in range(start_x, end_x + 1):
                    surface_map[y][x] = "#"
            
            current_coord = next_coord
    
    return surface_map


# Drop some sand
def drop(surface, bottomless=False):
    x = drop_x
    y = 0
    
    while True:
        # We hit the y limit
        if y + 1 == lower_limit:
            if bottomless:
                return False
            else:
                surface[y][x] = 'O'
                return True
        
        # Check for what's under the current line
        next_line = surface[y + 1].keys()
        if x in next_line:
            if x - 1 not in next_line:
                x -= 1
            elif x + 1 not in next_line:
                x += 1
            else:
                # Check if we hit the top
                if y == 0:
                    return False
                
                surface[y][x] = 'O'
                return True
        y += 1


# Render the map (for debugging, also because it looks cool)
def render(surface):
    # Find the left and right bounds
    x_values = []
    [x_values.extend(list(line.keys())) for line in surface]
    
    min_x = min(x_values)
    max_x = max(x_values) + 1
    
    # Render the first line differently, based on the drop point
    line = surface[0]
    rendered_line = ['.'] * (max_x - min_x)
    for x, value in line.items():
        rendered_line[x - min_x] = value
    rendered_line[drop_x - min_x] = '+'
    
    print(''.join(rendered_line))
    
    # Render the rest of the lines line
    for line in surface[1:]:
        rendered_line = ['.'] * (max_x - min_x)
        for x, value in line.items():
            rendered_line[x - min_x] = value
        
        print(''.join(rendered_line))

# Part 1
surface = generate_surfaces()
count = 0
while drop(surface, True): count += 1
# render(surface)
print(count)

# Part 2
surface = generate_surfaces()
count = 1       # For the last sand drop
while drop(surface): count += 1
print(count)
