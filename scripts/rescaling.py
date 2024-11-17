import sys

query = {}
ref = {}
scaling = {}
with open(sys.argv[1], "r") as q:
	for line in q:
		line = line.strip().split("\t")
		query[line[0]] = line[2]
		scaling[line[0]] = line[1]
with open(sys.argv[2], "r") as r:
	for line in r:
		line = line.strip().split("\t")
		ref[line[0]] = line[1]

max_dif = 0
max_key = None

com_keys = set(query.keys()) & set(ref.keys())
for key in com_keys:
	if ref[key] > query[key]:
		dif = ref[key] - query[key]
		if dif > max_dif:
			max_dif = dif
			max_key = key
scaling_factor = float(max_key)/ref[max_key]
rescaling = {key: round(value * scaling_factor) for key, value in scaling.items()}

with open(sys.argv[3], "w") as s:
	for key, value in rescaling.items():
	s.write(f"{key}\t{value}\n")
