# Find clusters in the given graph using adjacency list and depth first search
# Use the number of clusters to calculate the number of roads
# calculate final cost using no. of roads, cost of road, no. of cities, and cost of single library

import sys
from collections import deque
from functools import reduce  
                

def roadsAndLibraries(n, c_lib, c_road, cities):
        if c_lib <= c_road:
            return c_lib * n
        
        
        def num_disconnected(roads):
            result = 0
            visited = set()
            length = len(roads)
            
            for i in range(length):
                if i not in visited:
                    stack = deque([])
                    stack.append(i)
                    while len(stack):
                        cur = stack.pop()
                        visited.add(cur)
                        for neighbor in roads[cur]:
                            if neighbor not in visited:
                                stack.append(neighbor)
                    result +=1
            return result
        
        clusters = num_disconnected(cities)
        
        return (c_road * (n - clusters)) + c_lib * clusters
        

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = [list() for _ in range(n)]
        for cities_i in range(m):
           cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
           cities_t = [c-1 for c in cities_t]
           cities_t.sort() 
           city1, city2 = cities_t
           cities[city1].append(city2)
           cities[city2].append(city1)
        result = roadsAndLibraries2(n, c_lib, c_road, cities)
        print(result)
