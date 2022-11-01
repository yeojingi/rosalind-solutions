filename = "rosalind_ba2c.txt"
f = open(f"./data/{filename}", "r")
dna = f.readline().strip()
k = int(f.readline().strip())
profile = [ list(map(float, f.readline().strip().split())) for _ in range(4)]
nucleotides = {'A':0, 'C':1, 'G': 2, 'T': 3}

maxP = 0
maxPattern = ""

L = len(dna)

for i in range(L - k + 1):
  window = dna[i:i+k]

  p = 1
  for j in range(k):
    p *= profile[nucleotides[window[j]]][j]
  
  if p > maxP:
    maxP = p
    maxPattern = [window]
  elif p == maxP:
    maxPattern.append(window)


print(maxPattern)