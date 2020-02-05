## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

import sys


if len(sys.argv) != 3:
    print('\nuseage:\npython3 download_ref_seq.py <strain_name> <input_txt> \nexample:\npython3 download_ref_seq.py Bacillus_amyloliquefaciens strain_list_add_assembly_name.txt \n')
    exit()

with open(sys.argv[2],'r') as read_file:
    lines = read_file.readlines()
    for line in lines:
        line = line.strip().split('\t')
        ID = line[1]+'_'+line[2]
        file_name = ['_cds_from_genomic.fna.gz','_genomic.fna.gz','_genomic.gff.gz','_protein.faa.gz','_genomic.gbff.gz','_feature_table.txt.gz']
        for i in file_name:
            cmd_str = 'wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/{0}/latest_assembly_versions/{1}/{2}'.format(sys.argv[1],ID,ID+i)
            cmd_change_name = 'mv {0} {1}'.format(ID+i,line[0]+'_'+ID+i)
            print(cmd_str) 
            print(cmd_change_name)
