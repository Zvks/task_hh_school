
from collections import deque, defaultdict

def min_steps_to_last_island(islands):
    n = len(islands)
    if n == 1:
        return 0  
    

    continent_map = defaultdict(list)
    for i in range(n):
        continent_map[islands[i]].append(i)
    

    queue = deque([0])  
    visited = set([0])  
    steps = 0
    
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            
            # Check if we've reached the last island
            if current == n - 1:
                return steps
            
            # Check the neighboring islands
            neighbors = []
            if current > 0:
                neighbors.append(current - 1)  # Left neighbor
            if current < n - 1:
                neighbors.append(current + 1)  # Right neighbor
            
            # Check teleportation to other islands in the same continent
            if islands[current] in continent_map:
                neighbors.extend(continent_map[islands[current]])
                # Clear the record for this continent to prevent further portal use
                del continent_map[islands[current]]
            
            # Go through neighbors and enqueue them if not visited
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        steps += 1  # Increment step count after processing all nodes at current level
    
    return -1  # If we never reach the last island (shouldn't happen in valid input)


islands = list(map(int, input().strip().split()))
print(min_steps_to_last_island(islands))
