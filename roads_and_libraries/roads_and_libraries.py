# Find clusters in the given graph using adjacency list and depth first search
# Use the number of clusters to calculate the number of roads
# calculate final cost using no. of roads, cost of road, no. of cities, and cost of single library

import sys
from collections import deque
from functools import reduce


def roads_and_libraries(cities_count, cost_library, cost_road, cities_adjacency_list):
    if cost_library <= cost_road:
        return cost_library * cities_count

    def num_disconnected(roads):
        clusters_count = 0
        visited = set()
        length = len(roads)

        for i in range(length):
            # this will only run if current node has not been visited
            if i not in visited:
                # the stack gets declared for every new disjoint set
                stack = deque([])
                stack.append(i)
                # this loop keeps running until a node with no unvisited neighbors is reached
                # add each neighbor to stack if it is not visited
                while len(stack):
                    cur = stack.pop()
                    visited.add(cur)
                    # add each neighbor to stack if it is not visited
                    for neighbor in roads[cur]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                # loop breaks once stack is emptied and we increment cluster count by one
                clusters_count += 1

        return clusters_count

    clusters = num_disconnected(cities_adjacency_list)

    return (cost_road * (cities_count - clusters)) + cost_library * clusters


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = [list() for _ in range(n)]
        for cities_i in range(m):
            cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
            cities_t = [c - 1 for c in cities_t]
            cities_t.sort()
            city1, city2 = cities_t
            cities[city1].append(city2)
            cities[city2].append(city1)
        res = roads_and_libraries(n, c_lib, c_road, cities)
        print(res)
