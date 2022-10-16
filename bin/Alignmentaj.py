print("Please install the BioPyton package first.")
a = input('Specify the path to the fasta file 1: ')
b = input('Specify the path to the fasta file 2: ')
j = int(input('Write the number of proposed amino acid sequences: '))
from Bio.SeqIO import parse
file = open(a)
records = parse(file, 'fasta')
for record in records:
    record.seq

file1 = open(b)
humans = parse(file1, 'fasta')
for human in humans:
    human.seq

a = record.seq
b = human.seq
c = len(human.seq)
for i in range(c):
    if b[i:i+j] in a:
        print(b[i:i+j])

print('Results ready!')

