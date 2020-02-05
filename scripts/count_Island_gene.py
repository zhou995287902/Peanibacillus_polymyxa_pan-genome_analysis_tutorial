## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-
import sys

def open_pan_sequence(file_name):
	seq = {}
	with open(file_name,'r')as read_file:
		for line in read_file:
			if '>' in line[0]:
				seq_name = line.split('/')[-1].strip()
				seq[seq_name] = ''
			else:
				seq[seq_name] += line.strip()

	return seq

def open_Island_tab(file_name):
	Island_list = {}
	with open(file_name,'r')as read_file:
		lines = read_file.readlines()
		for line in lines[1:]:
			col_list = line.split('\t')
			seq_position = col_list[0].strip()+','+col_list[1].strip()
			gene_name = col_list[4].strip()
			gene_id = col_list[6].strip()
			if seq_position not in Island_list.keys():
				Island_list[seq_position] = {}
				Island_list[seq_position][gene_id]=gene_name
			else:
				if gene_name not in Island_list[seq_position]:
					Island_list[seq_position][gene_id]=gene_name

	count = len(Island_list)
	return Island_list,count


if __name__ == '__main__':
	core_gene_count = 0
	accessory_gene_count = 0
	unique_gene_count = 0
	core_gene_seq = open_pan_sequence(sys.argv[1])
	accessory_gene_seq = open_pan_sequence(sys.argv[2])
	unique_gene_seq = open_pan_sequence(sys.argv[3])
	for each_Island_file in sys.argv[4:]:
		gene_count = 0
		Island_list,count = open_Island_tab(each_Island_file)
		for gene_id_list in Island_list.values(): 	
			gene_count += len(gene_id_list)
			each_Island_core_gene_count = 0
			each_Island_accessory_gene_count = 0
			each_Island_unique_gene_count = 0
			for each_gene_name in gene_id_list.values():
				if each_gene_name in core_gene_seq:
					core_gene_count += 1
					each_Island_core_gene_count += 1
					print('core_gene\t{}\t{}'.format(each_gene_name,core_gene_seq[each_gene_name]))
				elif each_gene_name in accessory_gene_seq:
					accessory_gene_count += 1
					each_Island_accessory_gene_count += 1
					print('accessory_gene\t{}\t{}'.format(each_gene_name,accessory_gene_seq[each_gene_name]))
				elif each_gene_name in unique_gene_seq:
					unique_gene_count +=1
					each_Island_unique_gene_count += 1
					print('unique_gene\t{}\t{}'.format(each_gene_name,unique_gene_seq[each_gene_name]))
			# print(len(gene_id_list),gene_id_list)
			# print(f'total_gene:{len(gene_id_list)}\teach_Island_core_gene_count:{each_Island_core_gene_count}\t\
			# each_Island_accessory_gene_count:{each_Island_accessory_gene_count}\teach_Island_unique_gene_count:{each_Island_unique_gene_count}')
		# print(f'{each_Island_file} Island count :{count}\tgene_count:{gene_count}')
	# print(f'core_gene_count:{core_gene_count}\naccessory_gene_count:{accessory_gene_count}\nunique_gene_count:{unique_gene_count}')