import argparse
from undirected.maze_parser import  main


def parse_argument():
    parser = argparse.ArgumentParser(description='Maze Solver',prog='maze_parser')
    parser.add_argument('file',help='The file to parse',type=str)
    parser.add_argument('-a','--algorithm',help='The algorithm to use to solve the maze',type=str,required=False,default='astar',action='store')
    return parser.parse_args()


def start():
    parsed_arguments = parse_argument()
    algorithm = parsed_arguments.algorithm
    file = parsed_arguments.file
    main(file,algorithm)
