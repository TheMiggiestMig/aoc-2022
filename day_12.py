with open('day') as f: txt = f.read()


class Node:
    
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = parent
    
    def __eq__(self, test):
        if isinstance(test, Node):
            return (self.x, self.y) == (test.x, test.y)
        elif len(test) == 2:
            return (self.x, self.y) == (test[0], test[1])
        else:
            return NotImplemented
    
    def __repr__(self):
        return f"Node: {(self.x, self.y)}"
    
    def get_mapped_lvl(self, grid):
        return grid[self.y][self.x]
    
    def get_distance(self, node):
        if isinstance(node, Node):
            return abs(node.x - self.x) + abs(node.y - self.y)
        else:
            return abs(node[0] - self.x) + abs(node[1] - self.y)
    
    @classmethod
    def search_mapped(cls, search, grid):
        for y, line in enumerate(grid):
            for x, value in enumerate(line):
                if search == value:
                    return Node(x, y)
    
    @classmethod
    def get_mapped(cls, coords, grid):
        if (coords[1] >= 0 and coords[1] < len(grid)
            and coords[0] >= 0 and coords[0] < len(grid[0])):
                
            node = Node(coords[0], coords[1])
            return (node, grid[node.y][node.x])
        else:
            return None

def generate_terrain():
    return txt.splitlines()

def is_traversable(curr_lvl, check_lvl, backtrack=False):
    if curr_lvl == 'S': curr_lvl = chr(ord('a') - 1)
    if curr_lvl == 'E': curr_lvl = chr(ord('z') + 1)
    if check_lvl == 'S': check_lvl = chr(ord('a') - 1)
    if check_lvl == 'E': check_lvl = chr(ord('z') + 1)
    
    if not backtrack:
        return True if ord(check_lvl) - ord(curr_lvl) <= 1 else False
    else:
        return True if ord(curr_lvl) - ord(check_lvl) <= 1 else False
        
    
# Yay A*!
def find_path(terrain, start_node, end_node=None, a_star=True, target='E', backtrack=False):
    open_list = [start_node]
    closed_list = []
    
    while len(open_list):
        current_node_index = 0
        current_node = open_list[current_node_index]
        
        # Find the open node with the lowest current f value
        for i, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_node_index = i
        
        # Move the current node to the closed list
        open_list.pop(current_node_index)
        closed_list.append(current_node)
        
        # Check if we've reached the goal
        if (end_node and current_node == end_node) or (current_node.get_mapped_lvl(terrain) == target):
            
            # Back track the path to the start_node
            path = []
            while current_node.parent:
                path.append(current_node)
                current_node = current_node.parent
            
            return path[::-1] # Reverse the path since it was backtracked
        
        # We're not at the end yet, keep searching.
        else:
            # Check the neighbors
            neighbors = []
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for direction in directions:
                neighbor = Node.get_mapped((current_node.x + direction[0], current_node.y + direction[1]), terrain)
                
                if neighbor:
                    neighbor_node, neighbor_lvl = neighbor
                    
                    if neighbor_node in open_list:
                        continue
                
                    if neighbor_node in closed_list:
                        continue
                    
                    if is_traversable(current_node.get_mapped_lvl(terrain), neighbor_lvl, backtrack):
                        neighbor_node.g = current_node.g + 1
                        neighbor_node.h = neighbor_node.get_distance(end_node) if a_star else 0
                        neighbor_node.f = neighbor_node.g + neighbor_node.h
                        neighbor_node.parent = current_node
                        open_list.append(neighbor_node)
    
#Part 1
terrain = generate_terrain()
print(len(find_path(terrain, Node.search_mapped('S', terrain), Node.search_mapped('E', terrain))))

#Part 2
terrain = generate_terrain()
print(len(find_path(terrain, Node.search_mapped('E', terrain), target='a', a_star=False, backtrack=True)))
