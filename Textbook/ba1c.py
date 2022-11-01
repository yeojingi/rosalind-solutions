def ReverseComplement(Pattern):
  complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

  newPattern = []
  for i in range(len(Pattern)):
    newPattern.append(complement[Pattern[len(Pattern) - 1 - i]])

  return "".join(newPattern)