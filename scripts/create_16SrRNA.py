## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-
import sys
import os

all_file_names = sys.argv[1:]

write_file = open('14_strain_16SrRNA.fasta','w')
for each_file in all_file_names:
	seq = {}
	with open(each_file,'r') as f:
		for line in f:
			if '>' in line[0]:
				seq_name = line[:16]
				seq[seq_name] = ''
			else:
				seq[seq_name] += line.strip()

	write_file.write('>'+each_file[:-4]+'\n'+seq[seq_name]+'\n')

write_file.close()