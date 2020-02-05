## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-
import sys

def open_COG_anno(COG_anno):
    with open(COG_anno,'r')as f:
        cog_type = {}
        lines = f.readlines()
        for line in lines[1:]:
            COG_func = line.split('\t')[3].strip()
            if COG_func not in cog_type:
                cog_type[COG_func] = 1
            else:
                cog_type[COG_func] +=1

    return cog_type

def open_fun_txt(fun_txt):
    fun_type = {}
    with open(fun_txt,'r')as read_fun_txt:
        lines = read_fun_txt.readlines()
        for line in lines[1:]:
            col_list = line.split('\t')
            Code = col_list[0].strip()
            Name = col_list[1].strip()
            fun_type[Code] = Name
    return fun_type


if __name__ =='__main__':
    COG_anno = sys.argv[1]
    cog_type = open_COG_anno(COG_anno)
    fun_type = open_fun_txt(sys.argv[2])
    print('Code\tFunctional-Categories\tGene-Number')
    for k,v in cog_type.items():
        print(f"{k}\t{fun_type[k]}\t{v}")
