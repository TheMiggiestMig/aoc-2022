with open("day") as f: txt = f.read()

# Define a node (file / directory).
def Node(name, parent=None, size=0, is_dir=False):
    return {'name': name, 'parent':parent, 'size':size, 'is_dir':is_dir, 'items':{}}

# Traverse up a directory and update the sizes.
def up(node):
    if node['parent']:
        if node['is_dir']: directory_sizes.append(node['size'])
        node['parent']['size'] += node['size']
        node = node['parent']
    return node

directory_sizes = []  # Used for the challenge.

# Build the file structure.
root = Node('', is_dir=True)
node = root

# Parse the command prompt line-by-line.
for line in txt.splitlines():
    if line[:4] == "$ cd":
        directory = line[5:]
        
        if directory == '..':
            node = up(node)
            
        elif directory == '/': node = root
        else:
            node = node['items'][directory]
    
    elif line[:4] == "dir ":
        node['items'][line[4:]] = Node(line[4:], node, is_dir=True)
    
    elif line[0] == "$":
        continue
    else:
        size, name = line.split(' ')
        node['items'][name] = Node(name, parent=node, size=int(size))
        node['size'] += int(size)

# Directory sizes are calculated when traversing up, so backtrack to root to re-calculate
while node['parent']: node = up(node)
directory_sizes.append(root['size'])

# Part 1
print(sum([d if d < 100000 else 0 for d in sorted(directory_sizes, reverse=True)]))

# Part 2
min_target_size = 30000000 - (70000000 - root['size'])
curr_size = root['size']

for d in sorted(directory_sizes,reverse=True):
    if d < min_target_size: break
    curr_size = d

print(curr_size)
