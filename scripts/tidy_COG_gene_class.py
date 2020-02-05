## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-11-27
# encoding='utf-8'

import sys

def open_COG_class_file(file_name):
    with open(file_name,'r')as read_file:
         lines = read_file.readlines()
         for line in lines[1:]:
            col_list = line.strip().split('\t')
            Code = col_list[0]
            Function = col_list[1]
            if col_list[2] != '0':
                # print(col_list)
                gene_id_list = col_list[-1].split(' ')
                # print(gene_id_list)
                for each_gene_id in gene_id_list:
                    gene_id = each_gene_id.split(',')[0].split('/')[-1]
                    COG_id = ','.join(each_gene_id.split(',')[1:])
                    gene_type = each_gene_id.split(',')[0].split('/')[0]
                    print(f'{gene_id}\t{COG_id}\t{Code}\t{gene_type}\t{Function}')

if __name__ == '__main__':
    for each_file in sys.argv[1:]:
        open_COG_class_file(each_file)    
            

