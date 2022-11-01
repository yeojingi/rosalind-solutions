def greedy_motif_search(Dnas, k, t):
  bestmotifs = [ Dna[0:k] for Dna in Dnas ]
  L = len(Dnas[0])
  for j in range(L - k + 1):
    window = Dnas[0][j:j+k]
    motifs = [ window ]

    for i in range(1, t):
      profile = form_profile(motifs, k)
      motif_i = most_probable_kmer(Dnas[i], profile, k)
    
      motifs.append(motif_i)
    if score(motifs, k) < score(bestmotifs, k):
      bestmotifs = motifs
  
  return "\n".join(bestmotifs)


def form_profile(motifs, k):
  nucleotides = ['A', 'C', 'G', 'T']
  profile = { nucleotide: [0] * k for nucleotide in nucleotides }
  
  for motif in motifs:
    for i in range(k):
      nucleotide = motif[i]
      profile[nucleotide][i] += 1
  
  for i in nucleotides:
    for j in range(k):
      profile[i][j] /= len(motifs)
  
  return profile

def most_probable_kmer(Dna, profile, k):
  maxP = 0
  maxKmer = Dna[0:k]
  L = len(Dna)

  for i in range(L - k + 1):
    window = Dna[i:i+k]
    p = 1

    for j in range(k):
      nucleotide = window[j]
      p *= profile[nucleotide][j]
    
    if p > maxP:
      maxP = p
      maxKmer = window
  
  return maxKmer

def score(motifs, k):
  bestKmer = best_from_motifs(motifs, k)
  d = 0

  for motif in motifs:
    d += hamming_distance(motif, bestKmer)
  
  return d

def best_from_motifs(motifs, k):
  nucleotides = ['A', 'C', 'G', 'T']

  profile = form_profile(motifs, k)
  bestKmer = ""

  for j in range(k):
    maxP = 0
    maxNucleotide = ""
    for i in nucleotides:
      if profile[i][j] > maxP:
        maxP = profile[i][j]
        maxNucleotide = i
    bestKmer += maxNucleotide
  
  return bestKmer

def hamming_distance(target, pattern):
  d = 0
  for i in range(len(target)):
    if target[i] != pattern[i]:
      d += 1
  return d

filename = "rosalind_ba2d.txt"
f = open(f"./data/{filename}", "r")
k, t = map(int, f.readline().strip().split())
Dnas = [ f.readline().strip() for _ in range(t) ]
res = greedy_motif_search(Dnas, k, t)
print(res)