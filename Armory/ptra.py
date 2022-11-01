from Bio.Seq import translate

f = open(f"./data/rosalind_ptra (3).txt", 'r')
dna = f.readline().strip()
protein = f.readline().strip()

ans = 0
for i in [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33]:

  p = translate(dna, table=i, to_stop=True, stop_symbol='*')
  if protein == p:
    print(i)
    exit()