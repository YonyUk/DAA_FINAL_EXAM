import heapq
import os

os.system('cls')

def dijkstra(graph, start_node):
    # Initialize distances dictionary
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    streets_min = { node: float('infinity') if node!= start_node else 0  for node in graph}
    
    # Create priority queue
    pq = [(0, start_node , 0 )]
    
    while pq:
        current_distance, current_node , streets_min_queue = heapq.heappop(pq)
        
        # Skip if we've already found shorter path
        if current_distance > distances[current_node]:
            continue
        
        # Process neighbors
        for neighbor, weight in enumerate(graph[current_node]):
            distance = current_distance + weight
            
            # Update distance if it's less than what we previously knew
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                streets_min[neighbor] = streets_min_queue + 1 # as dijkstra discover in BFS search , it and update if found path is lower than actual , we always have a minimum street path
                heapq.heappush( pq , ( distance , neighbor , streets_min[neighbor] ) )
    
    return streets_min

def solve_using_dijkstra(graph):
    
    output = {}
    for key in graph: # O( |V| * |E|log|V| ),  whose worst case is acotated by O( |V|^3 * log |V|) and best case |E| = |V|-1 => O( |V|^2 *l og|V| )

        start_node = key
        street_min = dijkstra(graph, start_node)
        
        output[start_node] = [ street_min[item] for item in street_min]

    # for i in output:
    #     print( f'{i}: ', output[i])
    
    return output
    