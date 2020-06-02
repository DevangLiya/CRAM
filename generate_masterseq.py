#A program to generate master sequence of 1s and 0s for scoring

import pandas as pd 

names = ['data/alignment.fasta']

def make_df(fname):
	print("Opening the alignment file " + fname + " and reading the sequences")
	sequence = ""
	with open(fname, 'r') as fh:
		for line in fh:
			if line.startswith('>'):
				all_sequences.append(list(sequence.upper()))
				all_names.append(line)
				sequence = ""
			else:
				sequence = sequence + line.strip()

	all_sequences.append(list(sequence.upper()))	#Add the last sequence
	del all_sequences[0]	#Delete first empty string

	print("Converting sequences to DataFrame")
	df = pd.DataFrame(all_sequences)
	return df

outf = open('master_sequences', 'w')

for fname in names:
	outf.write('>' + fname.split('.')[0] + '\n')

	all_names = []
	all_sequences = []

	df = make_df(fname)

	print("Looking for mutations")

	acc_seq = ''
	for position in range(len(all_sequences[0])):
		if position%1000 == 0:
			print("At position %d/%d" %(position, len(all_sequences[0])))
		currect_nucleotide = df[position][0]
		if not all(df[:][position] == currect_nucleotide):
			acc_seq = acc_seq + '0'
		else:
			acc_seq = acc_seq + '1'

	outf.write(acc_seq)

outf.close()