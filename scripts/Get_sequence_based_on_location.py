## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-15
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-


import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

def get_fasta_seq(fasta_file):
    seq = {}
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        seq[seq_record.id] = str(seq_record.seq)
        # print(repr(seq_record.seq))
        # print(len(seq_record))
    # print(seq_record.id,seq[seq_record.id])
    return seq


def get_protein_id(cluster_file,seq):
    with open(cluster_file) as read_file:
        lines = read_file.readlines()
        for line in lines[:8]:
            col_list = line.split('\t')
            protein_id = col_list[3]
            print('>'+protein_id+'\n'+seq[protein_id])


if __name__ =='__main__':
    fasta_file = sys.argv[1]
    seq = get_fasta_seq(fasta_file)
    # print(seq)
    protein_id = ['APQ57336.1','APQ57337.1','APQ57338.1','APQ57339.1',"APQ57340.1","APQ57341.1","APQ57342.1"]
    # get_protein_id(sys.argv[2],seq)
    for i in protein_id:
        print(f'>{i}\n{seq[i]}')