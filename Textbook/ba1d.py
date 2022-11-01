def PatternMatching(Pattern, Genome):
  indices = []
  for i in range(len(Genome) - len(Pattern) + 1):
    window = Genome[i:i+len(Pattern)]

    if window == Pattern:
      indices.append(str(i))
  
  return " ".join(indices)