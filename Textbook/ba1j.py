def FrequentWordsWithMismatchesWithComplement(dna, k, d):
  L = len(dna)

  hashes = {}

  for i in range(L-k+1):
    window = dna[i:i+k]
    
    dDistancedKmers = GenerateMismatchedWordsWithD(window, d)
    dDistancedKmers += GenerateMismatchedWordsWithD(ReverseComplement(window), d)

    for kmers in dDistancedKmers:
      if not hashes.get(kmers):
        hashes[kmers] = 1
      else:
        hashes[kmers] += 1

  maxValue = 0
  maxKmers = []
  for key, value in hashes.items():
    if maxValue < value:
      maxKmers = [key]
      maxValue = value
    elif maxValue == value:
      maxKmers.append(key)

  return list(maxKmers)

def GenerateMismatchedWordsWithD(kmer, d):
  AAs = ['A', 'G', 'C', 'T']
  mismatcheds = []

  def rec(kmer, i, d):
    if d == 0:
      mismatcheds.append(kmer)
      return 
    if i >= len(kmer):
      mismatcheds.append(kmer)
      return

    cur = kmer[i]
    for aa in AAs:
      if aa == cur:
        rec(kmer, i+1, d)
      else:
        newKmer = kmer[:i] + aa + kmer[i+1:]
        rec(newKmer, i+1, d-1)

  rec(kmer, 0, d)

  return mismatcheds    

def ReverseComplement(dna):
  complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

  L = len(dna)

  reverseComplemented = ""

  for i in range(L):
    reverseComplemented += complement[dna[L-1 - i]]
  
  return reverseComplemented

name = input()
f = open(f"./data/{name}", "r")
dna = f.readline().strip()
k, d = map(int, f.readline().strip().split())
res = FrequentWordsWithMismatchesWithComplement(dna, k, d)
print(" ".join(res))
