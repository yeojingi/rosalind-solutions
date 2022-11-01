from ba1g import hamming_distance

def approximate_pattern_matching(pattern, dna, d):
  k = len(pattern)
  L = len(dna)

  indices = []

  for i in range(L - k + 1):
    window = dna[i:i+k]

    window_d = hamming_distance(pattern, window)
    if window_d <= d:
      indices.append(i)

  return " ".join(list(map(str, indices)))