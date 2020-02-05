## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

import sys
import os
# use command
# python prediction_16SrRNA.py /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/genomic_sequence/no_plasmid_genomic/*.fna

all_seq_file_names = sys.argv[1:]

for each_file in all_seq_file_names:
    strain_name = each_file.split('/')[-1].split('_')[0]
    print('~/biosoft/rnammer-1.2/rnammer -S bac -m ssu -xml {0}.xml -gff {0}.gff -h {0}.hmmreport -f {0}.fsa < {1}'.format(strain_name,each_file))
    # os.system('~/biosoft/rnammer-1.2/rnammer -S bac -m ssu -xml {0}.xml -gff {0}.gff -h {0}.hmmreport -f {0}.fsa < {1}'.format(strain_name,each_file))

# all_file_names = sys.argv[1:]

write_file = open('14_strain_16SrRNA_1.fasta','w')
for each_file in all_seq_file_names:
	seq = {}
	strain_name = each_file.split('/')[-1].split('_')[0]
	# print(strain_name)
	fsa_file = strain_name + '.fsa'
	print(fsa_file)
	with open(fsa_file,'r') as f:
		for line in f:
			if '>' in line[0]:
				seq_name = line[:16]
				seq[seq_name] = ''
			else:
				seq[seq_name] += line.strip()

	write_file.write('>'+strain_name+'\n'+seq[seq_name]+'\n')

write_file.close()    