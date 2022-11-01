def greedy_motif_search(Dnas, k, t):
  bestmotifs = [ Dna[0:k] for Dna in Dnas ]
  L = len(Dnas[0])

  for l in range(L - k + 1):
    motifs = [ Dnas[0][l:l+k] ]

    for i in range(1, t):
      profile = form_profile(motifs, k)
      motif = most_probable_in_dna(Dnas[i], profile, k)
      motifs.append(motif)
    
    if scoring(motifs, k) < scoring(bestmotifs, k):
      bestmotifs = motifs
  
  return "\n".join(bestmotifs)

def form_profile(motifs, k):
  nucleotides_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

  profile = [ [1] * k for _ in range(4) ]
  t = len(motifs)
  
  for motif in motifs:
    for i in range(k):
      profile[ nucleotides_dict[motif[i]] ][i] += 1
  
  for i in range(4):
    for j in range(k):
      profile[i][j] /= (t + 4)

  return profile

def most_probable_in_dna(Dna, profile, k):
  nucleotides_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
  L = len(Dna)
  
  maxP = 0
  maxKmer = ""

  for i in range(L - k + 1):
    window = Dna[i:i+k]
    p = 1

    for j in range(k):
      nucleotide = window[j]
      p *= profile[ nucleotides_dict[nucleotide] ][j]
    
    if p > maxP:
      maxP = p
      maxKmer = window
  
  return maxKmer

def scoring(motifs, k):
  profile = form_profile(motifs, k)
  kmer = most_probable_in_profile(profile, k)

  score = 0
  for motif in motifs:
    d = hamming_distance(motif, kmer)
    score += d
  
  return score

def most_probable_in_profile(profile, k):
  nucleotides_arr = ['A', 'C', 'G', 'T']
  kmer = ""

  for j in range(k):
    p = 0
    maxNucleotide = ""
    for i in range(4):
      if profile[i][j] > p:
        p = profile[i][j]
        maxNucleotide = nucleotides_arr[i]
    kmer += maxNucleotide
  
  return kmer

def hamming_distance(target, pattern):
  d = 0
  
  for i in range(len(pattern)):
    if target[i] != pattern[i]:
      d += 1
  
  return d

filename = "rosalind_ba2e.txt"
f = open(f"./data/{filename}", "r")
k, t = map(int, f.readline().strip().split())
Dnas = [ f.readline().strip() for _ in range(t)]
res = greedy_motif_search(Dnas, k, t)
print(res)