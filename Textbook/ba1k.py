def FrequencyArray(dna, k):
  kmers = GenerateKmers(k)
  hashes = {kmer: 0 for kmer in kmers}

  L = len(dna)
  for i in range(L-k+1):
    window = dna[i:i+k]

    hashes[window] += 1
  
  anss = []
  for kmer in kmers:
    anss.append(str(hashes[kmer]))
  
  return " ".join(anss)

def GenerateKmers(k):
  nucleotides = ['A', 'C', 'G', 'T']

  kmers = []
  def rec(k, kmer):
    if k == 0:
      kmers.append(kmer)
      return
    
    for nucleotide in nucleotides:
      rec(k-1, kmer + nucleotide)
  
  rec(k, "")

  return kmers

filename = input()
f = open(f"./data/{filename}", "r")
dna = f.readline().strip()
k = int(f.readline().strip())
res = FrequencyArray(dna, k)
print(res)