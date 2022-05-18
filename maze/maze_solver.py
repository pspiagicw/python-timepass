import functools
# def bfs_solver(adjency_list , start , end):
#     node_explored = list()
#     queue = [start]
#     while queue:
#         current_node = queue.pop(0)
#         if current_node == end:
#             return True , node_explored
#         if current_node not in node_explored:
#             node_explored.append(current_node)
#             for node in adjency_list[current_node]:
#                 if node not in node_explored:
#                     queue.append(node)

#     return False , node_explored
    
def bfs_solver(adjency_list , start , end):
    node_explored = list()
    queue = [(start ,[start])]
    while queue:
        current_node = queue.pop(0)
        if current_node[0] == end:
            return True , node_explored , current_node[1]
        if current_node[0] not in node_explored:
            node_explored.append(current_node[0])
            for node in adjency_list[current_node[0]]:
                if node not in node_explored:
                    queue.append((node,current_node[1] + [node]))

    return False , node_explored , list()
def dfs_solver(adjency_list , start , end):
    node_explored = list()
    queue = [(start ,[start])]
    while queue:
        current_node = queue.pop()
        if current_node[0] == end:
            return True , node_explored , current_node[1]
        if current_node[0] not in node_explored:
            node_explored.append(current_node[0])
            for node in adjency_list[current_node[0]]:
                if node not in node_explored:
                    queue.append((node,current_node[1] + [node]))

    return False , node_explored , list()
# def dfs_solver(adjency_list , start , end):
#     node_explored = list()
#     queue = [start]
#     while queue:
#         current_node = queue.pop()
#         if current_node == end:
#             return True , node_explored
#         if current_node not in node_explored:
#             node_explored.append(current_node)
#             for node in adjency_list[current_node]:
#                 if node not in node_explored:
#                     queue.append(node)

#     return False , node_explored

# def greedy_solver(adjency_list , start , end):
#     node_explored = list()
#     queue = [start]
#     while queue:
#         current_node = queue.pop()
#         if current_node == end:
#             return True , node_explored
#         if current_node not in node_explored:
#             node_explored.append(current_node)
#             neighbours = adjency_list[current_node]
#             sorted(neighbours,key=functools.partial(manhattan_distance,end=end))
#             queue.extend(filter(lambda x:x not in node_explored,neighbours))
            

#             # for node in adjency_list[current_node]:
#             #     if node not in node_explored:
#             #         queue.append(node)

#     return False , node_explored

import math
def manhattan_distance(node,end):
    return math.sqrt(abs(node[0] -end[0])**2 + abs(node[1] - end[1])**2)



# def a_star_solver(adjency_list , start , end):



def greedy_solver(adjency_list , start , end):
    node_explored = list()
    queue = [(start ,[start])]
    while queue:
        current_node = queue.pop()
        if current_node[0] == end:
            return True , node_explored , current_node[1]
        if current_node[0] not in node_explored:
            node_explored.append(current_node[0])
            neighbors = list()
            for node in adjency_list[current_node[0]]:
                if node not in node_explored:
                    neighbors.append((node,current_node[1] + [node]))
            sorted_neighbors = list()
            while neighbors:
                least_cost = float('inf')
                least_index = 0
                for i in range(len(neighbors)):
                    if manhattan_distance(neighbors[i][0],end) < least_cost:
                        least_index = i
                        least_cost = manhattan_distance(neighbors[i][0],end)
                sorted_neighbors.append(neighbors.pop(i))
            queue.extend(sorted_neighbors[::-1])
    return False , node_explored , list()
def astar_solver(adjency_list , start , end):
    node_explored = list()
    queue = [(start ,[start],0)]
    while queue:
        current_node = queue.pop()
        if current_node[0] == end:
            return True , node_explored , current_node[1]
        if current_node[0] not in node_explored:
            node_explored.append(current_node[0])
            neighbors = list()
            for node in adjency_list[current_node[0]]:
                if node not in node_explored:
                    neighbors.append((node,current_node[1] + [node],current_node[2] + 1))
            sorted_neighbors = list()
            while neighbors:
                least_cost = float('inf')
                least_index = 0
                for i in range(len(neighbors)):
                    if manhattan_distance(neighbors[i][0],end) + neighbors[i][2] < least_cost:
                        least_index = i
                        least_cost = manhattan_distance(neighbors[i][0]+neighbors[i][2],end)
                sorted_neighbors.append(neighbors.pop(i))
            queue.extend(sorted_neighbors[::-1])
    return False , node_explored , list()
