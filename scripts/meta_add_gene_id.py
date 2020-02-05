## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time: 2019-12-16
# encoding='utf-8'

import sys
## Tridecaptin gene ID
gene_id = {'AHF21225.1':"triA",'AHF21226.1':"triB",'AHF21227.1':"triC",'AHF21228.1':"triD",'AHF21229.1':"triE"}


## Fusaricidin gene ID
#gene_id = {'ACA34357.1':'fusG',"ACA34358.1":"fusF",'ACA34359.1':'fusE','ACA34360.1':'fusD','ACA34361.1':'fusC','ACA34362.1':"fusB",\
# 'ABQ96384.2':"fusA",'ACA34363.1':"fusTE",'ACZ01943.1':"fusG",'ACZ01944.1':"fusF",'ACZ01945.1':'fusE','ACZ01946.1':'fusD','ACZ01947.1':'fusC',\
# 'ACZ01948.1':'fusB','ACA09733.2':"fusA",}

## Paenilan gene ID 
# gene_id = {'PPE_01446':'pnlR2','PPE_01448':'pnlK','PPE_01449':'pnlF','PPE_01450':'pnlG','PPE_01451':'pnlE','PPE_01452':'pnlC2',\
# 'PPE_04953':'pnlA','PPE_01453':'pnlC1',"PPE_01454":"pnlR1","PPE_01455":"pnlB","PPE_01456":"pnlT"}
with open(sys.argv[1],'r') as read_file:
	for line in read_file:
		col_list = line.strip().split('\t')
		protein_id = col_list[3]
		tt = '\t'.join(col_list[:-1])
		print(f'{tt}\t{gene_id[protein_id]}')