## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-25
# encoding='utf-8'
import sys
import re

def open_knownclusterblast(file_name):
	strains_name = file_name.split('/')[1].split('_')[0] + '_' + file_name.split('/')[-1].split('.')[-2].split('_')[1]
	Metabolites = {}
	is_true = False
	with open(file_name,'r') as read_file:
		Metabolites[strains_name] = {'Mibig_id':'','Source':'','Type':''}
		for line in read_file:
			if '>>' == line.strip():
				is_true = True
			if is_true:
				if '1.' in line :
					Metabolites[strains_name]['Mibig_id'] = line.split('.')[1].strip()
				elif 'Source:' in line :
					Metabolites[strains_name]['Source'] = line.split(':')[1].strip()
				elif 'Type:' in line :
					Metabolites[strains_name]['Type'] = line.split(':')[1].strip()
			if 'Table of genes, locations, strands and annotations of subject cluster:' in line :
				break
	return Metabolites


if __name__ == '__main__':
	print('Strain\tMibig_id\tSource\tType')
	for each_file in sys.argv[1:]:
		Metabolites = open_knownclusterblast(each_file)
		for k,v in Metabolites.items():
			print('{}\t{}\t{}\t{}'.format(k,v['Mibig_id'],v['Source'],v['Type']))

