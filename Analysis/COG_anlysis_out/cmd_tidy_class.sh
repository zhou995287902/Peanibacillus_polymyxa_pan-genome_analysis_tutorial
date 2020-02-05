cut -f 1,2,3 core_out.class > t1
cut -f 3 accessory_out.class > t2
cut -f 3 unique_out.class > t3

paste t1 t2 t3 > Pan_cog_gene_count.txt

rm t1 t2 t3

