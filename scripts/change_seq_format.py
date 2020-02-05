## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-16
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

import sys


def del_plasmid_seq(read_file_name,write_file_name):
    seq = {}
    write_file = open(write_file_name,'w')
    with open(read_file_name,'r') as read_file:
        for line in read_file:
            # print(line)
            if '>' in line[0]:
                # print(seq_name)
                seq_name = line
                seq[line] = ''
            else:
                seq[seq_name] += line
    for k,v in seq.items():
        if "plasmid" not in k:
            write_file.write(k+v)

    write_file.close()






all_genomic_file_names = sys.argv[1:]


for each_file in all_genomic_file_names:
    write_file_name = each_file.split('/')[1]
    read_file_name = each_file
    # print(each_file)
    del_plasmid_seq(read_file_name,write_file_name)

# print(sys.argv[:])
# print(file_name)
# write_file = open('all_genomic.fasta','w')
# bool_pick = False
# with open(sys.argv[1],'r') as f:
#     seq = {}
#     for line in f:
#         if 'complete genome' in line and '>' in line:
#             bool_pick = True
#         elif '>' in line and 'plasmid' in line:
#             bool_pick = False
#         if '>' in line and bool_pick:
#             head_name = line.strip()
#             seq[head_name] = ''
#         elif bool_pick:
#             seq[head_name] += line.strip()
#     for k,v in seq.items():
#         write_file.write(k+'\n'+v+'\n')

# write_file.close()


