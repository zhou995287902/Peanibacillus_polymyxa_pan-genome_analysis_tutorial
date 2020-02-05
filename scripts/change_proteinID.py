## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-16
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-


## use command
## python change_proteinID.py Fusaricidin_add_gene_id.table /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/genomic_genebank/*.tab > Fusaricidin_add_gene_id_and_proteinID.table

import sys

def get_locus_to_proteinID(tab_file):
	global locus_protein
	with open(tab_file,'r') as read_file:
		for line in read_file:
			col_list = line.split('\t')
			locus_id = col_list[3]
			protein_id = col_list[4]
			locus_protein[locus_id] = protein_id


def get_locusID(file_name,locus_protein):
	with open(file_name,'r') as read_file:
		# print(locus_protein)
		for line in read_file:
			col_list = line.strip().split('\t')
			locus_id = col_list[2]
			print(f'{line.strip()}\t{locus_protein[locus_id]}')


if __name__ == '__main__':
	locus_protein = {}
	for each_file in sys.argv[2:]:
		# print(each_file)
		get_locus_to_proteinID(each_file)
	# print(locus_protein)
	get_locusID(sys.argv[1],locus_protein)
