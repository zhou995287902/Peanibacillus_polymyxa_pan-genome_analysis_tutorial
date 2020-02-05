## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-04
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

import sys

def get_Protein_id(file_name):
	Protein_id_dict = {}
	strain_name = file_name.split('/')[-1].split('_')[0]
	with open(file_name,'r') as read_file:
		for line in read_file:
			if line.startswith('>'):
				Protein_id = line.split(' ')[0].replace('>','')
				Protein_id_dict[Protein_id] = strain_name

	return Protein_id_dict

if __name__ == '__main__':
	for each_file in sys.argv[1:]:
		Protein_id_dict = get_Protein_id(each_file)
		for k,v in Protein_id_dict.items():
			print(f'{v}\t{k}')
