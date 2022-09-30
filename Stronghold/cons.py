f = open("./data/rosalind_cons (1).txt", "r")
strands = []
strand = ""
line = f.readline()
while True:
  line = f.readline()
  if not line:
    strands.append(strand)
    break
  line = line.strip()
  if line[0] == '>':
    strands.append(strand)
    strand = ""
  else:
    strand += line

profile = [ [0, 0, 0, 0] for _ in range(len(strands[0]))]
consensus = ""

ACTG = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
actg = ['A', 'C', 'G', 'T']

for strand in strands:
  for i in range(len(strand)):
    profile[i][ACTG[strand[i]]] += 1

for i in range(len(profile)):
  maxIndex = 0
  maxValue = profile[i][0]
  for j in range(1, 4):
    if maxValue < profile[i][j]:
      maxIndex = j
      maxValue = profile[i][j]
  consensus += actg[maxIndex]

print(consensus)

for i in range(4):
  anss = []
  for j in range(len(profile)):
    anss.append(str(profile[j][i]))
  string = " ".join(anss)
  print(f"{actg[i]}: {string}")