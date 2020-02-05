## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-31
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

# use command
# python highlight_cluster_position.py /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/secondary_metabolite_biosynthetic_gene_clusters/Fusaricidin_gene.table > Fusaricidin_gene_highlight_position.txt
# python highlight_cluster_position.py /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/secondary_metabolite_biosynthetic_gene_clusters/Tridecaptin_gene > Polymyxin_gene_highlight_position.txt
# python highlight_cluster_position.py /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/secondary_metabolite_biosynthetic_gene_clusters/Tridecaptin_gene_.table > Tridecaption_gene_highlight_position.txt
# python highlight_cluster_position.py /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/secondary_metabolite_biosynthetic_gene_clusters/Paenilan_gene_structure.table > Paenilan_gene_highlight_position.txt
# python highlight_cluster_position.py /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/KEGG_pathway_analysis/14_Paenibacilus_polymyxa_KEGG/nif_gene_structure_add_protein_id.table > nif__gene_highlight_position.txt
import sys

def get_cluster_position(file_name):
    position = {}
    with open(file_name,'r') as read_file:
        for line in read_file:
            col_list = line.strip().split('\t')
            strain_name = col_list[0]
            gene_start = int(col_list[4])
            gene_end = int(col_list[5])
            if strain_name not in position:
                position[strain_name] = []
                position[strain_name].append(gene_start)
                position[strain_name].append(gene_end)
            else:
                position[strain_name].append(gene_start)
                position[strain_name].append(gene_end)
    return position


if __name__ == '__main__':
    temp = {'ATCC15970':'CP011420.1','CF05':'NZ_CP009909.1','CR1':'CP006941.2','E681':'CP000154.2','HY96-2':'CP025957.1','J':'CP015423.1',\
    'M1':'HE577054.1','SC2':'CP002213.2','SQR21':'CP006872.1','Sb3-1':'CP010268.1','YC0136':'CP017967.3','YC0573':'CP017968.3',\
    'ZF129':'CP040829.1','ZF197':'CP042272.1'}
    position = get_cluster_position(sys.argv[1])
    for k,v in position.items():
        if k != 'WLY78':
            cluster_strat = min(v)
            cluster_end = max(v)
            print(f'{temp[k]}\t{cluster_strat}\t{cluster_end}\tfill_color=vlyellow')
