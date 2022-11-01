dna = "TATTAGAAACACGACAAAAGTTGGGCCGAC"

ans = 0

L = len(dna)

nuc = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for i in range(L):
  ans += nuc[dna[i]] * 4**(L-1-i)

print(ans)