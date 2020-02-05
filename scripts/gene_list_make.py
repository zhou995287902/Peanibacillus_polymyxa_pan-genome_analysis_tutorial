## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-
import sys
import re 


def get_all_gene_id(file_name):
	global gene_list
	is_True = False
	with open(file_name,'r')as read_file:
		for line in read_file:
			if re.search(r' +gene +.*\d+\.\.\d+',line):
				# print(line)
				is_True = False
			elif re.search(r' +CDS +.*\d+\.\.\d+',line):
				# print(line)
				is_True = True
			if is_True:
				if '/locus_tag=' in line:
					gene_id = line.split('=')[1].strip().strip('"')
				if '/protein_id=' in line :
					protein_id = line.split('=')[1].strip().strip('"')
				# col_list = line.split(' ')

				# print(col_list)
				# protein_id = col_list[3].strip('').split('=')[1]
				# gene_id = col_list[1].strip('').split('=')[1]
				# protein_id = re.search(r'\[protein_id=(.*\.\d)\]',line).group(1)
				# print(protein_id)
				# gene_id = re.search(r'\[locus_tag=(.*)\]',line).group(1)
				# print(protein_id,gene_id)
					gene_list[protein_id] = gene_id

if __name__ == '__main__':
	gene_list = {}
	for file_name in sys.argv[1:]:
		get_all_gene_id(file_name)

	for k,v in gene_list.items():
		print(f'{v}\t{k}')

