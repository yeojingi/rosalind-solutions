nucs = {'A': 0, 'C': 1, 'G': 2, 'T':3}
cnts = [0, 0, 0, 0]

dna = input()

for nuc in dna:
  cnts[nucs[nuc]] += 1

print(*cnts, sep=" ")