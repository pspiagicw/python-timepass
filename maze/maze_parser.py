
from undirected import maze_solver
import pprint
import collections
def readfile(filename):
    file_contents = ""
    with open(filename,'r') as file:
        file_contents = file.readlines()
    return file_contents

def convert_to_matrix(file_contents):
    maze_matrix = [ list(line)[:-1] for line in file_contents ]
    return maze_matrix
def find_start_end(maze_matrix):
    start = (None,None)
    end = (None,None)
    for i in range(len(maze_matrix)):
        for j in range(len(maze_matrix[0])):
                if maze_matrix[i][j] == '?':
                    start = (i,j)
                if maze_matrix[i][j] == 'x':
                    end = (i,j)
    return start,end
def convert_to_adjency_list(maze_matrix,start,end):
    current_node = start
    adjency_list = collections.defaultdict(lambda : [] )
    node_list = find_neighbors(maze_matrix,current_node)
    node_explored = set()
    while node_list:
        if current_node not in node_explored:
            neighbor_points = find_neighbors(maze_matrix,current_node)
            node_list.extend(neighbor_points)
            for point in neighbor_points:
                    adjency_list[current_node] = adjency_list[current_node] + [point]
            node_explored.add(current_node)
            current_node = node_list.pop()
        else:
            current_node = node_list.pop()
    return adjency_list
def find_neighbors(maze_matrix,point):
    x = point[0]
    y = point[1]
    neighbor_points = list()
    for point_x, point_y in ( (i,j) for i in range(len(maze_matrix)) for j in range(len(maze_matrix[0])) ):
        if (abs(point_x - x) <=1 ) and (abs(point_y - y ) <= 1 ) and (abs(point_x - x) != abs(point_y -y )):
            neighbor_points.append((point_x,point_y))
    neighbor_points =  list(filter(lambda x: maze_matrix[x[0]][x[1]] != '#',neighbor_points))
    return neighbor_points
                
def parse_file(filename):
    contents = readfile(filename)
    matrix = convert_to_matrix(contents)
    start , end = find_start_end(matrix)
    adjency_list = convert_to_adjency_list(matrix,start,end)
    return adjency_list , start , end
def print_graph(explored_nodes,maze_matrix,start,path):
    for node in explored_nodes:
        i , j = node
        if node != start:
            maze_matrix[i][j] = '-'
        if node in path:
            maze_matrix[i][j] = '+'
    maze_matrix = [ ''.join(row)+'\n' for row in maze_matrix ]
    with open('graph.txt','w') as graphfile:
        graphfile.writelines(maze_matrix)

def main(file,algorithm):
    graph , start , end= parse_file(file)
    result , nodes , path= maze_solver.astar_solver(graph,start,end)
    if algorithm == 'bfs':
        result , nodes , path= maze_solver.bfs_solver(graph,start,end)
    elif algorithm == 'dfs':
        result , nodes , path= maze_solver.dfs_solver(graph,start,end)
    elif algorithm == 'greedy':
        result , nodes , path= maze_solver.greedy_solver(graph,start,end)

    matrix = convert_to_matrix(readfile('example.txt'))
    print_graph(nodes,matrix,start,path)
    print(result)



