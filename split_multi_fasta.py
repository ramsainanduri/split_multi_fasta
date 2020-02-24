import os
import sys
import argparse

#Developer Info
print ("\n*********************************************************************************************************")
print ("* Python script to split multi fasta file into individual file using sequence ids as file names\t\t*")
print ("* Script Developed by\t:\tRam Sai Nanduri\t\t\t\t\t\t\t\t*")
print ("*********************************************************************************************************")
##Argument parser
parser = argparse.ArgumentParser(description="Split multi fasta file into individual files using sequence ids as their file names.")
parser.add_argument("-m", "--multifasta", metavar="multifasta", help="Input multi fasta file", type=str)
parser.add_argument("-v", "--version", help="Program's version", action='version', version='%(prog)s 1.0')
args = parser.parse_args()
#Reading user inut file
in_file = args.multifasta
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
	print ("\nSucessfully splited "+os.path.basename(in_file)+" into single fasta files")
except:
	sys.exit("Opps..either file is not present or file format is not correct")
