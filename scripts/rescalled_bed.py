import sys

query = {}
tracking_query = {}
with open(sys.argv[1], "r") as f1:
	for line in f1:
	columns = line.strip().split("\t")
	query[columns[0]]=columns[1]
	tracking_query[columns[0]]=0

w = open(sys.argv[3], "w")

with  open(sys.argv[2], "r") as f2:
	for line in f2:
		line = line.strip().split("\t")
		if (line[3] in query) and (tracking_query[line[3]] < query[line[3]]):
			w.write(line)
			tracking_query[line[3]] += 1
w.close()
	
