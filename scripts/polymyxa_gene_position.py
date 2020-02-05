## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-31
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

# use command
# python gene_density_calculate.py /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/genomic_genebank/chromsome_genomic/*.tab > polymyxa_gene_length.txt

import sys

temp = {'ATCC':'CP011420','CF05':'NZ_CP009909','CR1':'CP006941','E681':'CP000154','HY96-2':'CP025957','J':'CP015423','M1':'HE577054','SC2':'CP002213',\
'SQR21':'CP006872','Sb3-1':'CP010268','YC0136':'CP017967','YC0573':'CP017968','ZF129':'CP040829','ZF197':'CP042272'}
def get_gene_psition(file_name):
	strain_name = file_name.split('/')[-1].split('_')[0]
	with open(file_name,'r') as read_file:
		for line in read_file:
			col_list = line.strip().split('\t')
			print(f'{temp[strain_name]}\t{col_list[1]}\t{col_list[2]}')


if __name__ == '__main__':
	for each_file in sys.argv[1:]:
		get_gene_psition(each_file)
