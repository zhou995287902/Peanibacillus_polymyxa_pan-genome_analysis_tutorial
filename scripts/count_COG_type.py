## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1],'r')as f:
    cog_type = {}
    for line in f:
        col_2 = line.split('\t')[1].strip()
        if col_2:
            if ',' not in col_2:
                if col_2 not in cog_type:
                    cog_type[col_2] = 1
                else:
                    cog_type[col_2] +=1
            else:
                for i in col_2.split(','):
                    if i.strip() not in cog_type:
                        cog_type[i.strip()] = 1
                    else:
                        cog_type[i.strip()] +=1
print('Code\tFunctional-Categories\tGene-Number')
for k,v in cog_type.items():
    print(f"{k}\t{v}")
