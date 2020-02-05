## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-30
# encoding='utf-8'
import sys
import re
## use command
## python get_metabolites_and_genes.py ./*/knownclusterblast/*.txt > get_metabolites_and_genes.table

def open_knownclusterblast(file_name):
	repeat_gene = []
	# print(file_name)
	strains_name = file_name.split('/')[1].split('_')[0] + '_' + file_name.split('/')[-1].split('.')[-2].split('_')[1]
	print(strains_name)
	Metabolites = {}
	total_genes = {}
	Mibig_genes = {}
	is_header = False
	is_true = False
	is_Mibig_gene = False
	genes_True = False
	count = 0
	with open(file_name,'r') as read_file:
		Metabolites[strains_name] = {'Mibig_id':'','Source':'','Type':''}
		for line in read_file:
			if 'Table of genes, locations, strands and annotations of query cluster:' in line :
				is_header = True
				continue
			elif line.strip() == '':
				is_header = False
			if is_header:
				total_col_list = line.strip().split('\t')
				total_loucs_id = total_col_list[0]
				total_start = total_col_list[1]
				total_end = total_col_list[2]
				total_strands = total_col_list[3]
				total_annotations = total_col_list[4]
				total_genes[total_loucs_id] = {'loucs_id':total_loucs_id,'start':total_start,'end':total_end,'strands':total_strands,'annotations':total_annotations}
			if '>>' == line.strip():
				count +=1
				is_true = True
			if is_true:
				if '1.' in line :
					Metabolites[strains_name]['Mibig_id'] = line.split('.')[1].strip()
				elif 'Source:' in line :
					Metabolites[strains_name]['Source'] = line.split(':')[1].strip()
				elif 'Type:' in line :
					Metabolites[strains_name]['Type'] = line.split(':')[1].strip()
			if 'Table of genes, locations, strands and annotations of subject cluster:' in line :
				is_Mibig_gene = True
				continue
			elif 'Table of Blast hits' in line :
				is_Mibig_gene = False
				genes_True = True
				continue

			if is_Mibig_gene and line.strip() != '':
				Mibig_col_list = line.strip().split('\t')
				# print(Mibig_col_list)
				Mibig_Protein_id = Mibig_col_list[0]
				Mibig_start = Mibig_col_list[2]
				Mibig_end = Mibig_col_list[3]
				Mibig_strands = Mibig_col_list[4]
				Mibig_annotations = Mibig_col_list[5]
				Mibig_genes[Mibig_Protein_id] = {'Protein_id':Mibig_Protein_id,'start':Mibig_start,'end':Mibig_end,'strands':Mibig_strands,'annotations':Mibig_annotations}
			if count >= 2:
				genes_True = False
				break	
			try:
				if genes_True and line.strip() != '':
					# print('Strain\tMibig_id\tSource\tType')
					# for k,v in Metabolites.items():
						# print('{}\t{}\t{}\t{}\n'.format(k,v['Mibig_id'],v['Source'],v['Type']))
					col_list = line.strip().split('\t')
					# print(col_list)
					# print('Protein_id\tProtein_id\tStart\tend\tStand\tgene_id')
					loucs_id = col_list[0]
					Protein_id = col_list[1]
					# print(line)
					# print(f'{strains_name}\t{loucs_id}\t{Protein_id}\t{total_genes[loucs_id]['start']}\t{total_genes[loucs_id]['end']}\t\
						# {total_genes[loucs_id]['strands']}\t{Mibig_genes[Protein_id]['annotations']}')
					if loucs_id not in repeat_gene:
						repeat_gene.append(loucs_id)
						print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(strains_name,Metabolites[strains_name]['Source'],loucs_id,Protein_id,total_genes[loucs_id]['start'],total_genes[loucs_id]['end'],\
						total_genes[loucs_id]['strands'],Mibig_genes[Protein_id]['annotations']))
			except Exception as reason:
				# pass
				print('Error',reason)
			
	return Metabolites


if __name__ == '__main__':
	
	for each_file in sys.argv[1:]:
		
		Metabolites = open_knownclusterblast(each_file)
		# for k,v in Metabolites.items():
			# print('{}\t{}\t{}\t{}'.format(k,v['Mibig_id'],v['Source'],v['Type']))

