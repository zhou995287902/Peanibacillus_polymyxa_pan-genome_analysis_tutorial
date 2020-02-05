## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## change time: 2019-11-24
# encoding='utf-8'

import sys
import re


def open_gbk_file(file_name):
    # print(file_name.split('/'))
    strains_name = file_name.split('/')[1].split('_')[0] + '_' + file_name.split('/')[2].split('.')[-2]
    # print(strains_name)
    sec_meta_type = {}
    type_length = {}
    type_position = {}
    with open(file_name,'r') as read_file:
        lines = read_file.readlines()
        all_length = re.search(r'\d+ bp',lines[0]).group().split(' ')[0]
        for line in lines:
            gene_position = re.search(r'\d+\.\.\d+',line)
            if gene_position:
                if 'gene' not in line:
                    gene_position_key = gene_position.group()
                    sec_meta_type[gene_position_key] = []
                    # print(gene_position)
            else:
                if "product" in line :
                    # print(gene_position)
                    sec_meta_type[gene_position_key].append(line.split('=')[-1].strip())
    # print('\n'.join(sec_meta_type[f'1..{all_length}']))
    temp = ''

    for i in sec_meta_type[f'1..{all_length}']:
        # print(sec_meta_type)
        ## 这里是用来看次级代谢产物是出自哪个菌株
        ii = strains_name + i
        # ii = i
        type_length[ii] = 0
        for k,v in sec_meta_type.items():
            # print(k,v)
            if temp != i and len(v) < 2 and i in v :
                min_start = float(k.split('..')[0])
                max_end = float(k.split('..')[1])
                type_length[ii] += float(k.split('..')[1]) - float(k.split('..')[0]) + 1
                temp = i
            if len(v) < 2 and i in v :
                if min_start >= float(k.split('..')[0]) and max_end <= float(k.split('..')[1]):
                    type_length[ii] -= max_end - min_start + 1
                    min_start = float(k.split('..')[0])
                    max_end = float(k.split('..')[1])
                    type_length[ii] += float(k.split('..')[1]) - float(k.split('..')[0]) + 1
                elif min_start < float(k.split('..')[0]) and max_end > float(k.split('..')[1]):
                    pass    
                elif min_start <= float(k.split('..')[0]) and max_end < float(k.split('..')[1]):
                    type_length[ii] += float(k.split('..')[1]) - max_end 
                    max_end = float(k.split('..')[1])
                elif min_start > float(k.split('..')[0]) and max_end >= float(k.split('..')[1]):
                    type_length[ii] += min_start - float(k.split('..')[0]) 
                    min_start = float(k.split('..')[0])
                type_position[ii] = str(int(min_start)) + '@@' + str(int(max_end))
    
    for k,v in type_length.items():
        meta_position_start = type_position[k].split('@@')[0]
        meta_position_end = type_position[k].split('@@')[1]
        k = k.strip('"')
        strain_name = k.split('"')[0]
        meta_type = k.split('"')[1]
        print(f'{strain_name}\t{meta_position_start}\t{meta_position_end}\t{meta_type}\t{v}') 

if __name__ =='__main__':
    print('strain_name\tstart\tend\tType\tLength')
    for file_name in sys.argv[1:]:
        open_gbk_file(file_name)
