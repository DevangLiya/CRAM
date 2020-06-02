# CRAM - Conserved Residues from Multisequence Alignment 

1. generate_masterseq.py: A master sequence consisting of 1 for the nucleotide position that is conserved across all the genomes and 0 for the nucleotide position that is not conserved is produced for the given alignment using the program. It is possible to generate master sequences from multiple alignment files at once.
2. score.py: A frame of given size is moved across the entire length of the master sequence and each instance of frame is given a score between 0 and 100 to represent the level of conservation by counting the number of 1s in that frame. Starting position of every frame between the given threshold is reported in a file conserved.txt
