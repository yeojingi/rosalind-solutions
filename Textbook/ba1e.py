def clump_finding(genome, k, L, t):
  clumps = set()

  patterns_scores = {}

  for i in range(L - k + 1):
    window = genome[i:i+k]

    if not patterns_scores.get(window):
      patterns_scores[window] = 1
    else:
      patterns_scores[window] += 1

  for key, value in patterns_scores.items():
    if value >= t:
      clumps.add(key)

  for l in range(1, len(genome) - L + 1):
    window = genome[l-1:l+k-1]
    patterns_scores[window] -= 1

    window = genome[l+L-k:l+L]
    if not patterns_scores.get(window):
      patterns_scores[window] = 1
    else:
      patterns_scores[window] += 1

    if patterns_scores[window] >= t:
      clumps.add(window)
  
  return ' '.join(list(clumps))