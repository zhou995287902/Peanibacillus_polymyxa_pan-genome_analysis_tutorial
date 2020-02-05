# encoding='utf-8'

import sys
import re

def open_file(fielname):
    with open(filename,'r')as f:
        line_one = f.readline().strip()
        genome_size = re.search(r'\d+ bp',line_one).group()
        genome_name = '/'.join(filename.split('/')[-2:]).replace('.gbk','')

    # print(f'{genome_name}:{genome_size}')
    return genome_name,genome_size


if __name__ == '__main__':
    print('Strain\tGenome_size\tSecondary_metabolite_size\tRatio')
    all_genome_size = {}
    dir_name = ''
    count = 0
    complete_genome_size = 1
    for filename in sys.argv[1:]:
        genome_name,genome_size=open_file(filename)
        all_genome_size[genome_name] = genome_size
    for k,v in all_genome_size.items():
        if dir_name != k.split('/')[0].strip():
            if dir_name :
                print('{}\t{}\t{}\t{:.2%}'.format(dir_name.split('_GC')[0],complete_genome_size,count,count/complete_genome_size))
            dir_name = k.split('/')[0].strip()
            count = 0
            if 'region' not in k:
                complete_genome_size = int(v.split(' ')[0])
            else:
                count += int(v.split(' ')[0])
        else:
            if 'region' not in k:
                complete_genome_size = int(v.split(' ')[0])
            else:
                count += int(v.split(' ')[0])
    print('{}\t{}\t{}\t{:.2%}'.format(dir_name.split('_GC')[0],complete_genome_size,count,count/complete_genome_size))
