python sec_meta_type_count.py ./*/*.region*.gbk > sec_meta_type_length_new.table

python gbk2gff.py ./*/*.region*.gbk
                     
python tidy_sec_meta_pan_gene.py ../PAN_genome_analysis/sequence/core_seq.txt ../PAN_genome_analysis/sequence/accessory_seq.txt ../PAN_genome_analysis/sequence/unique_seq.txt ./*/*region*.tab > tidy_sec_meta_pan_gene.table
python get_metabolites.py ./*/knownclusterblast/*.txt > get_metabolites.table


