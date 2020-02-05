## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-27
# encoding='utf-8'

import sys
print('Island_start\tIsland_end\tLength\tMethod\tGene_name\tGene_ID\tLocus\tGene_start\tGene_end\tStrand\tProduct\tExternal_Annotations')
for each_file in sys.argv[1:]:
	GI_position = []
	GI_size = []
	strain_name = each_file.split('/')[-1].split('.')[0]
	with open(each_file,'r') as read_file:
		lines = read_file.readlines()
		# print(strain_name)
		for line in lines[1:]:
			col_list = line.strip().split('\t')
			GI_strat_end = '_'.join(col_list[:2])
			each_GI_size = int(col_list[1]) -int(col_list[0]) 
			GI_size.append(each_GI_size)
			if 'Predicted by at least one method' in line :
				# print(line.strip())
				if GI_strat_end not in GI_position:
					GI_position.append(GI_strat_end)
		print(f"{strain_name}'s number of GI:{len(GI_position)}")
print(f'GI MAX size:{max(GI_size)} \nGI min size:{min(GI_size)}')
# GI_size.sort()
# print(GI_size)		