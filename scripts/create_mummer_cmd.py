## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-26
# encoding='utf-8'

import sys
file_names = sys.argv[1:]
new_file = ['./ZF129_GCA_006274405.1_ASM627440v1_genomic.fnanew','./Sb3-1_GCA_000819665.1_ASM81966v1_genomic.fnanew']
# for ref_file in sys.argv[1:]:
# 	temp_list = []
# 	for qry_file in sys.argv[1:]:
# 		out_file = qry_file.split('/')[-1].split('_')[0] + '_2_' + ref_file.split('/')[-1].split('_')[0]
# 		#print('nucmer -c 200 -g 200 -p {} {} {}'.format(out_file,ref_file,qry_file))
# 		#print('delta-filter -1 {}.delta > {}.rq.delta'.format(out_file,out_file))
# 		#print('show-coords -T -q -H {}.rq.delta > {}.show'.format(out_file,out_file))
# 		#print('mummerplot -f -l -p {} -s large -t png {}.delta'.format(out_file,out_file))	
	# 	temp_list.append(f'"{out_file}.show"')
	# for i in range(len(temp_list)-1,-1,-1):
	# 	print(temp_list[i],end=',')	

for ref_file in new_file:
	temp_list = []
	for qry_file in file_names:
		# print(ref_file,qry_file)
		out_file = qry_file.split('/')[-1].split('_')[0] + '_2_' + ref_file.split('/')[-1].split('_')[0]
		print('nucmer -c 200 -g 200 -p {} {} {}'.format(out_file,ref_file,qry_file))
		print('delta-filter -1 {}.delta > {}.rq.delta'.format(out_file,out_file))
		print('show-coords -T -q -H {}.rq.delta > {}.show'.format(out_file,out_file))
		print('mummerplot -f -l -p {} -s large -t png {}.delta'.format(out_file,out_file))

for ref_file in file_names:
	temp_list = []
	for qry_file in new_file:
		# print(new_file)
		# print(ref_file,qry_file)
		out_file = qry_file.split('/')[-1].split('_')[0] + '_2_' + ref_file.split('/')[-1].split('_')[0]
		print('nucmer -c 200 -g 200 -p {} {} {}'.format(out_file,ref_file,qry_file))
		print('delta-filter -1 {}.delta > {}.rq.delta'.format(out_file,out_file))
		print('show-coords -T -q -H {}.rq.delta > {}.show'.format(out_file,out_file))
		print('mummerplot -f -l -p {} -s large -t png {}.delta'.format(out_file,out_file))
