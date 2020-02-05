python ../../scripts/count_Island_gene.py ../PAN_genome_analysis/sequence/core_seq.txt ../PAN_genome_analysis/sequence/accessory_seq.txt ../PAN_genome_analysis/sequence/unique_seq.txt *.tsv|less -S
python ../../scripts/GIgene_COG_KEGG_anno.py tidy_all_COG_gene_class.table all_KEGG_anno.txt Island_type_count.tab *.tsv > GIgene_COG_KEGG_anno.table





