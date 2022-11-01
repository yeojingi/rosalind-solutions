name = "ba2a.txt"
f = open(f"./data/{name}", "r")

k, d = map(int, f.readline().strip().split())
dnas = []
while True:
  line = f.readline().strip()
  if not line:
    break

  dnas.append(line)

kmers = {}

def genDMismatches(pattern, d):
  nucleotides = ['A', 'C', 'G', 'T']
  patterns = []
  def rec(s, i, d):
    if i == len(pattern):
      patterns.append(s)
      return

    for nuc in nucleotides:
      if pattern[i] == nuc:
        rec(s + nuc, i+1, d)
      else:
        if d > 0:
          rec(s + nuc, i+1, d-1)
  
  rec("", 0, d)
  
  return patterns

for nDna in range(len(dnas)):
  dna = dnas[nDna]
  L = len(dna)

  for i in range(L - k + 1):
    window = dna[i:i+k]

    mismatches = genDMismatches(window, d)

    for mismatch in mismatches:
      if kmers.get(mismatch):
        kmers[mismatch] |= int(2**(nDna))
      else:
        kmers[mismatch] = int(2**(nDna))

patterns = []
for key, value in kmers.items():
  print(key, value)
  if value == 2**len(dnas) - 1:
    patterns.append(key)

print(*patterns, sep=" ")