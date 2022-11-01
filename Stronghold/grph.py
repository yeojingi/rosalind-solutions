f = open('./data/rosalind_grph (1).txt', 'r')

strands = {}
strand = ""
fileName = ""
fileNames = []

while True:
  line = f.readline().strip()

  if not line:
    strands[fileName] = strand
    fileNames.append(fileName)
    break
  if line[0] == '>':
    if strand:
      strands[fileName] = strand
      fileNames.append(fileName)
    fileName = line[1:]
    strand = ""
  else:
    strand += line
  
N = len(fileNames)

print(strands)
anss = []
for i in range(N):
  cur = strands[fileNames[i]]
  for j in range(i+1, N):
    target = strands[fileNames[j]]
    
    if cur[-3:] == target[:3]:
      ans = [fileNames[i], fileNames[j]]
      anss.append(" ".join(ans))

    elif cur[:3] == target[-3:]:
      ans = [fileNames[j], fileNames[i]]
      anss.append(" ".join(ans))

fo = open('./data/output.txt', 'w')
fo.write("\n".join(anss))
fo.close()