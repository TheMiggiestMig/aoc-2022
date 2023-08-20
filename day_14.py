with open('day') as f: txt = f.read()

surfaces = []
left_bound = -1
right_bound = -1
bottom_bound = -1
drop_x = 500

walls = []


# Map the walls
for line in txt.splitlines():
    coords = [tuple([int(pt) for pt in coord.split(',')]) for coord in line.split(' -> ')]
    walls.append(coords)
    
    # Determine the space bounds
    for coord in coords:
        if coord[0] < left_bound or left_bound == -1:
            left_bound = coord[0]
        elif coord[0] + 1 > right_bound:
            right_bound = coord[0] + 1
        
        if coord[1] > bottom_bound:
            bottom_bound = coord[1]
    
surfaces = [['.'] * (right_bound - left_bound) for y in range(bottom_bound + 1)]
for wall in walls:
    current_coord = wall[0]
    
    for coord in range(1, len(wall)):
        next_coord = wall[coord]
        start_x = min(current_coord[0], next_coord[0])
        
        for x in range(abs(next_coord[0] - current_coord[0]) + 1):
            start_y = min(current_coord[1], next_coord[1])
            
            for y in range(abs(next_coord[1] - current_coord[1]) + 1):
                surfaces[start_y + y][start_x + x - left_bound] = '#'
                
        current_coord = next_coord

def drop(coord, surface):
    x, y = coord
    
    while True:
        #print(''.join(surfaces[y][:x]) + '?' + ''.join(surfaces[y][x + 1:]))
        y += 1
        if y > bottom_bound: return False
        if surface[y][x - left_bound] != '.':
            if x - 1 < left_bound: return False
            if surface[y][x - left_bound - 1] == '.':
                x -= 1
                continue
            
            if x + 1 > right_bound - 1: return False
            if surface[y][x - left_bound + 1] == '.':
                x += 1
                continue
            break
                
    surface[y - 1][x - left_bound] = 'O'
    return True


def render_surface(surface):
    [print(''.join(surface)) for surface in surfaces]


# Part 1
count = 0
while drop((drop_x, 0), surfaces):
    count += 1
render_surface(surfaces)
print(count)
