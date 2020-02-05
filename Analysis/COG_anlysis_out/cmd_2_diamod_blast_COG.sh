diamond makedb --in ~/Database/COG/myva -d COG2003

## accessory_seq
diamond blastp -d ~/Database/COG/COG2003 -q accessory_seq.txt -e 1e-5 -k 50 --sensitive -o accessory_seq_diamond_out.m8
python ../../scripts/filter_diamond_cogblastp_out_m8.py accessory_seq_diamond_out.m8 > accessory_seq_diamond_out.filter.m8
python ../../scripts/diamond_COG_blast_anno_filter.py ~/Database/COG/COG2014/cog2003-2014.csv ~/Database/COG/COG2014/cognames2003-2014.tab accessory_seq_diamond_out.filter.m8 > Accessory_seq_COG_diamond_blast_filter_anno.txt
python ../../scripts/diamond_COG_count.py Accessory_seq_COG_diamond_blast_filter_anno.txt ~/Database/COG/COG2014/fun2003-2014.tab > Accessory_COG_type_count.table

## accessory_genes_with_atypical_GC_content
diamond blastp -d ~/Database/COG/COG2003 -q accessory_genes_with_atypical_GC_content.txt -e 1e-5 -k 50 --sensitive -o accessory_genes_with_atypical_GC_content_diamond_out.m8
python filter_diamond_cogblastp_out_m8.py accessory_genes_with_atypical_GC_content_diamond_out.m8 > accessory_genes_with_atypical_GC_content_diamond_out.filter.m8
python ../../scripts/diamond_COG_blast_anno_filter.py ~/Database/COG/COG2014/cog2003-2014.csv ~/Database/COG/COG2014/cognames2003-2014.tab accessory_genes_with_atypical_GC_content_diamond_out.filter.m8 > Accessory_genes_with_atypical_GC_content_COG_diamond_blast_filter_anno.txt
python ../../scripts/diamond_COG_count.py Accessory_genes_with_atypical_GC_content_COG_diamond_blast_filter_anno.txt ~/Database/COG/COG2014/fun2003-2014.tab > Accessory_genes_with_atypical_GC_content_COG_type_count.table


## core_seq
diamond blastp -d ~/Database/COG/COG2003 -q core_seq.txt -e 1e-5 -k 50 --sensitive -o core_seq_diamond_out.m8
python ../../scripts/filter_diamond_cogblastp_out_m8.py core_seq_diamond_out.m8 > core_seq_diamond_out.filter.m8
python ../../scripts/diamond_COG_blast_anno_filter.py ~/Database/COG/COG2014/cog2003-2014.csv ~/Database/COG/COG2014/cognames2003-2014.tab core_seq_diamond_out.filter.m8 > Core_seq_COG_diamond_blast_filter_anno.txt
python ../../scripts/diamond_COG_count.py Core_seq_COG_diamond_blast_filter_anno.txt ~/Database/COG/COG2014/fun2003-2014.tab > Core_COG_type_count.table


## core_genes_with_atypical_GC_content
diamond blastp -d ~/Database/COG/COG2003 -q core_genes_with_atypical_GC_content.txt -e 1e-5 -k 50 --sensitive -o core_genes_with_atypical_GC_content_diamond_out.m8
python filter_diamond_cogblastp_out_m8.py core_genes_with_atypical_GC_content_diamond_out.m8 > core_genes_with_atypical_GC_content_diamond_out.filter.m8
python ../../scripts/diamond_COG_blast_anno_filter.py ~/Database/COG/COG2014/cog2003-2014.csv ~/Database/COG/COG2014/cognames2003-2014.tab core_genes_with_atypical_GC_content_diamond_out.filter.m8 > Core_genes_with_atypical_GC_content_COG_diamond_blast_filter_anno.txt
python ../../scripts/diamond_COG_count.py Core_genes_with_atypical_GC_content_COG_diamond_blast_filter_anno.txt ~/Database/COG/COG2014/fun2003-2014.tab > Core_genes_with_atypical_GC_content_COG_type_count.table


## unique_seq
diamond blastp -d ~/Database/COG/COG2003 -q unique_seq.txt -e 1e-5 -k 50 --sensitive -o unique_seq_diamond_out.m8
python ../../scripts/filter_diamond_cogblastp_out_m8.py unique_seq_diamond_out.m8 > unique_seq_diamond_out.filter.m8
python ../../scripts/diamond_COG_blast_anno_filter.py ~/Database/COG/COG2014/cog2003-2014.csv ~/Database/COG/COG2014/cognames2003-2014.tab unique_seq_diamond_out.filter.m8 > Unique_seq_COG_diamond_blast_filter_anno.txt
python ../../scripts/diamond_COG_count.py Unique_seq_COG_diamond_blast_filter_anno.txt ~/Database/COG/COG2014/fun2003-2014.tab > Unique_COG_type_count.table


## unique_genes_with_atypical_GC_content
diamond blastp -d ~/Database/COG/COG2003 -q unique_genes_with_atypical_GC_content.txt -e 1e-5 -k 50 --sensitive -o unique_genes_with_atypical_GC_content_diamond_out.m8
python filter_diamond_cogblastp_out_m8.py unique_genes_with_atypical_GC_content_diamond_out.m8 > unique_genes_with_atypical_GC_content_diamond_out.filter.m8
python ../../scripts/diamond_COG_blast_anno_filter.py ~/Database/COG/COG2014/cog2003-2014.csv ~/Database/COG/COG2014/cognames2003-2014.tab unique_genes_with_atypical_GC_content_diamond_out.filter.m8 > Unique_genes_with_atypical_GC_content_COG_diamond_blast_filter_anno.txt
python ../../scripts/diamond_COG_count.py Unique_genes_with_atypical_GC_content_COG_diamond_blast_filter_anno.txt ~/Database/COG/COG2014/fun2003-2014.tab > Unique_genes_with_atypical_GC_content_COG_type_count.table

cut -f 3 core_cog_type_count.table >t1
cut -f 3 Accessory_COG_type_count.table >t2
cut -f 3 Unique_COG_type_count.table >t3
paste t1 t2 t3 > temp.matrix


