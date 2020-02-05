## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-12-2
# encoding='utf-8'

## use command
## python filter_nif_gene.py filter_nif_gene.txt /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/genomic_gff/*.gff > nif_gene_structure_add_protein_id.table
import sys
import re

def get_protein_id(file_name):
	gene_id_list = ['nifB','nifH','nifD','nifK','nifE','nifN','nifX','hesA','nifV']
	protein_gene = {}
	with open(file_name,'r') as read_file:
		for line in read_file:
			if '.' in line[0]:
				strain_name = line.split('/')[1].split('_')[0]
			else:
				protein_id = line.split(';')[0][2:].strip()
				gene_id = line.split(';')[1][-4:]
				if gene_id in gene_id_list:
					protein_gene[protein_id] = [gene_id,strain_name]

	return protein_gene

def get_gene_structure(file_name,protein_gene):
	with open(file_name,'r')as read_file:
		for line in read_file:
			if line.startswith('#'):
				continue
			col_list = line.strip().split('\t')
			# print(col_list)
			if col_list[1] == 'Protein Homology':
				protein_id = col_list[-1].split(';')[3].split('=')[1]
				# print(protein_id)
			else:
				continue
			if protein_id in protein_gene.keys():
				# print(protein_id)
				# print(protein_gene.keys())
				print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(protein_gene[protein_id][1],protein_id,protein_gene[protein_id][0],col_list[3],col_list[4],col_list[6],col_list[6]))


if __name__ == '__main__':
	protein_gene = get_protein_id(sys.argv[1])
	# print(protein_gene)
	for each_file in sys.argv[2:]:
		get_gene_structure(each_file,protein_gene)



