## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-
import sys
import re

def open_whog(filename):
    anno = {}
    is_true = False
    with open(filename,'r')as read_file:
        for line in read_file:
            if '[' == line[0]:
                is_true = True
            elif '_______' in line:
                is_true = False

            if is_true:
                if '[' == line[0]:
                    # Functional_Category = re.search(r'\[([A-Z]+)\]',line).group(1)
                    # Ortholog_Group = re.search(r' COG\d+ ',line).group()
                    Functional_Group = line.strip()
                else:
                    subject_id = line.split(':')[-1].strip().split(' ')
                    for i in subject_id:
                        anno[i] = Functional_Group
                    # COG_id = line.split(':')[0].strip()
                    
    return anno

def open_fun(filename):
    Functional_Categorys = {}
    with open(filename,'r') as read_file:
        for line in read_file:
            if '[' in line :
                Functional_Category = re.search(r'\[([A-Z]+)\]',line).group(1)
                Functional_anno = re.search(r'[^\]].*',line).group().strip()
                Functional_Categorys[Functional_Category] = Functional_anno

    return Functional_Categorys

                
def open_diamond_out(filename):
    Query_subject = {}
    with open(filename,'r') as read_file:
        lines = read_file.readlines()
        for line in lines[1:]:
            col_list = line.split('\t')
            Query_id = col_list[0].strip()
            subject_id = col_list[1].strip()
            Query_subject[Query_id] = subject_id
    return Query_subject



if __name__ == '__main__':
    anno = open_whog(sys.argv[1])
    Functional_Categorys = open_fun(sys.argv[2])
    Query_subject = open_diamond_out(sys.argv[3])
    print(f"Query_id\tSubject_id\tOrtholog_Group\tFunctional_Category\tOG_Description")
    for k,v in Query_subject.items():
        Ortholog_Group = anno[v].split(' ')[1].strip()
        Functional_Category = anno[v].split(' ')[0].strip().strip('[').strip(']')
        for i in Functional_Category:
            OG_Description = Functional_Categorys[Functional_Category]
            print(f"{k}\t{v}\t{Ortholog_Group}\t{Functional_Category}\t{OG_Description}")
                









