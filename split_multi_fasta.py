import os
import sys
#Reading user inut file
in_file = sys.argv[1]
file_path = os.path.abspath(os.path.dirname(in_file))
try:
	with open(in_file, "r") as fa:
	    lines=fa.read().split('>')
	    lines = lines[1:]
	    lines=['>'+ seq for seq in lines]
	    for name in lines:
	    	#Extracting sequence Id to use it for file name
	        file_name=name.split('\n')[0][1:]  
	        out_file=open(file_path+"/"+file_name+".fasta", "w")
	        out_file.write(name)
	        out_file.close()
	print ("\nSucessfully Split "+os.path.basename(in_file)+" into single fasta files")
except:
	sys.exit("Opps..either file is not present or file format is not correct")