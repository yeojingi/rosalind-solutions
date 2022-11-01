def minimum_skew(dna):
  minValue = 0
  minIndices = [0]

  value = 0
  for i in range(len(dna)):
    nucleotide = dna[i]

    # print(value, end=" ")
    if value < minValue:
      minValue = value
      minIndices = [i]
    elif value == minValue:
      minIndices.append(i)

    if nucleotide == 'C':
      value -= 1
    elif nucleotide == 'G':
      value += 1
  
  if value < minValue:
    minValue = value
    minIndices = [len(dna)]
  elif value == minValue:
    minIndices.append(len(dna))

  return " ".join(list(map(str, minIndices)))