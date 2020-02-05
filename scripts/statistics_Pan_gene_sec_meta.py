## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-24
# encoding='utf-8'

import sys

def open_tidy_sec_meta_pan_gene(file_name):
	pan_gene_dict = {}
	with open(file_name,'r')as read_file:
		lines = read_file.readlines()
		row_names = lines[0].strip().split('\t')
		for line in lines[1:]:
			col_list = line.strip().split('\t')
			protein_id = col_list[2]
			pan_gene_dict[protein_id] = {}
			for i in range(6):
				pan_gene_dict[protein_id][row_names[i]] = col_list[i]

	return pan_gene_dict

def open_sec_meta_type_length(file_name):
	meta_type_dict = {}
	with open(file_name,'r') as read_file:
		lines = read_file.readlines()
		row_names = lines[0].strip().split('\t')
		for line in lines[1:]:
			col_list = line.strip().split('\t')
			strain_name = col_list[0] + col_list[1] + col_list[2]
			meta_type_dict[strain_name] = {}
			for i in range(5):
				meta_type_dict[strain_name][row_names[i]] = col_list[i]

	return meta_type_dict


if __name__ == '__main__':
	pan_gene_dict = open_tidy_sec_meta_pan_gene(sys.argv[1])
	meta_type_dict = open_sec_meta_type_length(sys.argv[2])
	# print(len(pan_gene_dict),len(meta_type_dict))
	print('strain_name\tgene_type\tprotein_id\tMeta_Type\tstart\tend\tprotein_seq')
	for pan_gene_dict_value in pan_gene_dict.values():
		for meta_type_dict_value in meta_type_dict.values():
			if pan_gene_dict_value['strain_name'] == meta_type_dict_value['strain_name']:
				if int(pan_gene_dict_value['start']) >= int(meta_type_dict_value['start']) and int(pan_gene_dict_value['end']) <= int(meta_type_dict_value['end']):
					print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(pan_gene_dict_value['strain_name'],pan_gene_dict_value['gene_type'],pan_gene_dict_value['protein_id'],\
						meta_type_dict_value['Type'],pan_gene_dict_value['start'],pan_gene_dict_value['end'],pan_gene_dict_value['protein_seq']))
