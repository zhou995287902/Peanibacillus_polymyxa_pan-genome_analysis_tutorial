## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

import sys

def open_similarity_links(file_name):
	result = []
	# line_list = []
	with open(file_name,'r')as read_file:
		
		for line in read_file:
			line_list = []
			col_list = line.strip().split('\t')
			line_list.append('_'.join(col_list[:3]))
			line_list.append('_'.join(col_list[3:]))
			# print(line_list)
			line_list.sort()
			# print(line_list)
			if line_list not in result:
				result.append(line_list)
				print('\t'.join(col_list))


if __name__ == '__main__':
	open_similarity_links(sys.argv[1])