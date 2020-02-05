## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-

import sys
import requests
import re

if len(sys.argv) != 2:
    print('\nuseage:\npython3 get_assembly_name.py <input_txt> \nexample:\npython3 get_assembly_name.py bacillus_amyloiquefaciens_strain_list \n')
    exit()

# 获取网页内容
def get_web_content(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}                        
    response = requests.get(url,headers = header)    
    return response

with open(sys.argv[1],'r') as read_file:
    lines = read_file.readlines()
    for line in lines[1:]:
        col_list = line.strip().split('\t')
        assembly_num = col_list[1].strip()
        # print(assembly_num)
        url = 'https://www.ncbi.nlm.nih.gov/assembly/' + assembly_num
        # print(url)
        web_content = get_web_content(url).text
        # print(web_content)
        assembly_name = re.search(r'<title>(.*)</title>',web_content).group(1)
        assembly_name = assembly_name.split('-')[0].strip()
        col_list.append(assembly_name)
        print('\t'.join(col_list))
        
