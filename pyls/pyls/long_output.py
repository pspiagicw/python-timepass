import os
import stat
import datetime
import math

def generate_output_long(directory:str=',')->list:
    output = list()
    for f in os.listdir(directory):
        file_stat = os.stat(os.path.abspath(f))
        file_mode = stat.filemode(file_stat.st_mode)
        size = file_stat.st_size
        most_recent_accesed = datetime.datetime.utcfromtimestamp(file_stat.st_atime).strftime('%H:%M')
        file_stat_string = '\t'.join([file_mode,str(math.ceil(size/(1024))),most_recent_accesed,f])
        output.append(file_stat_string)
    return output
