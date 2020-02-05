## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-31
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

# use command
# python gene_density_calculate.py polymyxa_genome_length.txt polymyxa_gene_length.txt > gene_density_heatmap.txt
import sys

def get_genomic_length(file_name):
    genomic_length = {}
    with open(file_name,'r') as read_file:
        for line in read_file:
            col_list = line.strip().split('\t')
            access_id = col_list[0]
            genomic_strat = int(col_list[1])
            genomic_end = int(col_list[2])
            genomic_length[access_id] = [genomic_strat,genomic_end]
    return genomic_length


def get_gene_position(file_name,genomic_length):
    gene_density = {}
    for k,v in genomic_length.items():
        j = 0
        gene_density[k] = {}
        ge_length = v[1] -v[0]
        for i in range(0,ge_length,ge_length//20):
            gene_density[k][f'{j}..{i}'] = 0
            j = i
    # print(gene_density)
    with open(file_name,'r') as read_file:
        for line in read_file:
            col_list = line.strip().split('\t')
            # print(col_list)
            access_id = col_list[0]
            gene_strat = int(col_list[1])
            gene_end = int(col_list[2])
            for k in gene_density[access_id]:
                j = int(k.split('..')[0])
                i = int(k.split('..')[1])
                if gene_strat >= j and gene_end <= i:
                    gene_density[access_id][k] +=1
    return gene_density


if __name__ == '__main__':
    temp1 = {'CP011420':'id=chr1','NZ_CP009909':'id=chr2','CP006941':'id=chr3','CP000154':'id=chr4','CP025957':'id=chr5','CP015423':'id=chr6','HE577054':'id=chr7','CP002213':'id=chr8',\
        'CP006872':'id=chr9','CP010268':'id=chr10','CP017967':'id=chr11','CP017968':'id=chr12','CP040829':'id=chr13','CP042272':'id=chr14'}
    temp = {'CP011420':'CP011420.1','NZ_CP009909':'NZ_CP009909.1','CP006941':'CP006941.2','CP000154':'CP000154.2','CP025957':'CP025957.1',\
    'CP015423':'CP015423.1','HE577054':'HE577054.1','CP002213':'CP002213.2','CP006872':'CP006872.1','CP010268':'CP010268.1',\
    'CP017967':'CP017967.3','CP017968':'CP017968.3','CP040829':'CP040829.1','CP042272':'CP042272.1'}
    genomic_length = get_genomic_length(sys.argv[1])
    gene_density=get_gene_position(sys.argv[2],genomic_length)
    for k,v in gene_density.items():
        for i,j in v.items():
            group_strat = int(i.split('..')[0])
            group_end = int(i.split('..')[1])
            print(f'{temp[k]}\t{group_strat}\t{group_end}\t{j}\t{temp1[k]}')
            # print(f'{temp[k]}\t{group_strat}\t{group_end}\t{j}')