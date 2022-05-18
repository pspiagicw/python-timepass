import os
from pyls import arguments
from pyls import long_output


def main():
    """ This is the main which is called when running pyls"""
    # Parse the arguments 
    args = arguments.parse_arguments()
    # Configure Arguments and set corresponding variables
    output = generate_output(args.directory)
    if args.long:
        output = long_output.generate_output_long(args.directory)
    print_output(output,True if args.all else False)

def generate_output(directory:str) -> list:
    """ This generates the normal output.Which is list of files in direcotry"""
    return os.listdir(directory)
def print_output(output_list:list,hidden:bool=False):
    """ This prints the given list on a new line and checks for hidden files"""
    for node in output_list:
        if not node.startswith('.') or hidden:
            print(node)
    
    
