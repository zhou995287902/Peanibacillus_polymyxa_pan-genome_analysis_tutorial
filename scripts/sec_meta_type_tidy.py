## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1],'r')as read_file:
	for line in read_file:
		col_list = line.strip().split(' ')
		print('{}\t{}:{}'.format(col_list[1].split('"')[0],col_list[1].split('"')[1],col_list[0]))