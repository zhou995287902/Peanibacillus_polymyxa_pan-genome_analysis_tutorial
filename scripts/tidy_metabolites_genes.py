## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-30
# encoding='utf-8'

import sys
## use command
## python tidy_metabolites_genes.py get_metabolites_and_genes.table > get_metabolites_and_genes.tidy.table

with open(sys.argv[1],'r')as read_file:
	lines = read_file.readlines()
	metabolites_type = []
	for line in lines:
		col_list = line.strip().split('\t')
		if len(col_list) <= 1:
			continue
		if col_list[1] not in metabolites_type:
			metabolites_type.append(col_list[1])

	for i in metabolites_type:
		for line in lines:
			col_list = line.strip().split('\t')
			if len(col_list) <= 1:
				continue
			if i == col_list[1]:
				print(line.strip())

