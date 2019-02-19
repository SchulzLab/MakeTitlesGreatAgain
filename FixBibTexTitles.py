#!/usr/bin/python
#This script outputs all title lines of a bibtex file with two {{ }} brackets around
#it to fix capitalizatoin of most latex bibliography styles


import sys
import re


#read in fasta file
if len(sys.argv) < 2:
        print "usage python FixBibTexTitles.py file.bib > newFile.bib"
else :

        file=open(sys.argv[1],'r')

        
        for line in file:
        	line=line.strip()
        	#if this is a title line with {} brackets around the title
        	if re.search("\s*title\s*=",line) and re.search("\{*\}",line):
        		#split on the { and } brackets and output with double {{ }}
        		elems=re.split("{*}*",line)
        		print "".join([elems[0],"{{",elems[1],"}}",elems[2]])
        	else:
        		print line
                
                
