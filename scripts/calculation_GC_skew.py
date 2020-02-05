## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2020-01-02
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

# use command
# python calculation_GC_skew.py 10000 /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/genomic_sequence/no_plasmid_genomic/*.fna > all_genome_sequence_GC_skew.txt

import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

def get_fasta_seq(fasta_file):
    seq = {}
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        seq[seq_record.id] = str(seq_record.seq)
        
    return seq

def GC_skew_calculation(seq,num):
	GC_skews = {}
	for k,v in seq.items():
		j = 0
		for index in range(10000,len(v),10000):
			G,C = 0,0
			for i in v[j:index]:
				if i == 'G':
					G += 1
				elif i == 'C':
					C += 1
			GC_skew = (G-C)/(G+C)
			# print(j,index)
			# print(v[j:index])
			print(f'{k}\t{j+1}\t{index}\t{GC_skew}')
			j = index


if __name__ == '__main__':
	for each_file in sys.argv[2:]:
		seq = get_fasta_seq(each_file)
		GC_skew_calculation(seq,sys.argv[1])