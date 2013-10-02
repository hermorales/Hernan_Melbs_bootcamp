import sys
sequence = ('AGTCGTACG')
#sequence = set(sequence)
a = sequence.count('A')
c = sequence.count('C')
t = sequence.count('T')
g = sequence.count('G')
print(sequence)
base_count = {'A' : a, 'G' : g, 'C' : c, 'G' : g} 
print(base_count)

###  EXTENDED SOLUTION

sequence2 = "GTGTACGTACGGACAACTAGCAACACGTGCACAC"
is_rna = False
if 'U' in sequence2:
    is_rna = True
sequence2 = sequence2.replace('U', 'T')
g = sequence2.count('G')
a = sequence2.count('A')
t = sequence2.count('T')
c = sequence2.count('C')
base_counts = {'G': g, 'A': a, 'T': t, 'C': c}
total_length = g+a+t+c
gc_content = (g+c)/float(total_length) * 100
base_counts['U'] = base_counts['T']
del base_counts['T']
print sequence2
print base_counts
print gc_content



