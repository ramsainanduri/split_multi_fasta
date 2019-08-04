import os
import sys
#Reading user inut file
in_file = sys.argv[1]
with open(in_file, "r") as fa:
    lines=fa.read().split('>')
    lines = lines[1:]
    lines=['>'+ seq for seq in lines]
    for name in lines:
        file_name=name.split('\n')[0][1:]  #Extracting sequence Id to use it for file name
        out_file=open(file_name+".fasta", "w")
        out_file.write(name)
        out_file.close()