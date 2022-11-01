def FrequentWords(Text, k):
  kmers = {}

  for i in range(len(Text) - k + 1):
    window = Text[i:i+k]

    if not kmers.get(window):
      kmers[window] = 1
    else:
      kmers[window] += 1

  maxKeys = ""
  maxValue = 0
  for key, value in kmers.items():
    if maxValue < value:
      maxValue = value
      maxKeys = [key]
    elif maxValue == value:
      maxKeys.append(key)
  
  return " ".join(maxKeys)