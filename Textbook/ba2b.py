import math


filename = "rosalind_ba2b.txt"
f = open(f"./data/{filename}", "r")
k = int(f.readline().strip())
dnas = []
while True:
  line = f.readline().strip()
  if not line:
    break

  dnas.append(line)

def hamming_distance(pattern, window):
  if len(pattern) != len(window):
    print("hamming_distance, length error")
    return
  d = 0
  for i in range(len(pattern)):
    if pattern[i] != window[i]:
      d += 1
  
  return d

def generate_kmer(k):
  nucleotides = ['A', 'C', 'G', 'T']

  kmers = []
  def rec(string, n):
    if n == 0:
      kmers.append(string)
      return
    
    for nucloetide in nucleotides:
      rec(string + nucloetide, n-1)
  
  rec("", k)
  return kmers

kmers = generate_kmer(k)
minDAll = math.inf
minKmerAll = []
for kmer in kmers:
  d_sum = 0
  for dna in dnas:
    minD = math.inf
    L = len(dna)
    for i in range(L - k + 1):
      window = dna[i:i+k]
      d = hamming_distance(window, kmer)
      if minD > d:
        minD = d
    d_sum += minD
  
  if minDAll > d_sum:
    minDAll = d_sum
    minKmerAll = [kmer]
  elif minDAll == d_sum:
    minKmerAll.append(kmer)

print(minKmerAll)