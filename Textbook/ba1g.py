def hamming_distance(dna1, dna2):
  score = 0
  for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
      score += 1

  return score