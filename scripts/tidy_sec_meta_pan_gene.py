## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-11-14
## change time : 2019-11-24
#encoding='utf-8'
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

def open_sec_meta_tab(file_name):
	strains_name = file_name.split('/')[1].split('_')[0] + '_' + file_name.split('/')[2].split('.')[-2]
	sec_meta_list = {}
	with open(file_name,'r')as read_file:
		lines = read_file.readlines()
		for line in lines:
			col_list = line.split('\t')
			seq_position = col_list[1].strip()+','+col_list[2].strip()
			gene_id = col_list[3].strip() + '@@' + seq_position + '@@' + strains_name
			gene_name = col_list[4].strip()
			# print(gene_id,gene_name)
			if seq_position not in sec_meta_list.keys():
				sec_meta_list[seq_position] = {}
				sec_meta_list[seq_position][gene_id]=gene_name
			else:
				if gene_name not in sec_meta_list[seq_position]:
					sec_meta_list[seq_position][gene_id]=gene_name

	count = len(sec_meta_list)
	return sec_meta_list,count


if __name__ == '__main__':
	core_gene_count = 0
	accessory_gene_count = 0
	unique_gene_count = 0
	core_gene_seq = open_pan_sequence(sys.argv[1])
	accessory_gene_seq = open_pan_sequence(sys.argv[2])
	unique_gene_seq = open_pan_sequence(sys.argv[3])
	print('strain_name\tgene_type\tprotein_id\tstart\tend\tprotein_seq')
	for each_sec_meta_file in sys.argv[4:]:
		gene_count = 0
		sec_meta_list,count = open_sec_meta_tab(each_sec_meta_file)
		# print(sec_meta_list)
		for gene_id_list in sec_meta_list.values(): 	
			gene_count += len(gene_id_list)
			each_sec_meta_core_gene_count = 0
			each_sec_meta_accessory_gene_count = 0
			each_sec_meta_unique_gene_count = 0
			for gene_id_position,each_gene_name in gene_id_list.items():
				strain_name = gene_id_position.split('@@')[2]
				gene_position_start = gene_id_position.split('@@')[1].split(',')[0]
				gene_position_end = gene_id_position.split('@@')[1].split(',')[1]
				if each_gene_name in core_gene_seq:
					core_gene_count += 1
					each_sec_meta_core_gene_count += 1
					print('{}\tcore_gene\t{}\t{}\t{}\t{}'.format(strain_name,each_gene_name,gene_position_start,gene_position_end,core_gene_seq[each_gene_name]))
				elif each_gene_name in accessory_gene_seq:
					accessory_gene_count += 1
					each_sec_meta_accessory_gene_count += 1
					print('{}\taccessory_gene\t{}\t{}\t{}\t{}'.format(strain_name,each_gene_name,gene_position_start,gene_position_end,accessory_gene_seq[each_gene_name]))
				elif each_gene_name in unique_gene_seq:
					unique_gene_count +=1
					each_sec_meta_unique_gene_count += 1
					print('{}\tunique_gene\t{}\t{}\t{}\t{}'.format(strain_name,each_gene_name,gene_position_start,gene_position_end,unique_gene_seq[each_gene_name]))
			# print(len(gene_id_list),gene_id_list)
			# print(f'total_gene:{len(gene_id_list)}\teach_sec_meta_core_gene_count:{each_sec_meta_core_gene_count}\t\
			# each_sec_meta_accessory_gene_count:{each_sec_meta_accessory_gene_count}\teach_sec_meta_unique_gene_count:{each_sec_meta_unique_gene_count}')
		# print(f'{each_sec_meta_file} sec_meta count :{count}\tgene_count:{gene_count}')
	# print(f'core_gene_count:{core_gene_count}\naccessory_gene_count:{accessory_gene_count}\nunique_gene_count:{unique_gene_count}')