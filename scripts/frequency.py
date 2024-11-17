import sys
import csv

frequency = {}
with open(sys.argv[1], "r") as f:
	for line in f:
		value = line.strip()
	if value in frequency:
		frequency[value] += 1
	else:
		frequency[value] = 1
total_count = sum(frequency.values())
with open(sys.argv[2], "w") as f2:
	for value, count in frequency.items():
		normalized_frequency = count / total_count
		f2.write(f"{value}\t{count}\t{normalized_frequency:.6f}\n")
