## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-20
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

## use command
## python tidy_kegg.py ./*/gene_anno.txt|less -S

import sys 

def open_kegg_anno(file_name):
	pathway_ids = {}
	with open(file_name,'r') as read_file:
		lines = read_file.readlines()
		for line in lines[1:]:
			col_list = line.strip().split('\t')
			pathwayid = col_list[5]
			other = '\t'.join(col_list[5:])
			if other not in pathway_ids:
				pathway_ids[other] = 1
			else:
				pathway_ids[other] += 1
	return pathway_ids

if __name__ == '__main__':
	for each_file in sys.argv[1:]:
		pathway_ids = open_kegg_anno(each_file)
		print(each_file)
		for k,v in pathway_ids.items():
			print(f'ko{k}\t{v}')
