## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-16
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

## use command
## python get_cluster_cds_position.py sec_meta_type_length_new.table ./*_genomic*/*.tab > all_cluster_cds_position.table

import sys


def get_cluster_cds_seq(cds_tab_file):
    global cds_tab_dict 
    file_name = cds_tab_file.split('/')[-2].split('_')[0] + '_' + cds_tab_file.split('.')[-2]
    cds_tab_dict[file_name] = {}
    with open(cds_tab_file,'r') as read_file:
        for line in read_file:
            col_list = line.strip().split('\t')
            position = col_list[1] + '..' + col_list[2]
            cds_tab_dict[file_name][position] = col_list

def get_cluster_position(all_cluster_file,cds_tab_dict):
    with open(all_cluster_file,'r') as read_file:
        lines = read_file.readlines()
        for line in lines[1:]:
            col_list = line.strip().split('\t')
            strain_name = col_list[0]
            strain_nm = strain_name.split('_')[0]
            cluster_start = col_list[1]
            cluster_end = col_list[2]
            cluster_type = col_list[3]
            cluster_cds = cds_tab_dict[strain_name]
            for v in cluster_cds.values():
                cds_start = v[1]
                cds_end = v[2]
                cds_foucs = v[3]
                cds_protein_id = v[4]
                cds_gene_name = v[5]
                if cds_start >= cluster_start and cds_end <= cluster_end:
                    print(f'{strain_nm}\t{cluster_type}\t{cds_foucs}\t{cds_protein_id}\t{cds_start}\t{cds_end}\t{cds_gene_name}\t+\t+')

if __name__ == '__main__':
    all_cluster_file = sys.argv[1]
    cds_tab_dict = {}
    for each_file in sys.argv[2:]:
        get_cluster_cds_seq(each_file)
    # print(cds_tab_dict)
    get_cluster_position(all_cluster_file,cds_tab_dict)


