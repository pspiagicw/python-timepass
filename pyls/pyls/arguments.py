import argparse


def parse_arguments()->'Namespace':
    """ This method retures the namespace object after parsing arguments"""
    parser = argparse.ArgumentParser(description='Pure python clone of ls command')
    parser.add_argument('directory',metavar='Directory',default='.',help='The directory name to print the contents on.',nargs='?',type=str)
    parser.add_argument('--all','-A',help='If given all files including hidden files are shown',action='store_const',const=True)
    parser.add_argument('--long','-L',help='If given all files are printed in long form',action='store_const',const=True)
    return parser.parse_args()


