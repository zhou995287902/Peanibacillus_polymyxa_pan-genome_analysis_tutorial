## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## change time 2019-11-24
#encoding='utf-8'
import sys
import re

## use command
## python gbk2gff.py /mnt/d/share/Paenibacillus_polymyxa_pan_genome_project/strain_seq/input_directory/genomic_genebank/*_genomic.gbff

def open_gbk_file(file_name):
    res = {}
    is_True = False
    index = -1
    with open(file_name,'r')as read_file:
        lines = read_file.readlines()
        for line in lines:
            index += 1 
            if 'join' in line:
                gene_position = re.search(r'\d+\.\.\>?\d*\,\d+\.?\.?\>?\d*\)?\)?$',line)
            else: 
                gene_position = re.search(r'\d+\.\.\>?\d+\)?$',line)
            if line[5:9] == 'CDS ':
                locus_tag,product,protein_id,translation = '','','',''
                is_True = True
                # print(line)
                CDS_name = re.search(r'CDS_?[A-Z,a-z]*',line).group()
                CDS_position = gene_position.group()
                res[CDS_position] = {'CDS_name':CDS_name,'locus_tag':'','product':'','protein_id':'','translation':''}
            elif line[5:9] !='CDS ' and gene_position:
                is_True = False
            if is_True:
                CDS_start = CDS_position.split('..')[0].strip()
                res[CDS_position]['CDS_start'] = CDS_start
                CDS_end = CDS_position.split('..')[1].strip().strip(')')
                res[CDS_position]['CDS_end'] = CDS_end
                if '/locus_tag' in line:
                    locus_tag = line.split('=')[-1].strip().strip('"')
                    res[CDS_position]['locus_tag'] =locus_tag
                elif 'product' in line:
                    product= line.split('=')[-1].strip().strip('"')
                    res[CDS_position]['product'] = product
                elif 'protein_id' in line:
                    protein_id = line.split('=')[-1].strip().strip('"')
                    res[CDS_position]['protein_id'] =protein_id
                elif 'translation' in line:
                    translation += line.split('=')[-1].strip().strip('"')
                    next_index = index
                    while True:
                        next_index += 1 
                        next_line = lines[next_index]
                        # print(next_line[:21].strip())
                        if next_line[:21].strip() == '' and next_line[22] != '/':
                            # print(next_index,next_line[22:])
                            translation += next_line.strip().strip('"')
                        else:
                            break
                    res[CDS_position]['translation'] = translation
                # print(f'{CDS_start}\t{CDS_end}\t{locus_tag}\t{protein_id}\t{product}\t{translation}')
    return res


if __name__ =='__main__':
    for each_file in sys.argv[1:]:
        res = open_gbk_file(each_file)
        # print(res)
        wite_file_name = '.'.join(each_file.split('.')[:-1]).strip() + '.tab'
        write_file = open(wite_file_name,'w')
        for k ,v in res.items():
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(v['CDS_name'],v['CDS_start'],v['CDS_end'],v['locus_tag'],v['protein_id'],v['product'],v['translation']),file=write_file)
            # print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(v['CDS_name'],v['CDS_start'],v['CDS_end'],v['locus_tag'],v['protein_id'],v['product'],v['translation']))
        write_file.close()