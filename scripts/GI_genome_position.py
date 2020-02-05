## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2020-01-01
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

# use command
# python GI_genome_position.py /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/ISland_output/GIgene_COG_KEGG_anno.table > GI_genome_highlight.txt

import sys

def get_GI_group_position(file_name):
    GI_group_position = {}
    with open(file_name,'r') as read_file:
        lines = read_file.readlines()
        for line in lines[1:]:
            col_list = line.strip().split('\t')
            if len(col_list) == 1:
                strain_name = col_list[0]
                continue
            GI_num = col_list[0]
            GI_start = int(col_list[3])
            GI_end = int(col_list[4])
            if strain_name not in GI_group_position:
                GI_group_position[strain_name] = {}
            if GI_num not in GI_group_position[strain_name]:
                GI_group_position[strain_name][GI_num] = []
                GI_group_position[strain_name][GI_num].append(GI_start)
                GI_group_position[strain_name][GI_num].append(GI_end)
            else:
                GI_group_position[strain_name][GI_num].append(GI_start)
                GI_group_position[strain_name][GI_num].append(GI_end)
    return GI_group_position


if __name__ == '__main__':
    temp = {'ATCC15970':'CP011420.1','CF05':'NZ_CP009909.1','CR1':'CP006941.2','E681':'CP000154.2','HY96-2':'CP025957.1','J':'CP015423.1',\
    'M1chromosome':'HE577054.1','SC2chromosome':'CP002213.2','SQR21':'CP006872.1','Sb3-1chromosome':'CP010268.1','YC0136':'CP017967.3','YC0573':'CP017968.3',\
    'ZF129chromosome':'CP040829.1','ZF197chromosome':'CP042272.1'}
    tt = ['M1plasmid','SC2Psc2','']
    position = get_GI_group_position(sys.argv[1])
    # print(position)
    for k,v in position.items():
        if k not in tt:
            for i,j in v.items():
                GI_strat = min(j)
                GI_end = max(j)
                print(f'{temp[k]}\t{GI_strat}\t{GI_end}\tfill_color=vlyellow')

