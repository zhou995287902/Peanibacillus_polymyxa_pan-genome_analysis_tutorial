## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-27
# encoding='utf-8'
import sys

def open_KEGG_anno(file_name):
	KEGG_ID = {}
	with open(file_name,'r') as read_file:
		lines = read_file.readlines()
		for line in lines[1:]:
			col_list = line.strip().split('\t')
			protein_id = col_list[1]
			ko4_id = col_list[2]
			KEGG_ID[protein_id] = ko4_id

	return KEGG_ID

def open_COG_anno(file_name):
	COG_anno_id = {}
	with open(file_name,'r') as read_file:
		lines = read_file.readlines()
		for line in lines:
			col_list = line.strip().split('\t')
			protein_id = col_list[0]
			COG_id = col_list[1]
			COG_type = col_list[2]
			COG_anno_id[protein_id] = [COG_id,COG_type]

	return COG_anno_id


def open_island_type(file_name):
	island_type = {}
	with open(file_name,'r') as read_file:
		for line in read_file:
			col_list = line.strip().split('\t')
			protein_id = col_list[1]
			gene_type = col_list[0]
			island_type[protein_id] = gene_type

	return island_type


def open_total_strain_GI(file_name,KEGG_ID,COG_anno_id,island_type):
	GI_Position = []
	strain_name = each_file.split('/')[-1].split('.')[0]
	with open(file_name,'r') as read_file:
		lines = read_file.readlines()
		print(strain_name)
		for line in lines[1:]:
			COG_id = ''
			Ko4_id = ''
			gene_type = ''
			COG_type = ''
			col_list = line.strip().split('\t')
			GI_strat_end = '_'.join(col_list[:2]) 
			locus = col_list[6]
			Gene = col_list[5]
			Gene_start = col_list[7]
			Gene_end = col_list[8]
			Gene_id = col_list[4]
			Strand = col_list[9]
			Product = col_list[10]
			if 'Predicted by at least one method' in line :
				# print(line.strip())
				if GI_strat_end not in GI_Position:
					GI_Position.append(GI_strat_end)
					GI_number = len(GI_Position)
				GI_id = 'GI' + str(GI_number)
				if Gene_id in KEGG_ID :
					Ko4_id = KEGG_ID[Gene_id]
				if Gene_id in COG_anno_id:
					COG_id = COG_anno_id[Gene_id][0]
					COG_type = COG_anno_id[Gene_id][1]
				if Gene_id in island_type:
					gene_type = island_type[Gene_id]
				print(f'{GI_id}\t{Gene_id}\t{Gene}\t{Gene_start}\t{Gene_end}\t{Strand}\t{Product}\t{COG_id}\t{COG_type}\t{Ko4_id}\t{gene_type}')




if __name__ == '__main__':
	print('GI_ID\tGene_ID\tGene\tGene_start\tGene_end\tStrand\tProduct\tCOG\tCOG_type\tKEGG\tPan_gene')
	COG_anno_id = open_COG_anno(sys.argv[1])
	KEGG_ID = open_KEGG_anno(sys.argv[2])
	island_type = open_island_type(sys.argv[3])
	for each_file in sys.argv[4:]:
		open_total_strain_GI(each_file,KEGG_ID,COG_anno_id,island_type)
