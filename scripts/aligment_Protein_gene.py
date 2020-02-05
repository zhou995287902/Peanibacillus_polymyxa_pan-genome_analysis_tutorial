## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-04
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

import sys

def get_query_ref_ID(file_name):
	with open(file_name,'r')as f:
		qurey_Protein_ref_protein = {}
		for line in f:
			col_list = line.split('\t')
			query_protein_id = col_list[0].strip()
			ref_protein_id = col_list[1] 
			identity = float(col_list[2].strip())
			Score = float(col_list[-1].strip())
			if identity < 80:
				continue
			if query_protein_id not in qurey_Protein_ref_protein :
				qurey_Protein_ref_protein[query_protein_id] = ref_protein_id
				last_score = Score
			else:
				if Score > last_score:
					qurey_Protein_ref_protein[query_protein_id] = ref_protein_id

	return qurey_Protein_ref_protein


def get_protein_id_name(file_name):
	strain_name_protein_id = {}
	with open(file_name,'r') as read_file:
		for line in read_file:
			col_list = line.strip().split('\t')
			Protein_id = col_list[1]
			strain_name = col_list[0]
			strain_name_protein_id[Protein_id] = strain_name
	return strain_name_protein_id


if __name__ == '__main__':
	qurey_Protein_ref_protein = get_query_ref_ID(sys.argv[1])
	strain_name_protein_id = get_protein_id_name(sys.argv[2])
	# print(qurey_Protein_ref_protein,strain_name_protein_id)
	for k,v in qurey_Protein_ref_protein.items():
		print('{}\t{}\t{}'.format(strain_name_protein_id[k],k,strain_name_protein_id[v].split('.')[0]))
