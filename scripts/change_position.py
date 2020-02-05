## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-26
# encoding='utf-8'

import sys

for each_file in sys.argv[1:]:
	col_one = []
	write_file_name = './' + 'temp/' +each_file.split('/')[1] 
	# print(write_file_name)
	write_file = open(write_file_name,'w')
	with open(each_file,'r')as read_file:
		lines = read_file.readlines()
		for line in lines:
			col_list = line.strip().split('\t')
			# print(col_list[:2])
			col_one.append(col_list[:2])
			# print(col_one)
			#write_file.write(f'{col_list[2]}\t{col_list[3]}\t{col_list[0]}\t{col_list[1]}\t{col_list[4]}\t{col_list[5]}\t{col_list[6]}\t{col_list[7]}\t{col_list[8]}\n')
		col_one.reverse()
		# print(col_one)
		for index in range(len(lines)):
			temp = '\t'.join(col_one[index])
			temp2 = '\t'.join(lines[index].strip().split('\t')[2:])
			# print(f'{temp}\t{temp2}')
			write_file.write(f'{temp}\t{temp2}\n')
	write_file.close()