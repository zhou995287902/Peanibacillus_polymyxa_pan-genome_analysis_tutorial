## author: zhouliangliang
## email: zhouliangliang2018@gmail.com
## create time : 2019-12-30
#!/usr/bin/Python3.7
# -*- coding: utf-8 -*-
import sys

with open(sys.argv[1],'r')as f:
	seq_name_list = {}
	for line in f:
		col_list = line.split('\t')
		seq_name = col_list[0].strip()
		identity = float(col_list[2].strip())
		Score = float(col_list[-1].strip())
		if identity < 40:
			continue
		if seq_name not in seq_name_list :
			seq_name_list[seq_name] = line
			last_score = Score
		else:
			if Score > last_score:
				seq_name_list[seq_name] = line
print("Query_id\tSubject_id\tidentity\talignment_length\tmismatches\tgap_openings\tq.start\tq.end\ts.start\ts.end\te-value\tbit_score\t")
for k,v in seq_name_list.items():
	print(v,end='')



