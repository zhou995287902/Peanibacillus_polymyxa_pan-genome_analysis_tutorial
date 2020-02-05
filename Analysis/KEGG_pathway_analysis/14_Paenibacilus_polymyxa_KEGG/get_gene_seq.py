## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-12-2
# encoding='utf-8'

## use command
# python get_gene_seq.py nif_gene_structure_add_protein_id.table /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/genomic_sequence/no_plasmid_genomic/*.fna|less -S

import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

def get_gene_cluster_position(file_name):
	gene_cluster_position = {}
	strain_name = ''
	with open(file_name,'r')as read_file:
		for line in read_file:
			col_list = line.strip().split('\t')
			if col_list[0] != strain_name:
				strain_name = col_list[0]
				gene_cluster_position[strain_name] = []
			
			gene_cluster_position[strain_name].append(int(col_list[3]))
			gene_cluster_position[strain_name].append(int(col_list[4]))
	# print(gene_cluster_position)
	return gene_cluster_position



def reverse_seq(seq):
	tRNA = {'A':'T','T':'A','G':'C','C':'G'}
	Dna = ''
	for i in seq:
		Dna += tRNA[i]
	return Dna[::-1]


def get_fasta_seq(file_name,gene_cluster_position):
	strain_name = file_name.split('/')[-1].split('_')[0]
	if strain_name in gene_cluster_position:
		for seq_record in SeqIO.parse(file_name, "fasta"):
			# print(seq_record.id)
			start = int(min(gene_cluster_position[strain_name]))
			end = int(max(gene_cluster_position[strain_name]))
			# print(start,end)
			my_seq = Seq(str(seq_record.seq),IUPAC.unambiguous_dna)
			gene_cluster = my_seq[start-1:end-1]
			# print(seq_record.seq)
			gc_values = GC(gene_cluster)
			if strain_name == 'Sb3-1':
				print(strain_name,gene_cluster[::-1])
				gc_values = GC(reverse_seq(gene_cluster))
			else:
				print(strain_name,gene_cluster)
		# print(f'{strain_name}\t{gc_values}')

if __name__ == '__main__':
	# print(get_gene_cluster_position(sys.argv[1]))
	gene_cluster_position = get_gene_cluster_position(sys.argv[1])
	for each_file in sys.argv[2:]:
		get_fasta_seq(each_file,gene_cluster_position)