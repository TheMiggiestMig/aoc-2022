with open('day') as f: txt = f.read()

# [!] We're lazy, so we'll use eval. Sanitize first!
for char in txt:
    if char not in '0123456789,[]\n':
        print("Unexpected bytes found!")
        exit()


def compare(left, right):
    # If both left and right are integers, compare them both.
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        if left > right:
            return 1
        else:
            return 0
    # If both left and right are lists, iterate through their components.
    elif type(left) == list and type(right) == list:
        result = 0
        index = 0
        
        while not result:
            # Check if any of the lists have run out.
            if index >= len(left) and index >= len(right):
                return 0
            elif index >= len(left):
                return -1
            elif index >= len(right):
                return 1
                
            # If both lists have items, then compare the items.
            result = compare(left[index], right[index])
            index += 1
        
        return result
    
    # Only one of these items is a list. Wrap the other in a list and compare.
    else:
        if type(left) == int:
            return compare([left], right)
        else:
            return compare(left, [right])
    

# Part 1
correct_pairs = []
packet_pairs = txt.split('\n\n')
for index, packet_pair in enumerate(packet_pairs):
    packet_1, packet_2 = packet_pair.splitlines()
    packet_1 = eval(packet_1)
    packet_2 = eval(packet_2)
    
    if compare(packet_1, packet_2) == -1:
        correct_pairs.append(index + 1)

print(sum(correct_pairs))


# Part 2
packets = [eval(line) for line in txt.splitlines() if line != ""]
packets.append([[2]])
packets.append([[6]])

from functools import cmp_to_key
sorted_packets = sorted(packets, key=cmp_to_key(compare))
print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
