#encoding='utf-8'

python gene_list_make.py ../../Data/Peanibacillus_polymyxa_strains_sequence/genomic_genebank/*.gbff > ../gene.list.txt

## core_seq
python ../../script/kegg_trans.py ./core_genome_kegg_analysis/q00001.keg gene.list.txt ./core_genome_kegg_analysis/gene_anno.txt ./core_genome_kegg_analysis/pathway_anno.txt
mkdir ./core_genome_kegg_analysis/map_download
python ../../script/pathway_download.py core_genome_kegg_analysis/pathway_anno.txt core_genome_kegg_analysis/map_download/

## accessory_seq
python ../../script/kegg_trans.py ./accessory_genome_kegg_analysis/q00001.keg gene.list.txt ./accessory_genome_kegg_analysis/gene_anno.txt ./accessory_genome_kegg_analysis/pathway_anno.txt
mkdir ./accessory_genome_kegg_analysis/map_download
python ../../script/pathway_download.py ./accessory_genome_kegg_analysis/pathway_anno.txt accessory_genome_kegg_analysis/map_download/


## unique_seq
python ../../script/kegg_trans.py ./unique_genome_kegg_analysis/q00001.keg gene.list.txt ./unique_genome_kegg_analysis/gene_anno.txt ./unique_genome_kegg_analysis/pathway_anno.txt
mkdir ./unique_genome_kegg_analysis/map_download
python ../../script/pathway_download.py ./unique_genome_kegg_analysis/pathway_anno.txt unique_genome_kegg_analysis/map_download/