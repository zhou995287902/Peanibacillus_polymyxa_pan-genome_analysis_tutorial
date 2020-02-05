## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-27
# encoding='utf-8'

## use command
## python tidy_all_KEGG_anno.py ./*/gene_anno.txt|less -S
import sys 

def open_gene_anno(file_name):
	with open(file_name,'r') as read_file:
		lines = read_file.readlines()
		for line in lines[1:]:
			print(line.strip())

if __name__ == '__main__':
	for each_file in sys.argv[1:]:
		open_gene_anno(each_file)
