## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-26
# encoding='utf-8'

import sys

for each_file in sys.argv[1:]:
	seq = {}
	tRNA = {'A':'T','T':'A','C':'G','G':'C'}
	with open(each_file,'r')as read_file :
		for line  in read_file:
			if '>' in line :
				header = line.strip()
				seq[header] = ''
			else:
				for i in line.strip():
					seq[header] += tRNA[i]
				# print('ok')
	new_file = each_file + 'new'
	write_file = open(new_file,'w')
	for k,v in seq.items():
		write_file.write(f'{k}\n')
		new_v = v[::-1]
		count = 0
		for i in range(0,len(new_v)+1,80):
			write_file.write(f'{new_v[count:i]}\n')
			count = i
		write_file.write(f'{new_v[count:i]}\n')