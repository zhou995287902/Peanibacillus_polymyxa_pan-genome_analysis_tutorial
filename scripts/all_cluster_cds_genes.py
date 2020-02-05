## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-12-16
# encoding='utf-8'
import sys
import re
## use command
## python all_cluster_cds_genes.py ./*/knownclusterblast/*.txt > get_metabolites_and_genes.table

def open_clusterblast(clusterblast_file_name):
	repeat_gene = []
	type_list = []
	# print(file_name)
	strains_name = clusterblast_file_name.split('/')[1].split('_')[0] + '_' + clusterblast_file_name.split('/')[-1].split('.')[-2].split('_')[1]
	# print(strains_name)
	Metabolites = {}
	total_genes = {}
	Mibig_genes = {}
	is_header = False
	is_true = False
	is_Mibig_gene = False
	genes_True = False
	gggenes_True = False
	count = 0
	cluster_type = ''
	with open(clusterblast_file_name,'r') as read_file:
		Metabolites[strains_name] = {'Match_strain_id':'','Source':'','Type':''}
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
				gggenes_True = False
				repeat_gene = []

			if is_true:
				Match_strain = re.search(r'^\d+\. \w+',line)
				if Match_strain :
					Metabolites[strains_name]['Match_strain_id'] = Match_strain.group()[3:]
					# print(Match_strain.group()[3:])
				elif 'Source:' in line :
					Metabolites[strains_name]['Source'] = line.split(':')[1].strip()
				elif 'Type:' in line :
					cluster_type = line.split(':')[1].strip()
					if cluster_type not in type_list:
						type_list.append(cluster_type)
						# print(type_list)
						genes_True = True
					else:
						genes_True = False
					Metabolites[strains_name]['Type'] = line.split(':')[1].strip()
			if 'Table of genes, locations, strands and annotations of subject cluster:' in line :
				is_Mibig_gene = True
				continue
			elif 'Table of Blast hits' in line :
				is_Mibig_gene = False
				gggenes_True = True
				continue
			if len(type_list) > 3:
				break
			# if is_Mibig_gene and line.strip() != '':
			# 	Mibig_col_list = line.strip().split('\t')
			# 	# print(Mibig_col_list)
			# 	Mibig_Protein_id = Mibig_col_list[0]
			# 	Mibig_start = Mibig_col_list[2]
			# 	Mibig_end = Mibig_col_list[3]
			# 	Mibig_strands = Mibig_col_list[4]
			# 	Mibig_annotations = Mibig_col_list[5]
			# 	Mibig_genes[Mibig_Protein_id] = {'Protein_id':Mibig_Protein_id,'start':Mibig_start,'end':Mibig_end,'strands':Mibig_strands,'annotations':Mibig_annotations}
			# if genes_True and cluster_type not in type_list:
			# 	type_list.append(cluster_type)
			# 	genes_True = True
			# else:
			# 	genes_True = False	
			# print(gggenes_True,genes_True)
			try:
				if gggenes_True and genes_True and line.strip() != '':
					# print('Strain\tMibig_id\tSource\tType')
					# for k,v in Metabolites.items():
						# print('{}\t{}\t{}\t{}\n'.format(k,v['Mibig_id'],v['Source'],v['Type']))
					col_list = line.strip().split('\t')
					# print(col_list)
					# print('Protein_id\tProtein_id\tStart\tend\tStand\tgene_id')
					loucs_id = col_list[0]
					Protein_id = col_list[1]
					identity = col_list[2]
					coverage = col_list[4]
					# print(loucs_id)
					# print(line)
					# print(f'{strains_name}\t{loucs_id}\t{Protein_id}\t{total_genes[loucs_id]['start']}\t{total_genes[loucs_id]['end']}\t\
						# {total_genes[loucs_id]['strands']}\t{Mibig_genes[Protein_id]['annotations']}')
					if loucs_id not in repeat_gene:
						# print(cluster_type)
						repeat_gene.append(loucs_id)
						print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(strains_name,Metabolites[strains_name]['Type'],\
							Metabolites[strains_name]['Source'],loucs_id,Protein_id,total_genes[loucs_id]['start'],total_genes[loucs_id]['end'],\
							total_genes[loucs_id]['strands'],total_genes[loucs_id]['annotations'],identity,coverage))
			except Exception as reason:
				# pass
				print('Error',reason)

	# print(Metabolites)
	return Metabolites


if __name__ == '__main__':
	
	for each_file in sys.argv[1:]:
		
		Metabolites = open_clusterblast(each_file)
		# for k,v in Metabolites.items():
			# print('{}\t{}\t{}\t{}'.format(k,v['Mibig_id'],v['Source'],v['Type']))

